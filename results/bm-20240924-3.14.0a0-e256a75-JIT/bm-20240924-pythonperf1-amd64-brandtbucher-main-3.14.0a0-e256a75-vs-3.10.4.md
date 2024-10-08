# Results vs. 3.10.4

- fork: brandtbucher
- ref: main
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 240 ms: 1.03x faster                                             |
| html5lib       | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                            |
| tornado_http   | 108 ms                                                      | 88.1 ms: 1.23x faster                                            |
| Geometric mean | (ref)                                                       | 1.12x faster                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 202 ms: 2.16x faster                                             |
| async_tree_memoization  | 526 ms                                                      | 255 ms: 2.06x faster                                             |
| async_tree_io           | 1.11 sec                                                    | 578 ms: 1.92x faster                                             |
| async_tree_cpu_io_mixed | 638 ms                                                      | 393 ms: 1.62x faster                                             |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.6 ms: 1.44x faster                                            |
| float          | 61.7 ms                                                     | 53.4 ms: 1.16x faster                                            |
| Geometric mean | (ref)                                                       | 1.18x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                             |
| regex_compile  | 106 ms                                                      | 94.7 ms: 1.12x faster                                            |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                       | 1.08x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.89 ms: 1.56x faster                                            |
| pickle_pure_python   | 270 us                                                      | 196 us: 1.38x faster                                             |
| tomli_loads          | 1.67 sec                                                    | 1.29 sec: 1.29x faster                                           |
| unpickle_pure_python | 183 us                                                      | 143 us: 1.28x faster                                             |
| xml_etree_process    | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                            |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                            |
| xml_etree_generate   | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                            |
| xml_etree_parse      | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                            |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                            |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                            |
| pickle_dict          | 17.2 us                                                     | 17.8 us: 1.03x slower                                            |
| pickle               | 6.85 us                                                     | 7.43 us: 1.08x slower                                            |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                     |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                            |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                            |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.20 ms: 1.74x faster                                            |
| django_template | 28.9 ms                                                     | 26.4 ms: 1.09x faster                                            |
| genshi_text     | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                            |
| genshi_xml      | 41.0 ms                                                     | 45.5 ms: 1.11x slower                                            |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                             |
| deltablue                | 4.19 ms                                                     | 1.83 ms: 2.29x faster                                            |
| async_tree_none          | 435 ms                                                      | 202 ms: 2.16x faster                                             |
| async_tree_memoization   | 526 ms                                                      | 255 ms: 2.06x faster                                             |
| async_tree_io            | 1.11 sec                                                    | 578 ms: 1.92x faster                                             |
| deepcopy_memo            | 28.8 us                                                     | 15.3 us: 1.88x faster                                            |
| scimark_sor              | 106 ms                                                      | 60.5 ms: 1.75x faster                                            |
| mako                     | 9.03 ms                                                     | 5.20 ms: 1.74x faster                                            |
| spectral_norm            | 77.3 ms                                                     | 44.8 ms: 1.73x faster                                            |
| logging_silent           | 94.6 ns                                                     | 57.0 ns: 1.66x faster                                            |
| crypto_pyaes             | 62.5 ms                                                     | 38.1 ms: 1.64x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 393 ms: 1.62x faster                                             |
| scimark_lu               | 85.8 ms                                                     | 53.9 ms: 1.59x faster                                            |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                            |
| pyflate                  | 409 ms                                                      | 263 ms: 1.56x faster                                             |
| json_dumps               | 9.16 ms                                                     | 5.89 ms: 1.56x faster                                            |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.37 sec: 1.54x faster                                           |
| asyncio_tcp              | 732 ms                                                      | 477 ms: 1.54x faster                                             |
| chaos                    | 61.7 ms                                                     | 40.7 ms: 1.52x faster                                            |
| go                       | 139 ms                                                      | 91.7 ms: 1.51x faster                                            |
| generators               | 32.4 ms                                                     | 21.9 ms: 1.48x faster                                            |
| nbody                    | 71.3 ms                                                     | 49.6 ms: 1.44x faster                                            |
| deepcopy                 | 255 us                                                      | 183 us: 1.39x faster                                             |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                             |
| pickle_pure_python       | 270 us                                                      | 196 us: 1.38x faster                                             |
| sqlglot_parse            | 1.22 ms                                                     | 887 us: 1.37x faster                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.7 ms: 1.34x faster                                            |
| richards_super           | 52.2 ms                                                     | 39.3 ms: 1.33x faster                                            |
| pylint                   | 350 ms                                                      | 264 ms: 1.33x faster                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.06 ms: 1.32x faster                                            |
| pycparser                | 930 ms                                                      | 706 ms: 1.32x faster                                             |
| tomli_loads              | 1.67 sec                                                    | 1.29 sec: 1.29x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 143 us: 1.28x faster                                             |
| xml_etree_process        | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                            |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.28x faster                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.27x faster                                            |
| html5lib                 | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                            |
| tornado_http             | 108 ms                                                      | 88.1 ms: 1.23x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                            |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                            |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                             |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                           |
| hexiom                   | 5.74 ms                                                     | 4.88 ms: 1.18x faster                                            |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                            |
| bench_thread_pool        | 958 us                                                      | 820 us: 1.17x faster                                             |
| richards                 | 42.4 ms                                                     | 36.6 ms: 1.16x faster                                            |
| float                    | 61.7 ms                                                     | 53.4 ms: 1.16x faster                                            |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                           |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                             |
| pprint_safe_repr         | 592 ms                                                      | 524 ms: 1.13x faster                                             |
| regex_compile            | 106 ms                                                      | 94.7 ms: 1.12x faster                                            |
| sqlite_synth             | 1.91 us                                                     | 1.73 us: 1.11x faster                                            |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                            |
| fannkuch                 | 256 ms                                                      | 233 ms: 1.10x faster                                             |
| django_template          | 28.9 ms                                                     | 26.4 ms: 1.09x faster                                            |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                            |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                            |
| sympy_sum                | 107 ms                                                      | 99.1 ms: 1.08x faster                                            |
| xml_etree_generate       | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                            |
| logging_format           | 6.76 us                                                     | 6.33 us: 1.07x faster                                            |
| logging_simple           | 6.22 us                                                     | 5.91 us: 1.05x faster                                            |
| xml_etree_parse          | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                            |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                            |
| sqlglot_normalize        | 205 ms                                                      | 198 ms: 1.03x faster                                             |
| genshi_text              | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                            |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                            |
| sympy_str                | 194 ms                                                      | 189 ms: 1.03x faster                                             |
| 2to3                     | 246 ms                                                      | 240 ms: 1.03x faster                                             |
| sympy_integrate          | 15.3 ms                                                     | 14.9 ms: 1.03x faster                                            |
| meteor_contest           | 75.9 ms                                                     | 75.3 ms: 1.01x faster                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 39.7 ms: 1.00x faster                                            |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                            |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                            |
| pickle_dict              | 17.2 us                                                     | 17.8 us: 1.03x slower                                            |
| sympy_expand             | 314 ms                                                      | 332 ms: 1.05x slower                                             |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                            |
| pickle                   | 6.85 us                                                     | 7.43 us: 1.08x slower                                            |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                            |
| genshi_xml               | 41.0 ms                                                     | 45.5 ms: 1.11x slower                                            |
| create_gc_cycles         | 800 us                                                      | 895 us: 1.12x slower                                             |
| bench_mp_pool            | 62.0 ms                                                     | 70.2 ms: 1.13x slower                                            |
| telco                    | 3.94 ms                                                     | 4.53 ms: 1.15x slower                                            |
| async_generators         | 222 ms                                                      | 257 ms: 1.16x slower                                             |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                            |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                            |
| unpack_sequence          | 39.6 ns                                                     | 59.6 ns: 1.50x slower                                            |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                     |

Benchmark hidden because not significant (5): pathlib, pidigits, unpickle, docutils, pickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown