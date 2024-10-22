# Results vs. base

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-amd64
- commit hash: 1b65c46
- commit date: 2024-08-01
- overall geometric mean: 1.00x faster
- HPT reliability: 63.82%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.85 sec                                                                   | 1.83 sec: 1.01x faster                                                               |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators | 261 ms                                                                     | 258 ms: 1.01x faster                                                                 |
| coroutines       | 13.7 ms                                                                    | 13.8 ms: 1.01x slower                                                                |
| async_tree_io    | 545 ms                                                                     | 561 ms: 1.03x slower                                                                 |
| Geometric mean   | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (9): asyncio_tcp, asyncio_tcp_ssl, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 51.5 ms                                                                    | 49.7 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                                    | 14.4 ms: 1.02x faster                                                                |
| regex_dna      | 118 ms                                                                     | 116 ms: 1.02x faster                                                                 |
| regex_effbot   | 1.59 ms                                                                    | 1.56 ms: 1.02x faster                                                                |
| regex_compile  | 91.7 ms                                                                    | 90.5 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.6 us                                                                    | 14.1 us: 1.03x faster                                                                |
| xml_etree_iterparse  | 62.2 ms                                                                    | 61.2 ms: 1.02x faster                                                                |
| xml_etree_generate   | 52.3 ms                                                                    | 51.4 ms: 1.02x faster                                                                |
| unpickle_pure_python | 137 us                                                                     | 135 us: 1.02x faster                                                                 |
| xml_etree_process    | 37.8 ms                                                                    | 37.3 ms: 1.01x faster                                                                |
| tomli_loads          | 1.26 sec                                                                   | 1.28 sec: 1.01x slower                                                               |
| json_dumps           | 5.99 ms                                                                    | 6.10 ms: 1.02x slower                                                                |
| pickle_pure_python   | 184 us                                                                     | 187 us: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                                    | 22.7 ms: 1.03x slower                                                                |
| python_startup_no_site | 17.8 ms                                                                    | 18.7 ms: 1.05x slower                                                                |
| Geometric mean         | (ref)                                                                      | 1.04x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 40.9 ms                                                                    | 38.6 ms: 1.06x faster                                                                |
| genshi_text     | 18.7 ms                                                                    | 17.8 ms: 1.05x faster                                                                |
| django_template | 25.9 ms                                                                    | 25.6 ms: 1.01x faster                                                                |
| mako            | 4.97 ms                                                                    | 5.10 ms: 1.03x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pycparser                | 786 ms                                                                     | 695 ms: 1.13x faster                                                                 |
| genshi_xml               | 40.9 ms                                                                    | 38.6 ms: 1.06x faster                                                                |
| genshi_text              | 18.7 ms                                                                    | 17.8 ms: 1.05x faster                                                                |
| scimark_lu               | 75.2 ms                                                                    | 71.5 ms: 1.05x faster                                                                |
| nbody                    | 51.5 ms                                                                    | 49.7 ms: 1.04x faster                                                                |
| generators               | 23.0 ms                                                                    | 22.2 ms: 1.03x faster                                                                |
| json_loads               | 14.6 us                                                                    | 14.1 us: 1.03x faster                                                                |
| thrift                   | 533 us                                                                     | 519 us: 1.03x faster                                                                 |
| regex_v8                 | 14.7 ms                                                                    | 14.4 ms: 1.02x faster                                                                |
| pprint_pformat           | 995 ms                                                                     | 973 ms: 1.02x faster                                                                 |
| logging_silent           | 58.7 ns                                                                    | 57.3 ns: 1.02x faster                                                                |
| regex_dna                | 118 ms                                                                     | 116 ms: 1.02x faster                                                                 |
| regex_effbot             | 1.59 ms                                                                    | 1.56 ms: 1.02x faster                                                                |
| xml_etree_iterparse      | 62.2 ms                                                                    | 61.2 ms: 1.02x faster                                                                |
| xml_etree_generate       | 52.3 ms                                                                    | 51.4 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult  | 2.07 ms                                                                    | 2.04 ms: 1.02x faster                                                                |
| unpickle_pure_python     | 137 us                                                                     | 135 us: 1.02x faster                                                                 |
| coverage                 | 47.7 ms                                                                    | 47.0 ms: 1.02x faster                                                                |
| pprint_safe_repr         | 484 ms                                                                     | 477 ms: 1.01x faster                                                                 |
| typing_runtime_protocols | 118 us                                                                     | 116 us: 1.01x faster                                                                 |
| xml_etree_process        | 37.8 ms                                                                    | 37.3 ms: 1.01x faster                                                                |
| hexiom                   | 4.83 ms                                                                    | 4.77 ms: 1.01x faster                                                                |
| regex_compile            | 91.7 ms                                                                    | 90.5 ms: 1.01x faster                                                                |
| logging_format           | 6.53 us                                                                    | 6.45 us: 1.01x faster                                                                |
| django_template          | 25.9 ms                                                                    | 25.6 ms: 1.01x faster                                                                |
| async_generators         | 261 ms                                                                     | 258 ms: 1.01x faster                                                                 |
| sqlglot_parse            | 844 us                                                                     | 837 us: 1.01x faster                                                                 |
| docutils                 | 1.85 sec                                                                   | 1.83 sec: 1.01x faster                                                               |
| scimark_sor              | 92.7 ms                                                                    | 92.0 ms: 1.01x faster                                                                |
| gc_traversal             | 1.58 ms                                                                    | 1.56 ms: 1.01x faster                                                                |
| richards                 | 31.5 ms                                                                    | 31.3 ms: 1.01x faster                                                                |
| sympy_expand             | 330 ms                                                                     | 329 ms: 1.00x faster                                                                 |
| meteor_contest           | 70.7 ms                                                                    | 71.1 ms: 1.00x slower                                                                |
| deltablue                | 2.35 ms                                                                    | 2.37 ms: 1.01x slower                                                                |
| sqlglot_optimize         | 36.8 ms                                                                    | 37.0 ms: 1.01x slower                                                                |
| go                       | 101 ms                                                                     | 101 ms: 1.01x slower                                                                 |
| coroutines               | 13.7 ms                                                                    | 13.8 ms: 1.01x slower                                                                |
| comprehensions           | 10.3 us                                                                    | 10.4 us: 1.01x slower                                                                |
| tomli_loads              | 1.26 sec                                                                   | 1.28 sec: 1.01x slower                                                               |
| sympy_integrate          | 14.7 ms                                                                    | 14.9 ms: 1.01x slower                                                                |
| deepcopy                 | 185 us                                                                     | 187 us: 1.01x slower                                                                 |
| chaos                    | 39.4 ms                                                                    | 39.9 ms: 1.01x slower                                                                |
| sqlglot_normalize        | 192 ms                                                                     | 195 ms: 1.01x slower                                                                 |
| raytrace                 | 192 ms                                                                     | 195 ms: 1.01x slower                                                                 |
| deepcopy_reduce          | 1.82 us                                                                    | 1.85 us: 1.02x slower                                                                |
| sympy_sum                | 96.3 ms                                                                    | 98.0 ms: 1.02x slower                                                                |
| json_dumps               | 5.99 ms                                                                    | 6.10 ms: 1.02x slower                                                                |
| fannkuch                 | 215 ms                                                                     | 219 ms: 1.02x slower                                                                 |
| pickle_pure_python       | 184 us                                                                     | 187 us: 1.02x slower                                                                 |
| nqueens                  | 62.3 ms                                                                    | 63.5 ms: 1.02x slower                                                                |
| pyflate                  | 247 ms                                                                     | 253 ms: 1.03x slower                                                                 |
| mako                     | 4.97 ms                                                                    | 5.10 ms: 1.03x slower                                                                |
| async_tree_io            | 545 ms                                                                     | 561 ms: 1.03x slower                                                                 |
| python_startup           | 22.0 ms                                                                    | 22.7 ms: 1.03x slower                                                                |
| crypto_pyaes             | 39.4 ms                                                                    | 40.8 ms: 1.03x slower                                                                |
| python_startup_no_site   | 17.8 ms                                                                    | 18.7 ms: 1.05x slower                                                                |
| bench_mp_pool            | 73.0 ms                                                                    | 76.7 ms: 1.05x slower                                                                |
| mdp                      | 1.45 sec                                                                   | 1.55 sec: 1.07x slower                                                               |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (30): asyncio_tcp, bench_thread_pool, json, telco, create_gc_cycles, logging_simple, float, pidigits, spectral_norm, asyncio_tcp_ssl, pylint, async_tree_none_tg, html5lib, scimark_fft, async_tree_memoization_tg, richards_super, deepcopy_memo, 2to3, pathlib, sympy_str, dulwich_log, sqlglot_transpile, async_tree_cpu_io_mixed_tg, xml_etree_parse, scimark_monte_carlo, tornado_http, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

# HPT report

- Reliability score: 63.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown