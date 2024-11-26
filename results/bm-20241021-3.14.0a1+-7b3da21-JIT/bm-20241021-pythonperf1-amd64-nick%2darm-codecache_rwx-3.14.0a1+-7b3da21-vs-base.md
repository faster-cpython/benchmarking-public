# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-amd64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                      | 234 ms: 1.07x faster                                                     |
| docutils       | 1.89 sec                                                                    | 1.81 sec: 1.04x faster                                                   |
| html5lib       | 39.3 ms                                                                     | 38.8 ms: 1.01x faster                                                    |
| sphinx         | 769 ms                                                                      | 709 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines     | 15.0 ms                                                                     | 13.9 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (9): async_generators, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 54.3 ms                                                                     | 53.1 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 91.9 ms                                                                     | 82.6 ms: 1.11x faster                                                    |
| regex_dna      | 122 ms                                                                      | 116 ms: 1.05x faster                                                     |
| regex_v8       | 15.2 ms                                                                     | 15.0 ms: 1.01x faster                                                    |
| regex_effbot   | 1.58 ms                                                                     | 1.60 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 147 us                                                                      | 141 us: 1.05x faster                                                     |
| xml_etree_process    | 36.4 ms                                                                     | 35.3 ms: 1.03x faster                                                    |
| tomli_loads          | 1.29 sec                                                                    | 1.27 sec: 1.01x faster                                                   |
| xml_etree_generate   | 51.1 ms                                                                     | 50.5 ms: 1.01x faster                                                    |
| pickle_pure_python   | 199 us                                                                      | 197 us: 1.01x faster                                                     |
| xml_etree_parse      | 94.6 ms                                                                     | 94.0 ms: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (3): json_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 19.2 ms                                                                     | 18.2 ms: 1.05x faster                                                    |
| python_startup         | 25.1 ms                                                                     | 24.2 ms: 1.04x faster                                                    |
| Geometric mean         | (ref)                                                                       | 1.05x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 46.2 ms                                                                     | 40.3 ms: 1.15x faster                                                    |
| genshi_text    | 19.8 ms                                                                     | 18.5 ms: 1.07x faster                                                    |
| mako           | 4.97 ms                                                                     | 5.09 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| hexiom                   | 5.17 ms                                                                     | 4.25 ms: 1.22x faster                                                    |
| genshi_xml               | 46.2 ms                                                                     | 40.3 ms: 1.15x faster                                                    |
| generators               | 24.2 ms                                                                     | 21.2 ms: 1.14x faster                                                    |
| regex_compile            | 91.9 ms                                                                     | 82.6 ms: 1.11x faster                                                    |
| go                       | 91.7 ms                                                                     | 82.4 ms: 1.11x faster                                                    |
| sqlglot_optimize         | 42.7 ms                                                                     | 38.8 ms: 1.10x faster                                                    |
| pylint                   | 281 ms                                                                      | 258 ms: 1.09x faster                                                     |
| fannkuch                 | 232 ms                                                                      | 213 ms: 1.09x faster                                                     |
| mdp                      | 1.61 sec                                                                    | 1.48 sec: 1.09x faster                                                   |
| meteor_contest           | 76.1 ms                                                                     | 70.0 ms: 1.09x faster                                                    |
| sphinx                   | 769 ms                                                                      | 709 ms: 1.08x faster                                                     |
| coroutines               | 15.0 ms                                                                     | 13.9 ms: 1.08x faster                                                    |
| sympy_sum                | 103 ms                                                                      | 95.5 ms: 1.08x faster                                                    |
| genshi_text              | 19.8 ms                                                                     | 18.5 ms: 1.07x faster                                                    |
| 2to3                     | 250 ms                                                                      | 234 ms: 1.07x faster                                                     |
| richards                 | 34.2 ms                                                                     | 32.0 ms: 1.07x faster                                                    |
| sympy_integrate          | 15.8 ms                                                                     | 14.8 ms: 1.07x faster                                                    |
| richards_super           | 38.6 ms                                                                     | 36.2 ms: 1.07x faster                                                    |
| sympy_str                | 192 ms                                                                      | 180 ms: 1.06x faster                                                     |
| comprehensions           | 11.6 us                                                                     | 10.9 us: 1.06x faster                                                    |
| sqlglot_transpile        | 1.19 ms                                                                     | 1.12 ms: 1.06x faster                                                    |
| sympy_expand             | 326 ms                                                                      | 308 ms: 1.06x faster                                                     |
| deepcopy_memo            | 17.1 us                                                                     | 16.2 us: 1.06x faster                                                    |
| pprint_pformat           | 949 ms                                                                      | 900 ms: 1.05x faster                                                     |
| python_startup_no_site   | 19.2 ms                                                                     | 18.2 ms: 1.05x faster                                                    |
| sqlglot_parse            | 902 us                                                                      | 858 us: 1.05x faster                                                     |
| regex_dna                | 122 ms                                                                      | 116 ms: 1.05x faster                                                     |
| logging_silent           | 57.3 ns                                                                     | 54.5 ns: 1.05x faster                                                    |
| chaos                    | 41.5 ms                                                                     | 39.7 ms: 1.05x faster                                                    |
| spectral_norm            | 55.6 ms                                                                     | 53.2 ms: 1.05x faster                                                    |
| unpickle_pure_python     | 147 us                                                                      | 141 us: 1.05x faster                                                     |
| bench_mp_pool            | 91.1 ms                                                                     | 87.2 ms: 1.05x faster                                                    |
| docutils                 | 1.89 sec                                                                    | 1.81 sec: 1.04x faster                                                   |
| pyflate                  | 288 ms                                                                      | 276 ms: 1.04x faster                                                     |
| sqlglot_normalize        | 210 ms                                                                      | 202 ms: 1.04x faster                                                     |
| python_startup           | 25.1 ms                                                                     | 24.2 ms: 1.04x faster                                                    |
| pycparser                | 730 ms                                                                      | 707 ms: 1.03x faster                                                     |
| scimark_lu               | 55.0 ms                                                                     | 53.3 ms: 1.03x faster                                                    |
| xml_etree_process        | 36.4 ms                                                                     | 35.3 ms: 1.03x faster                                                    |
| raytrace                 | 212 ms                                                                      | 206 ms: 1.03x faster                                                     |
| scimark_monte_carlo      | 36.8 ms                                                                     | 35.8 ms: 1.03x faster                                                    |
| telco                    | 4.64 ms                                                                     | 4.51 ms: 1.03x faster                                                    |
| nbody                    | 54.3 ms                                                                     | 53.1 ms: 1.02x faster                                                    |
| logging_simple           | 6.20 us                                                                     | 6.08 us: 1.02x faster                                                    |
| deltablue                | 2.32 ms                                                                     | 2.27 ms: 1.02x faster                                                    |
| pprint_safe_repr         | 450 ms                                                                      | 442 ms: 1.02x faster                                                     |
| dulwich_log              | 41.0 ms                                                                     | 40.3 ms: 1.02x faster                                                    |
| scimark_sor              | 64.2 ms                                                                     | 63.1 ms: 1.02x faster                                                    |
| typing_runtime_protocols | 117 us                                                                      | 115 us: 1.01x faster                                                     |
| html5lib                 | 39.3 ms                                                                     | 38.8 ms: 1.01x faster                                                    |
| tomli_loads              | 1.29 sec                                                                    | 1.27 sec: 1.01x faster                                                   |
| xml_etree_generate       | 51.1 ms                                                                     | 50.5 ms: 1.01x faster                                                    |
| pickle_pure_python       | 199 us                                                                      | 197 us: 1.01x faster                                                     |
| regex_v8                 | 15.2 ms                                                                     | 15.0 ms: 1.01x faster                                                    |
| logging_format           | 6.63 us                                                                     | 6.58 us: 1.01x faster                                                    |
| xml_etree_parse          | 94.6 ms                                                                     | 94.0 ms: 1.01x faster                                                    |
| scimark_fft              | 154 ms                                                                      | 156 ms: 1.01x slower                                                     |
| regex_effbot             | 1.58 ms                                                                     | 1.60 ms: 1.01x slower                                                    |
| mako                     | 4.97 ms                                                                     | 5.09 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 2.10 ms                                                                     | 2.24 ms: 1.07x slower                                                    |
| Geometric mean           | (ref)                                                                       | 1.03x faster                                                             |

Benchmark hidden because not significant (27): bench_thread_pool, tornado_http, json_loads, json_dumps, deepcopy_reduce, deepcopy, crypto_pyaes, async_generators, async_tree_io_tg, pidigits, async_tree_none_tg, create_gc_cycles, async_tree_cpu_io_mixed_tg, float, xml_etree_iterparse, json, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, coverage, nqueens, gc_traversal, async_tree_memoization_tg, pathlib, thrift, async_tree_memoization, django_template

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown