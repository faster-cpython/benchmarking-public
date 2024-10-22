# Results vs. 3.10.4

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-amd64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 238 ms: 1.03x faster                                                          |
| docutils       | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                        |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                         |
| tornado_http   | 108 ms                                                      | 94.0 ms: 1.15x faster                                                         |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 208 ms: 2.09x faster                                                          |
| async_tree_io           | 1.11 sec                                                    | 536 ms: 2.07x faster                                                          |
| async_tree_memoization  | 526 ms                                                      | 255 ms: 2.07x faster                                                          |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.67x faster                                                          |
| Geometric mean          | (ref)                                                       | 1.96x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.9 ms: 1.40x faster                                                         |
| nbody          | 71.3 ms                                                     | 50.9 ms: 1.40x faster                                                         |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.4 ms: 1.19x faster                                                         |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                         |
| regex_v8       | 15.4 ms                                                     | 15.5 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                                         |
| pickle_pure_python   | 270 us                                                      | 181 us: 1.49x faster                                                          |
| unpickle_pure_python | 183 us                                                      | 130 us: 1.41x faster                                                          |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 37.2 ms: 1.20x faster                                                         |
| xml_etree_generate   | 55.5 ms                                                     | 52.5 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                         |
| xml_etree_parse      | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                         |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                         |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.98 ms: 1.81x faster                                                         |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                         |
| genshi_text     | 19.8 ms                                                     | 17.7 ms: 1.12x faster                                                         |
| genshi_xml      | 41.0 ms                                                     | 44.7 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 118 us: 2.85x faster                                                          |
| async_tree_none          | 435 ms                                                      | 208 ms: 2.09x faster                                                          |
| async_tree_io            | 1.11 sec                                                    | 536 ms: 2.07x faster                                                          |
| async_tree_memoization   | 526 ms                                                      | 255 ms: 2.07x faster                                                          |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.95x faster                                                         |
| deepcopy_memo            | 28.8 us                                                     | 15.5 us: 1.86x faster                                                         |
| mako                     | 9.03 ms                                                     | 4.98 ms: 1.81x faster                                                         |
| logging_silent           | 94.6 ns                                                     | 55.4 ns: 1.71x faster                                                         |
| spectral_norm            | 77.3 ms                                                     | 46.1 ms: 1.68x faster                                                         |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.67x faster                                                          |
| pyflate                  | 409 ms                                                      | 247 ms: 1.65x faster                                                          |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                         |
| json_dumps               | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                                         |
| richards_super           | 52.2 ms                                                     | 33.5 ms: 1.56x faster                                                         |
| raytrace                 | 273 ms                                                      | 176 ms: 1.56x faster                                                          |
| chaos                    | 61.7 ms                                                     | 39.7 ms: 1.55x faster                                                         |
| crypto_pyaes             | 62.5 ms                                                     | 40.5 ms: 1.54x faster                                                         |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.4 ms: 1.53x faster                                                         |
| sqlglot_parse            | 1.22 ms                                                     | 808 us: 1.50x faster                                                          |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                         |
| pickle_pure_python       | 270 us                                                      | 181 us: 1.49x faster                                                          |
| go                       | 139 ms                                                      | 95.4 ms: 1.46x faster                                                         |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.44x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                         |
| pylint                   | 350 ms                                                      | 246 ms: 1.42x faster                                                          |
| richards                 | 42.4 ms                                                     | 29.9 ms: 1.42x faster                                                         |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.41x faster                                                          |
| deepcopy                 | 255 us                                                      | 182 us: 1.41x faster                                                          |
| float                    | 61.7 ms                                                     | 43.9 ms: 1.40x faster                                                         |
| nbody                    | 71.3 ms                                                     | 50.9 ms: 1.40x faster                                                         |
| asyncio_tcp              | 732 ms                                                      | 531 ms: 1.38x faster                                                          |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.01 ms: 1.35x faster                                                         |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                        |
| pycparser                | 930 ms                                                      | 708 ms: 1.31x faster                                                          |
| pprint_pformat           | 1.22 sec                                                    | 950 ms: 1.28x faster                                                          |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                         |
| pprint_safe_repr         | 592 ms                                                      | 468 ms: 1.26x faster                                                          |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 4.65 ms: 1.23x faster                                                         |
| scimark_sor              | 106 ms                                                      | 86.1 ms: 1.23x faster                                                         |
| thrift                   | 617 us                                                      | 502 us: 1.23x faster                                                          |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.22x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.21x faster                                                         |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                                         |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                         |
| xml_etree_process        | 44.5 ms                                                     | 37.2 ms: 1.20x faster                                                         |
| scimark_lu               | 85.8 ms                                                     | 72.0 ms: 1.19x faster                                                         |
| regex_compile            | 106 ms                                                      | 89.4 ms: 1.19x faster                                                         |
| bench_thread_pool        | 958 us                                                      | 815 us: 1.18x faster                                                          |
| fannkuch                 | 256 ms                                                      | 219 ms: 1.17x faster                                                          |
| tornado_http             | 108 ms                                                      | 94.0 ms: 1.15x faster                                                         |
| sympy_sum                | 107 ms                                                      | 94.5 ms: 1.13x faster                                                         |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                         |
| nqueens                  | 66.6 ms                                                     | 59.0 ms: 1.13x faster                                                         |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                          |
| genshi_text              | 19.8 ms                                                     | 17.7 ms: 1.12x faster                                                         |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                         |
| logging_format           | 6.76 us                                                     | 6.24 us: 1.08x faster                                                         |
| sympy_integrate          | 15.3 ms                                                     | 14.2 ms: 1.07x faster                                                         |
| logging_simple           | 6.22 us                                                     | 5.80 us: 1.07x faster                                                         |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                          |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 52.5 ms: 1.06x faster                                                         |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                         |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.05x faster                                                         |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                         |
| docutils                 | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                         |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                         |
| 2to3                     | 246 ms                                                      | 238 ms: 1.03x faster                                                          |
| regex_v8                 | 15.4 ms                                                     | 15.5 ms: 1.01x slower                                                         |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                          |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                         |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                         |
| pathlib                  | 75.7 ms                                                     | 81.4 ms: 1.08x slower                                                         |
| genshi_xml               | 41.0 ms                                                     | 44.7 ms: 1.09x slower                                                         |
| gc_traversal             | 1.41 ms                                                     | 1.58 ms: 1.12x slower                                                         |
| telco                    | 3.94 ms                                                     | 4.47 ms: 1.13x slower                                                         |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 910 us: 1.14x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 72.6 ms: 1.17x slower                                                         |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                         |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.21x slower                                                         |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                                  |

Benchmark hidden because not significant (1): sympy_expand
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown