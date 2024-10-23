# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: windows-amd64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 246 ms                                                                      | 240 ms: 1.03x faster                                                 |
| docutils       | 1.91 sec                                                                    | 1.84 sec: 1.04x faster                                               |
| html5lib       | 39.5 ms                                                                     | 38.7 ms: 1.02x faster                                                |
| sphinx         | 766 ms                                                                      | 743 ms: 1.03x faster                                                 |
| tornado_http   | 96.2 ms                                                                     | 98.0 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_generators | 258 ms                                                                      | 264 ms: 1.02x slower                                                 |
| Geometric mean   | (ref)                                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, coroutines, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 91.1 ms                                                                     | 86.7 ms: 1.05x faster                                                |
| regex_dna      | 123 ms                                                                      | 122 ms: 1.01x faster                                                 |
| regex_v8       | 15.1 ms                                                                     | 15.5 ms: 1.03x slower                                                |
| regex_effbot   | 1.59 ms                                                                     | 1.66 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|---------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads         | 1.26 sec                                                                    | 1.24 sec: 1.02x faster                                               |
| xml_etree_parse     | 93.1 ms                                                                     | 95.5 ms: 1.03x slower                                                |
| xml_etree_iterparse | 61.6 ms                                                                     | 63.7 ms: 1.03x slower                                                |
| Geometric mean      | (ref)                                                                       | 1.00x slower                                                         |

Benchmark hidden because not significant (6): json_dumps, json_loads, xml_etree_process, unpickle_pure_python, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 18.8 ms                                                                     | 18.5 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 44.1 ms                                                                     | 38.0 ms: 1.16x faster                                                |
| django_template | 27.6 ms                                                                     | 25.3 ms: 1.09x faster                                                |
| genshi_text     | 18.9 ms                                                                     | 17.9 ms: 1.06x faster                                                |
| mako            | 4.99 ms                                                                     | 5.08 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                       | 1.07x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| hexiom                   | 5.13 ms                                                                     | 4.28 ms: 1.20x faster                                                |
| genshi_xml               | 44.1 ms                                                                     | 38.0 ms: 1.16x faster                                                |
| richards                 | 34.0 ms                                                                     | 30.8 ms: 1.10x faster                                                |
| go                       | 90.4 ms                                                                     | 82.2 ms: 1.10x faster                                                |
| fannkuch                 | 232 ms                                                                      | 212 ms: 1.10x faster                                                 |
| richards_super           | 38.3 ms                                                                     | 35.0 ms: 1.09x faster                                                |
| django_template          | 27.6 ms                                                                     | 25.3 ms: 1.09x faster                                                |
| sqlglot_optimize         | 42.6 ms                                                                     | 39.4 ms: 1.08x faster                                                |
| sympy_expand             | 323 ms                                                                      | 300 ms: 1.08x faster                                                 |
| sympy_str                | 192 ms                                                                      | 179 ms: 1.07x faster                                                 |
| sqlglot_normalize        | 206 ms                                                                      | 194 ms: 1.07x faster                                                 |
| comprehensions           | 11.6 us                                                                     | 10.9 us: 1.06x faster                                                |
| sqlglot_transpile        | 1.17 ms                                                                     | 1.11 ms: 1.06x faster                                                |
| genshi_text              | 18.9 ms                                                                     | 17.9 ms: 1.06x faster                                                |
| raytrace                 | 212 ms                                                                      | 200 ms: 1.06x faster                                                 |
| coverage                 | 50.3 ms                                                                     | 47.8 ms: 1.05x faster                                                |
| pprint_pformat           | 953 ms                                                                      | 906 ms: 1.05x faster                                                 |
| regex_compile            | 91.1 ms                                                                     | 86.7 ms: 1.05x faster                                                |
| generators               | 22.7 ms                                                                     | 21.6 ms: 1.05x faster                                                |
| sqlglot_parse            | 893 us                                                                      | 850 us: 1.05x faster                                                 |
| deepcopy_memo            | 16.6 us                                                                     | 15.8 us: 1.05x faster                                                |
| json                     | 3.09 ms                                                                     | 2.94 ms: 1.05x faster                                                |
| meteor_contest           | 75.4 ms                                                                     | 71.9 ms: 1.05x faster                                                |
| sympy_integrate          | 15.7 ms                                                                     | 15.0 ms: 1.05x faster                                                |
| sympy_sum                | 102 ms                                                                      | 98.0 ms: 1.04x faster                                                |
| chaos                    | 41.2 ms                                                                     | 39.5 ms: 1.04x faster                                                |
| pyflate                  | 285 ms                                                                      | 274 ms: 1.04x faster                                                 |
| pycparser                | 725 ms                                                                      | 696 ms: 1.04x faster                                                 |
| pprint_safe_repr         | 450 ms                                                                      | 433 ms: 1.04x faster                                                 |
| deepcopy                 | 190 us                                                                      | 183 us: 1.04x faster                                                 |
| docutils                 | 1.91 sec                                                                    | 1.84 sec: 1.04x faster                                               |
| deltablue                | 2.31 ms                                                                     | 2.23 ms: 1.03x faster                                                |
| logging_silent           | 56.3 ns                                                                     | 54.6 ns: 1.03x faster                                                |
| sphinx                   | 766 ms                                                                      | 743 ms: 1.03x faster                                                 |
| dulwich_log              | 41.0 ms                                                                     | 39.9 ms: 1.03x faster                                                |
| deepcopy_reduce          | 1.85 us                                                                     | 1.80 us: 1.03x faster                                                |
| 2to3                     | 246 ms                                                                      | 240 ms: 1.03x faster                                                 |
| html5lib                 | 39.5 ms                                                                     | 38.7 ms: 1.02x faster                                                |
| crypto_pyaes             | 40.6 ms                                                                     | 39.9 ms: 1.02x faster                                                |
| scimark_monte_carlo      | 36.8 ms                                                                     | 36.1 ms: 1.02x faster                                                |
| tomli_loads              | 1.26 sec                                                                    | 1.24 sec: 1.02x faster                                               |
| logging_simple           | 6.15 us                                                                     | 6.05 us: 1.02x faster                                                |
| scimark_fft              | 159 ms                                                                      | 157 ms: 1.02x faster                                                 |
| python_startup_no_site   | 18.8 ms                                                                     | 18.5 ms: 1.01x faster                                                |
| gc_traversal             | 1.96 ms                                                                     | 1.94 ms: 1.01x faster                                                |
| scimark_sor              | 64.3 ms                                                                     | 63.7 ms: 1.01x faster                                                |
| logging_format           | 6.49 us                                                                     | 6.44 us: 1.01x faster                                                |
| mdp                      | 1.54 sec                                                                    | 1.53 sec: 1.01x faster                                               |
| regex_dna                | 123 ms                                                                      | 122 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult  | 2.19 ms                                                                     | 2.21 ms: 1.01x slower                                                |
| nqueens                  | 61.9 ms                                                                     | 62.7 ms: 1.01x slower                                                |
| scimark_lu               | 53.3 ms                                                                     | 54.1 ms: 1.02x slower                                                |
| tornado_http             | 96.2 ms                                                                     | 98.0 ms: 1.02x slower                                                |
| mako                     | 4.99 ms                                                                     | 5.08 ms: 1.02x slower                                                |
| async_generators         | 258 ms                                                                      | 264 ms: 1.02x slower                                                 |
| xml_etree_parse          | 93.1 ms                                                                     | 95.5 ms: 1.03x slower                                                |
| regex_v8                 | 15.1 ms                                                                     | 15.5 ms: 1.03x slower                                                |
| spectral_norm            | 54.0 ms                                                                     | 55.7 ms: 1.03x slower                                                |
| typing_runtime_protocols | 111 us                                                                      | 114 us: 1.03x slower                                                 |
| xml_etree_iterparse      | 61.6 ms                                                                     | 63.7 ms: 1.03x slower                                                |
| regex_effbot             | 1.59 ms                                                                     | 1.66 ms: 1.05x slower                                                |
| Geometric mean           | (ref)                                                                       | 1.02x faster                                                         |

Benchmark hidden because not significant (26): pylint, thrift, async_tree_io_tg, create_gc_cycles, json_dumps, async_tree_cpu_io_mixed_tg, json_loads, xml_etree_process, unpickle_pure_python, float, xml_etree_generate, pickle_pure_python, pathlib, bench_mp_pool, python_startup, pidigits, async_tree_none_tg, coroutines, telco, async_tree_none, async_tree_memoization_tg, nbody, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, bench_thread_pool

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown