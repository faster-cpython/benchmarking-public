# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-amd64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| html5lib       | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| tornado_http   | 108 ms                                                      | 96.2 ms: 1.13x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 217 ms: 2.00x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 559 ms: 1.98x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 274 ms: 1.92x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                       |
| float          | 61.7 ms                                                     | 47.5 ms: 1.30x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.1 ms: 1.16x faster                                                       |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 199 us: 1.35x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 143 us: 1.29x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.99 ms: 1.81x faster                                                       |
| django_template | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 44.1 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.04x faster                                                        |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 559 ms: 1.98x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 274 ms: 1.92x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.82x faster                                                       |
| mako                     | 9.03 ms                                                     | 4.99 ms: 1.81x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.6 us: 1.73x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.3 ns: 1.68x faster                                                       |
| scimark_sor              | 106 ms                                                      | 64.3 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 53.3 ms: 1.61x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.8 ms: 1.56x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.6 ms: 1.54x faster                                                       |
| go                       | 139 ms                                                      | 90.4 ms: 1.54x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.2 ms: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 285 ms: 1.44x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 54.0 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.43x faster                                                       |
| generators               | 32.4 ms                                                     | 22.7 ms: 1.42x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.3 ms: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 893 us: 1.36x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 199 us: 1.35x faster                                                        |
| nbody                    | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                       |
| deepcopy                 | 255 us                                                      | 190 us: 1.35x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 450 ms: 1.31x faster                                                        |
| float                    | 61.7 ms                                                     | 47.5 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| raytrace                 | 273 ms                                                      | 212 ms: 1.29x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 143 us: 1.29x faster                                                        |
| pycparser                | 930 ms                                                      | 725 ms: 1.28x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 953 ms: 1.28x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.17 ms: 1.26x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.0 ms: 1.25x faster                                                       |
| pylint                   | 350 ms                                                      | 281 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.19 ms: 1.24x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                        |
| scimark_fft              | 187 ms                                                      | 159 ms: 1.18x faster                                                        |
| regex_compile            | 106 ms                                                      | 91.1 ms: 1.16x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.54 sec: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 835 us: 1.15x faster                                                        |
| tornado_http             | 108 ms                                                      | 96.2 ms: 1.13x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 5.13 ms: 1.12x faster                                                       |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| fannkuch                 | 256 ms                                                      | 232 ms: 1.10x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 61.9 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.04x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.49 us: 1.04x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                       |
| sympy_str                | 194 ms                                                      | 192 ms: 1.01x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.15 us: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.4 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 206 ms: 1.00x slower                                                        |
| sympy_integrate          | 15.3 ms                                                     | 15.7 ms: 1.03x slower                                                       |
| sympy_expand             | 314 ms                                                      | 323 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 80.4 ms: 1.06x slower                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 42.6 ms: 1.07x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 44.1 ms: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                       |
| async_generators         | 222 ms                                                      | 258 ms: 1.16x slower                                                        |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| coverage                 | 39.0 ms                                                     | 50.3 ms: 1.29x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.2 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.40 ms: 1.75x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (3): json, docutils, 2to3
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown