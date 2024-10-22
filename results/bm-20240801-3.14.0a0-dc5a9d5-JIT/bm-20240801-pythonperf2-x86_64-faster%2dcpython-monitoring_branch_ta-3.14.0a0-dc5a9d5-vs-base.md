# Results vs. base

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 98.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                      | 306 ms: 1.01x faster                                                                  |
| docutils       | 3.15 sec                                                                    | 3.12 sec: 1.01x faster                                                                |
| html5lib       | 71.6 ms                                                                     | 70.5 ms: 1.02x faster                                                                 |
| tornado_http   | 121 ms                                                                      | 119 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| coroutines       | 22.0 ms                                                                     | 21.1 ms: 1.04x faster                                                                 |
| async_generators | 385 ms                                                                      | 372 ms: 1.04x faster                                                                  |
| Geometric mean   | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (11): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, asyncio_tcp_ssl, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                                      | 251 ms: 1.00x slower                                                                  |
| float          | 75.0 ms                                                                     | 76.1 ms: 1.01x slower                                                                 |
| nbody          | 84.8 ms                                                                     | 91.2 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                      | 133 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.52 ms                                                                     | 3.50 ms: 1.01x faster                                                                 |
| regex_dna      | 236 ms                                                                      | 235 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|---------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads          | 25.5 us                                                                     | 25.3 us: 1.01x faster                                                                 |
| xml_etree_iterparse | 97.1 ms                                                                     | 97.7 ms: 1.01x slower                                                                 |
| xml_etree_generate  | 81.4 ms                                                                     | 82.3 ms: 1.01x slower                                                                 |
| xml_etree_process   | 56.8 ms                                                                     | 57.6 ms: 1.01x slower                                                                 |
| Geometric mean      | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (5): unpickle_pure_python, tomli_loads, pickle_pure_python, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 28.5 ms                                                                     | 26.3 ms: 1.08x faster                                                                 |
| genshi_xml      | 61.7 ms                                                                     | 60.1 ms: 1.03x faster                                                                 |
| django_template | 41.9 ms                                                                     | 41.2 ms: 1.02x faster                                                                 |
| mako            | 9.03 ms                                                                     | 9.05 ms: 1.00x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.03x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240801-pythonperf2-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text              | 28.5 ms                                                                     | 26.3 ms: 1.08x faster                                                                 |
| typing_runtime_protocols | 194 us                                                                      | 184 us: 1.05x faster                                                                  |
| coroutines               | 22.0 ms                                                                     | 21.1 ms: 1.04x faster                                                                 |
| telco                    | 8.11 ms                                                                     | 7.82 ms: 1.04x faster                                                                 |
| richards_super           | 54.7 ms                                                                     | 52.8 ms: 1.04x faster                                                                 |
| async_generators         | 385 ms                                                                      | 372 ms: 1.04x faster                                                                  |
| richards                 | 46.8 ms                                                                     | 45.2 ms: 1.04x faster                                                                 |
| logging_simple           | 6.44 us                                                                     | 6.23 us: 1.03x faster                                                                 |
| scimark_lu               | 113 ms                                                                      | 110 ms: 1.03x faster                                                                  |
| genshi_xml               | 61.7 ms                                                                     | 60.1 ms: 1.03x faster                                                                 |
| logging_format           | 7.07 us                                                                     | 6.88 us: 1.03x faster                                                                 |
| scimark_monte_carlo      | 66.4 ms                                                                     | 64.7 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult  | 3.94 ms                                                                     | 3.85 ms: 1.02x faster                                                                 |
| fannkuch                 | 353 ms                                                                      | 345 ms: 1.02x faster                                                                  |
| comprehensions           | 18.8 us                                                                     | 18.4 us: 1.02x faster                                                                 |
| sqlglot_parse            | 1.46 ms                                                                     | 1.43 ms: 1.02x faster                                                                 |
| go                       | 168 ms                                                                      | 165 ms: 1.02x faster                                                                  |
| deepcopy                 | 312 us                                                                      | 306 us: 1.02x faster                                                                  |
| django_template          | 41.9 ms                                                                     | 41.2 ms: 1.02x faster                                                                 |
| regex_compile            | 135 ms                                                                      | 133 ms: 1.02x faster                                                                  |
| html5lib                 | 71.6 ms                                                                     | 70.5 ms: 1.02x faster                                                                 |
| tornado_http             | 121 ms                                                                      | 119 ms: 1.02x faster                                                                  |
| deepcopy_memo            | 29.9 us                                                                     | 29.5 us: 1.01x faster                                                                 |
| sqlglot_transpile        | 1.88 ms                                                                     | 1.86 ms: 1.01x faster                                                                 |
| dask                     | 395 ms                                                                      | 391 ms: 1.01x faster                                                                  |
| sympy_expand             | 537 ms                                                                      | 531 ms: 1.01x faster                                                                  |
| sqlglot_optimize         | 63.3 ms                                                                     | 62.6 ms: 1.01x faster                                                                 |
| docutils                 | 3.15 sec                                                                    | 3.12 sec: 1.01x faster                                                                |
| json                     | 5.49 ms                                                                     | 5.43 ms: 1.01x faster                                                                 |
| deepcopy_reduce          | 3.03 us                                                                     | 3.00 us: 1.01x faster                                                                 |
| sympy_str                | 315 ms                                                                      | 312 ms: 1.01x faster                                                                  |
| chaos                    | 67.0 ms                                                                     | 66.5 ms: 1.01x faster                                                                 |
| pycparser                | 1.29 sec                                                                    | 1.28 sec: 1.01x faster                                                                |
| coverage                 | 80.1 ms                                                                     | 79.5 ms: 1.01x faster                                                                 |
| spectral_norm            | 81.9 ms                                                                     | 81.4 ms: 1.01x faster                                                                 |
| crypto_pyaes             | 70.9 ms                                                                     | 70.5 ms: 1.01x faster                                                                 |
| regex_effbot             | 3.52 ms                                                                     | 3.50 ms: 1.01x faster                                                                 |
| sqlglot_normalize        | 129 ms                                                                      | 129 ms: 1.01x faster                                                                  |
| json_loads               | 25.5 us                                                                     | 25.3 us: 1.01x faster                                                                 |
| regex_dna                | 236 ms                                                                      | 235 ms: 1.01x faster                                                                  |
| 2to3                     | 308 ms                                                                      | 306 ms: 1.01x faster                                                                  |
| sympy_integrate          | 26.1 ms                                                                     | 26.0 ms: 1.00x faster                                                                 |
| pidigits                 | 251 ms                                                                      | 251 ms: 1.00x slower                                                                  |
| mako                     | 9.03 ms                                                                     | 9.05 ms: 1.00x slower                                                                 |
| python_startup           | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                                                 |
| meteor_contest           | 127 ms                                                                      | 128 ms: 1.01x slower                                                                  |
| xml_etree_iterparse      | 97.1 ms                                                                     | 97.7 ms: 1.01x slower                                                                 |
| pyflate                  | 440 ms                                                                      | 442 ms: 1.01x slower                                                                  |
| mdp                      | 2.58 sec                                                                    | 2.60 sec: 1.01x slower                                                                |
| xml_etree_generate       | 81.4 ms                                                                     | 82.3 ms: 1.01x slower                                                                 |
| float                    | 75.0 ms                                                                     | 76.1 ms: 1.01x slower                                                                 |
| xml_etree_process        | 56.8 ms                                                                     | 57.6 ms: 1.01x slower                                                                 |
| bpe_tokeniser            | 4.82 sec                                                                    | 4.89 sec: 1.02x slower                                                                |
| scimark_fft              | 279 ms                                                                      | 284 ms: 1.02x slower                                                                  |
| gc_traversal             | 4.39 ms                                                                     | 4.47 ms: 1.02x slower                                                                 |
| pprint_pformat           | 1.67 sec                                                                    | 1.70 sec: 1.02x slower                                                                |
| pathlib                  | 16.4 ms                                                                     | 16.7 ms: 1.02x slower                                                                 |
| raytrace                 | 290 ms                                                                      | 297 ms: 1.02x slower                                                                  |
| scimark_sor              | 123 ms                                                                      | 127 ms: 1.03x slower                                                                  |
| generators               | 35.5 ms                                                                     | 36.9 ms: 1.04x slower                                                                 |
| logging_silent           | 99.0 ns                                                                     | 104 ns: 1.05x slower                                                                  |
| nbody                    | 84.8 ms                                                                     | 91.2 ms: 1.07x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (28): async_tree_io, bench_mp_pool, async_tree_cpu_io_mixed_tg, pylint, async_tree_io_tg, unpickle_pure_python, thrift, tomli_loads, asyncio_tcp, deltablue, hexiom, nqueens, create_gc_cycles, async_tree_cpu_io_mixed, async_tree_none_tg, regex_v8, async_tree_memoization_tg, python_startup_no_site, pickle_pure_python, json_dumps, async_tree_memoization, asyncio_tcp_ssl, xml_etree_parse, async_tree_none, sympy_sum, bench_thread_pool, pprint_safe_repr, asyncio_websockets

# HPT report

- Reliability score: 98.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x