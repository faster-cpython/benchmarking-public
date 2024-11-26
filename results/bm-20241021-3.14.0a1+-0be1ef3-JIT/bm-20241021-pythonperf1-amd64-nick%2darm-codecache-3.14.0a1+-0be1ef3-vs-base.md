# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: windows-amd64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                      | 240 ms: 1.04x faster                                                 |
| docutils       | 1.89 sec                                                                    | 1.84 sec: 1.03x faster                                               |
| html5lib       | 39.3 ms                                                                     | 38.7 ms: 1.02x faster                                                |
| sphinx         | 769 ms                                                                      | 743 ms: 1.04x faster                                                 |
| tornado_http   | 99.5 ms                                                                     | 98.0 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines       | 15.0 ms                                                                     | 13.9 ms: 1.08x faster                                                |
| async_generators | 268 ms                                                                      | 264 ms: 1.02x faster                                                 |
| Geometric mean   | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 54.3 ms                                                                     | 53.1 ms: 1.02x faster                                                |
| float          | 48.0 ms                                                                     | 47.4 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 91.9 ms                                                                     | 86.7 ms: 1.06x faster                                                |
| regex_v8       | 15.2 ms                                                                     | 15.5 ms: 1.02x slower                                                |
| regex_effbot   | 1.58 ms                                                                     | 1.66 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.29 sec                                                                    | 1.24 sec: 1.04x faster                                               |
| unpickle_pure_python | 147 us                                                                      | 142 us: 1.04x faster                                                 |
| xml_etree_generate   | 51.1 ms                                                                     | 50.2 ms: 1.02x faster                                                |
| xml_etree_process    | 36.4 ms                                                                     | 36.0 ms: 1.01x faster                                                |
| xml_etree_parse      | 94.6 ms                                                                     | 95.5 ms: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (4): pickle_pure_python, json_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 25.1 ms                                                                     | 24.2 ms: 1.04x faster                                                |
| python_startup_no_site | 19.2 ms                                                                     | 18.5 ms: 1.03x faster                                                |
| Geometric mean         | (ref)                                                                       | 1.03x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 46.2 ms                                                                     | 38.0 ms: 1.22x faster                                                |
| genshi_text     | 19.8 ms                                                                     | 17.9 ms: 1.11x faster                                                |
| django_template | 26.4 ms                                                                     | 25.3 ms: 1.04x faster                                                |
| mako            | 4.97 ms                                                                     | 5.08 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                       | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml               | 46.2 ms                                                                     | 38.0 ms: 1.22x faster                                                |
| hexiom                   | 5.17 ms                                                                     | 4.28 ms: 1.21x faster                                                |
| generators               | 24.2 ms                                                                     | 21.6 ms: 1.12x faster                                                |
| go                       | 91.7 ms                                                                     | 82.2 ms: 1.11x faster                                                |
| richards                 | 34.2 ms                                                                     | 30.8 ms: 1.11x faster                                                |
| genshi_text              | 19.8 ms                                                                     | 17.9 ms: 1.11x faster                                                |
| richards_super           | 38.6 ms                                                                     | 35.0 ms: 1.10x faster                                                |
| fannkuch                 | 232 ms                                                                      | 212 ms: 1.09x faster                                                 |
| sympy_expand             | 326 ms                                                                      | 300 ms: 1.09x faster                                                 |
| sqlglot_optimize         | 42.7 ms                                                                     | 39.4 ms: 1.08x faster                                                |
| coroutines               | 15.0 ms                                                                     | 13.9 ms: 1.08x faster                                                |
| sqlglot_normalize        | 210 ms                                                                      | 194 ms: 1.08x faster                                                 |
| deepcopy_memo            | 17.1 us                                                                     | 15.8 us: 1.08x faster                                                |
| sympy_str                | 192 ms                                                                      | 179 ms: 1.07x faster                                                 |
| sqlglot_transpile        | 1.19 ms                                                                     | 1.11 ms: 1.07x faster                                                |
| comprehensions           | 11.6 us                                                                     | 10.9 us: 1.07x faster                                                |
| sqlglot_parse            | 902 us                                                                      | 850 us: 1.06x faster                                                 |
| regex_compile            | 91.9 ms                                                                     | 86.7 ms: 1.06x faster                                                |
| raytrace                 | 212 ms                                                                      | 200 ms: 1.06x faster                                                 |
| meteor_contest           | 76.1 ms                                                                     | 71.9 ms: 1.06x faster                                                |
| sympy_sum                | 103 ms                                                                      | 98.0 ms: 1.05x faster                                                |
| sympy_integrate          | 15.8 ms                                                                     | 15.0 ms: 1.05x faster                                                |
| mdp                      | 1.61 sec                                                                    | 1.53 sec: 1.05x faster                                               |
| chaos                    | 41.5 ms                                                                     | 39.5 ms: 1.05x faster                                                |
| pyflate                  | 288 ms                                                                      | 274 ms: 1.05x faster                                                 |
| logging_silent           | 57.3 ns                                                                     | 54.6 ns: 1.05x faster                                                |
| pycparser                | 730 ms                                                                      | 696 ms: 1.05x faster                                                 |
| pprint_pformat           | 949 ms                                                                      | 906 ms: 1.05x faster                                                 |
| django_template          | 26.4 ms                                                                     | 25.3 ms: 1.04x faster                                                |
| 2to3                     | 250 ms                                                                      | 240 ms: 1.04x faster                                                 |
| deltablue                | 2.32 ms                                                                     | 2.23 ms: 1.04x faster                                                |
| tomli_loads              | 1.29 sec                                                                    | 1.24 sec: 1.04x faster                                               |
| pprint_safe_repr         | 450 ms                                                                      | 433 ms: 1.04x faster                                                 |
| python_startup           | 25.1 ms                                                                     | 24.2 ms: 1.04x faster                                                |
| sphinx                   | 769 ms                                                                      | 743 ms: 1.04x faster                                                 |
| unpickle_pure_python     | 147 us                                                                      | 142 us: 1.04x faster                                                 |
| deepcopy_reduce          | 1.86 us                                                                     | 1.80 us: 1.03x faster                                                |
| python_startup_no_site   | 19.2 ms                                                                     | 18.5 ms: 1.03x faster                                                |
| coverage                 | 49.3 ms                                                                     | 47.8 ms: 1.03x faster                                                |
| logging_format           | 6.63 us                                                                     | 6.44 us: 1.03x faster                                                |
| dulwich_log              | 41.0 ms                                                                     | 39.9 ms: 1.03x faster                                                |
| docutils                 | 1.89 sec                                                                    | 1.84 sec: 1.03x faster                                               |
| deepcopy                 | 187 us                                                                      | 183 us: 1.03x faster                                                 |
| logging_simple           | 6.20 us                                                                     | 6.05 us: 1.03x faster                                                |
| bench_mp_pool            | 91.1 ms                                                                     | 89.1 ms: 1.02x faster                                                |
| nbody                    | 54.3 ms                                                                     | 53.1 ms: 1.02x faster                                                |
| typing_runtime_protocols | 117 us                                                                      | 114 us: 1.02x faster                                                 |
| scimark_monte_carlo      | 36.8 ms                                                                     | 36.1 ms: 1.02x faster                                                |
| thrift                   | 528 us                                                                      | 519 us: 1.02x faster                                                 |
| async_generators         | 268 ms                                                                      | 264 ms: 1.02x faster                                                 |
| xml_etree_generate       | 51.1 ms                                                                     | 50.2 ms: 1.02x faster                                                |
| html5lib                 | 39.3 ms                                                                     | 38.7 ms: 1.02x faster                                                |
| scimark_lu               | 55.0 ms                                                                     | 54.1 ms: 1.02x faster                                                |
| telco                    | 4.64 ms                                                                     | 4.57 ms: 1.02x faster                                                |
| tornado_http             | 99.5 ms                                                                     | 98.0 ms: 1.01x faster                                                |
| create_gc_cycles         | 1.41 ms                                                                     | 1.39 ms: 1.01x faster                                                |
| xml_etree_process        | 36.4 ms                                                                     | 36.0 ms: 1.01x faster                                                |
| float                    | 48.0 ms                                                                     | 47.4 ms: 1.01x faster                                                |
| scimark_sor              | 64.2 ms                                                                     | 63.7 ms: 1.01x faster                                                |
| xml_etree_parse          | 94.6 ms                                                                     | 95.5 ms: 1.01x slower                                                |
| scimark_fft              | 154 ms                                                                      | 157 ms: 1.02x slower                                                 |
| regex_v8                 | 15.2 ms                                                                     | 15.5 ms: 1.02x slower                                                |
| mako                     | 4.97 ms                                                                     | 5.08 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult  | 2.10 ms                                                                     | 2.21 ms: 1.05x slower                                                |
| regex_effbot             | 1.58 ms                                                                     | 1.66 ms: 1.05x slower                                                |
| Geometric mean           | (ref)                                                                       | 1.03x faster                                                         |

Benchmark hidden because not significant (22): pylint, async_tree_memoization, async_tree_memoization_tg, pathlib, async_tree_io_tg, async_tree_cpu_io_mixed_tg, pickle_pure_python, async_tree_none_tg, async_tree_none, gc_traversal, crypto_pyaes, bench_thread_pool, json, spectral_norm, regex_dna, pidigits, json_loads, nqueens, json_dumps, async_tree_io, xml_etree_iterparse, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown