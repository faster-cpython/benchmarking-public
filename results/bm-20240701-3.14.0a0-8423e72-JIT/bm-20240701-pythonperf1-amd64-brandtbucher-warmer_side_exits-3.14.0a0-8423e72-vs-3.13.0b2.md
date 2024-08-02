# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-amd64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.00x slower
- HPT reliability: 99.26%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 238 ms: 1.15x slower                                                          |
| docutils       | 1.63 sec                                                        | 1.78 sec: 1.10x slower                                                        |
| html5lib       | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                                         |
| tornado_http   | 81.8 ms                                                         | 84.1 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg        | 605 ms                                                          | 528 ms: 1.15x faster                                                          |
| async_tree_io           | 588 ms                                                          | 550 ms: 1.07x faster                                                          |
| async_tree_none         | 218 ms                                                          | 208 ms: 1.05x faster                                                          |
| async_tree_none_tg      | 202 ms                                                          | 193 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed | 389 ms                                                          | 383 ms: 1.02x faster                                                          |
| Geometric mean          | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                         |
| float          | 49.7 ms                                                         | 45.9 ms: 1.08x faster                                                         |
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                          |
| regex_compile  | 78.0 ms                                                         | 89.4 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                  |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                        |
| unpickle_pure_python | 122 us                                                          | 118 us: 1.04x faster                                                          |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.6 ms: 1.01x faster                                                         |
| xml_etree_generate   | 53.2 ms                                                         | 54.5 ms: 1.02x slower                                                         |
| json_loads           | 14.2 us                                                         | 14.5 us: 1.03x slower                                                         |
| xml_etree_parse      | 90.9 ms                                                         | 94.1 ms: 1.04x slower                                                         |
| pickle_pure_python   | 175 us                                                          | 183 us: 1.04x slower                                                          |
| json_dumps           | 5.61 ms                                                         | 5.95 ms: 1.06x slower                                                         |
| xml_etree_process    | 36.4 ms                                                         | 39.3 ms: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.0 ms: 1.03x slower                                                         |
| python_startup_no_site | 16.2 ms                                                         | 17.4 ms: 1.07x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.15 ms: 1.23x faster                                                         |
| django_template | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                         |
| genshi_text     | 14.4 ms                                                         | 18.6 ms: 1.29x slower                                                         |
| genshi_xml      | 31.6 ms                                                         | 43.7 ms: 1.38x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 530 us: 15.31x faster                                                         |
| deepcopy_memo            | 22.1 us                                                         | 16.2 us: 1.36x faster                                                         |
| spectral_norm            | 63.7 ms                                                         | 47.4 ms: 1.35x faster                                                         |
| nbody                    | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                         |
| mako                     | 6.36 ms                                                         | 5.15 ms: 1.23x faster                                                         |
| deepcopy                 | 220 us                                                          | 185 us: 1.19x faster                                                          |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.10 ms: 1.19x faster                                                         |
| scimark_fft              | 171 ms                                                          | 147 ms: 1.16x faster                                                          |
| async_tree_io_tg         | 605 ms                                                          | 528 ms: 1.15x faster                                                          |
| crypto_pyaes             | 45.5 ms                                                         | 40.9 ms: 1.11x faster                                                         |
| deepcopy_reduce          | 1.99 us                                                         | 1.83 us: 1.09x faster                                                         |
| float                    | 49.7 ms                                                         | 45.9 ms: 1.08x faster                                                         |
| fannkuch                 | 243 ms                                                          | 227 ms: 1.07x faster                                                          |
| async_tree_io            | 588 ms                                                          | 550 ms: 1.07x faster                                                          |
| telco                    | 4.67 ms                                                         | 4.39 ms: 1.06x faster                                                         |
| json                     | 3.19 ms                                                         | 3.00 ms: 1.06x faster                                                         |
| tomli_loads              | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                        |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.41 sec: 1.05x faster                                                        |
| pyflate                  | 279 ms                                                          | 266 ms: 1.05x faster                                                          |
| async_tree_none          | 218 ms                                                          | 208 ms: 1.05x faster                                                          |
| async_tree_none_tg       | 202 ms                                                          | 193 ms: 1.05x faster                                                          |
| unpickle_pure_python     | 122 us                                                          | 118 us: 1.04x faster                                                          |
| comprehensions           | 10.4 us                                                         | 10.1 us: 1.02x faster                                                         |
| scimark_monte_carlo      | 39.1 ms                                                         | 38.3 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed  | 389 ms                                                          | 383 ms: 1.02x faster                                                          |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.6 ms: 1.01x faster                                                         |
| pidigits                 | 150 ms                                                          | 149 ms: 1.01x faster                                                          |
| pprint_safe_repr         | 474 ms                                                          | 477 ms: 1.01x slower                                                          |
| pprint_pformat           | 966 ms                                                          | 978 ms: 1.01x slower                                                          |
| regex_dna                | 119 ms                                                          | 121 ms: 1.02x slower                                                          |
| bench_thread_pool        | 768 us                                                          | 782 us: 1.02x slower                                                          |
| xml_etree_generate       | 53.2 ms                                                         | 54.5 ms: 1.02x slower                                                         |
| create_gc_cycles         | 888 us                                                          | 910 us: 1.03x slower                                                          |
| json_loads               | 14.2 us                                                         | 14.5 us: 1.03x slower                                                         |
| tornado_http             | 81.8 ms                                                         | 84.1 ms: 1.03x slower                                                         |
| python_startup           | 20.3 ms                                                         | 21.0 ms: 1.03x slower                                                         |
| logging_format           | 6.22 us                                                         | 6.44 us: 1.04x slower                                                         |
| xml_etree_parse          | 90.9 ms                                                         | 94.1 ms: 1.04x slower                                                         |
| logging_simple           | 5.78 us                                                         | 5.99 us: 1.04x slower                                                         |
| asyncio_tcp              | 471 ms                                                          | 489 ms: 1.04x slower                                                          |
| pickle_pure_python       | 175 us                                                          | 183 us: 1.04x slower                                                          |
| chaos                    | 38.4 ms                                                         | 40.3 ms: 1.05x slower                                                         |
| meteor_contest           | 69.9 ms                                                         | 73.6 ms: 1.05x slower                                                         |
| nqueens                  | 56.7 ms                                                         | 60.0 ms: 1.06x slower                                                         |
| json_dumps               | 5.61 ms                                                         | 5.95 ms: 1.06x slower                                                         |
| bench_mp_pool            | 64.8 ms                                                         | 69.3 ms: 1.07x slower                                                         |
| python_startup_no_site   | 16.2 ms                                                         | 17.4 ms: 1.07x slower                                                         |
| xml_etree_process        | 36.4 ms                                                         | 39.3 ms: 1.08x slower                                                         |
| richards                 | 26.7 ms                                                         | 29.0 ms: 1.08x slower                                                         |
| mdp                      | 1.31 sec                                                        | 1.43 sec: 1.09x slower                                                        |
| richards_super           | 30.2 ms                                                         | 32.9 ms: 1.09x slower                                                         |
| logging_silent           | 52.9 ns                                                         | 58.1 ns: 1.10x slower                                                         |
| docutils                 | 1.63 sec                                                        | 1.78 sec: 1.10x slower                                                        |
| coverage                 | 42.1 ms                                                         | 46.6 ms: 1.11x slower                                                         |
| sqlglot_parse            | 748 us                                                          | 830 us: 1.11x slower                                                          |
| sqlglot_transpile        | 955 us                                                          | 1.07 ms: 1.12x slower                                                         |
| html5lib                 | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                                         |
| sqlglot_normalize        | 173 ms                                                          | 194 ms: 1.12x slower                                                          |
| sympy_sum                | 84.4 ms                                                         | 95.0 ms: 1.13x slower                                                         |
| sqlglot_optimize         | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                                         |
| sympy_str                | 159 ms                                                          | 180 ms: 1.13x slower                                                          |
| regex_compile            | 78.0 ms                                                         | 89.4 ms: 1.15x slower                                                         |
| coroutines               | 12.8 ms                                                         | 14.6 ms: 1.15x slower                                                         |
| 2to3                     | 207 ms                                                          | 238 ms: 1.15x slower                                                          |
| raytrace                 | 162 ms                                                          | 187 ms: 1.15x slower                                                          |
| sympy_integrate          | 12.2 ms                                                         | 14.2 ms: 1.16x slower                                                         |
| typing_runtime_protocols | 101 us                                                          | 118 us: 1.16x slower                                                          |
| sympy_expand             | 271 ms                                                          | 316 ms: 1.17x slower                                                          |
| pylint                   | 205 ms                                                          | 239 ms: 1.17x slower                                                          |
| go                       | 82.1 ms                                                         | 97.5 ms: 1.19x slower                                                         |
| async_generators         | 223 ms                                                          | 274 ms: 1.23x slower                                                          |
| scimark_sor              | 75.3 ms                                                         | 93.2 ms: 1.24x slower                                                         |
| hexiom                   | 3.72 ms                                                         | 4.61 ms: 1.24x slower                                                         |
| django_template          | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                         |
| generators               | 19.6 ms                                                         | 24.5 ms: 1.25x slower                                                         |
| deltablue                | 1.88 ms                                                         | 2.36 ms: 1.25x slower                                                         |
| genshi_text              | 14.4 ms                                                         | 18.6 ms: 1.29x slower                                                         |
| scimark_lu               | 56.6 ms                                                         | 73.4 ms: 1.30x slower                                                         |
| genshi_xml               | 31.6 ms                                                         | 43.7 ms: 1.38x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.00x slower                                                                  |

Benchmark hidden because not significant (8): async_tree_memoization_tg, regex_v8, async_tree_memoization, regex_effbot, pathlib, gc_traversal, async_tree_cpu_io_mixed_tg, pycparser
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.26% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown