# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-amd64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.194x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 250 ms: 1.02x slower                                                        |
| docutils       | 1.92 sec                                                    | 1.89 sec: 1.01x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| tornado_http   | 108 ms                                                      | 99.5 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 218 ms: 1.99x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 564 ms: 1.97x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 281 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 54.3 ms: 1.31x faster                                                       |
| float          | 61.7 ms                                                     | 48.0 ms: 1.29x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.9 ms: 1.15x faster                                                       |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 199 us: 1.35x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.24x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.97 ms: 1.82x faster                                                       |
| django_template | 28.9 ms                                                     | 26.4 ms: 1.09x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 117 us: 2.87x faster                                                        |
| async_tree_none          | 435 ms                                                      | 218 ms: 1.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 564 ms: 1.97x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 281 ms: 1.87x faster                                                        |
| mako                     | 9.03 ms                                                     | 4.97 ms: 1.82x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.32 ms: 1.81x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.1 us: 1.68x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                                        |
| scimark_sor              | 106 ms                                                      | 64.2 ms: 1.65x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.0 ms: 1.56x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.8 ms: 1.56x faster                                                       |
| go                       | 139 ms                                                      | 91.7 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                       |
| pyflate                  | 409 ms                                                      | 288 ms: 1.42x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 55.6 ms: 1.39x faster                                                       |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                        |
| richards_super           | 52.2 ms                                                     | 38.6 ms: 1.35x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 199 us: 1.35x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 902 us: 1.35x faster                                                        |
| generators               | 32.4 ms                                                     | 24.2 ms: 1.34x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 450 ms: 1.32x faster                                                        |
| nbody                    | 71.3 ms                                                     | 54.3 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.10 ms: 1.30x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                      |
| raytrace                 | 273 ms                                                      | 212 ms: 1.29x faster                                                        |
| float                    | 61.7 ms                                                     | 48.0 ms: 1.29x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 949 ms: 1.28x faster                                                        |
| pycparser                | 930 ms                                                      | 730 ms: 1.27x faster                                                        |
| pylint                   | 350 ms                                                      | 281 ms: 1.25x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.24x faster                                                        |
| richards                 | 42.4 ms                                                     | 34.2 ms: 1.24x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.19 ms: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.22x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 528 us: 1.17x faster                                                        |
| regex_compile            | 106 ms                                                      | 91.9 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 847 us: 1.13x faster                                                        |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.17 ms: 1.11x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.61 sec: 1.11x faster                                                      |
| fannkuch                 | 256 ms                                                      | 232 ms: 1.10x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.4 ms: 1.09x faster                                                       |
| tornado_http             | 108 ms                                                      | 99.5 ms: 1.09x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.5 ms: 1.07x faster                                                       |
| coroutines               | 16.0 ms                                                     | 15.0 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| sympy_sum                | 107 ms                                                      | 103 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.63 us: 1.02x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                       |
| sympy_str                | 194 ms                                                      | 192 ms: 1.01x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.89 sec: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| 2to3                     | 246 ms                                                      | 250 ms: 1.02x slower                                                        |
| sqlglot_normalize        | 205 ms                                                      | 210 ms: 1.02x slower                                                        |
| sympy_integrate          | 15.3 ms                                                     | 15.8 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| sympy_expand             | 314 ms                                                      | 326 ms: 1.04x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 80.7 ms: 1.07x slower                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 42.7 ms: 1.07x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                       |
| async_generators         | 222 ms                                                      | 268 ms: 1.21x slower                                                        |
| python_startup           | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.27x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.94 ms: 1.38x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 91.1 ms: 1.47x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.41 ms: 1.76x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (3): logging_simple, genshi_text, meteor_contest
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.194x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown