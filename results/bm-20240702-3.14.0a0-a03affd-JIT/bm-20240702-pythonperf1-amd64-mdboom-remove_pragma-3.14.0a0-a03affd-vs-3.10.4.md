# Results vs. 3.10.4

- fork: mdboom
- ref: remove_pragma
- machine: windows-amd64
- commit hash: a03affd
- commit date: 2024-07-02
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 236 ms: 1.04x faster                                                |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                              |
| html5lib       | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                               |
| tornado_http   | 108 ms                                                      | 85.0 ms: 1.27x faster                                               |
| Geometric mean | (ref)                                                       | 1.16x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 212 ms: 2.05x faster                                                |
| async_tree_io           | 1.11 sec                                                    | 541 ms: 2.05x faster                                                |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.03x faster                                                |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                                |
| Geometric mean          | (ref)                                                       | 1.94x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.7 ms: 1.44x faster                                               |
| float          | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                               |
| Geometric mean | (ref)                                                       | 1.24x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.2 ms: 1.18x faster                                               |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                               |
| regex_v8       | 15.4 ms                                                     | 19.9 ms: 1.29x slower                                               |
| Geometric mean | (ref)                                                       | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                               |
| pickle_pure_python   | 270 us                                                      | 182 us: 1.48x faster                                                |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                                |
| tomli_loads          | 1.67 sec                                                    | 1.29 sec: 1.29x faster                                              |
| xml_etree_process    | 44.5 ms                                                     | 38.5 ms: 1.15x faster                                               |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.6 ms: 1.07x faster                                               |
| xml_etree_parse      | 96.8 ms                                                     | 92.0 ms: 1.05x faster                                               |
| xml_etree_generate   | 55.5 ms                                                     | 53.4 ms: 1.04x faster                                               |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.1 ms: 1.02x slower                                               |
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.30 ms: 1.70x faster                                               |
| django_template | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                               |
| genshi_text     | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                               |
| genshi_xml      | 41.0 ms                                                     | 45.9 ms: 1.12x slower                                               |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.05x faster                                                |
| async_tree_io            | 1.11 sec                                                    | 541 ms: 2.05x faster                                                |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.03x faster                                                |
| deepcopy_memo            | 28.8 us                                                     | 15.9 us: 1.81x faster                                               |
| deltablue                | 4.19 ms                                                     | 2.32 ms: 1.80x faster                                               |
| mako                     | 9.03 ms                                                     | 5.30 ms: 1.70x faster                                               |
| spectral_norm            | 77.3 ms                                                     | 45.6 ms: 1.69x faster                                               |
| logging_silent           | 94.6 ns                                                     | 56.7 ns: 1.67x faster                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                                |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.58x faster                                               |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                |
| json_dumps               | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                               |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                               |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                               |
| asyncio_tcp              | 732 ms                                                      | 483 ms: 1.52x faster                                                |
| richards_super           | 52.2 ms                                                     | 35.0 ms: 1.49x faster                                               |
| pylint                   | 350 ms                                                      | 236 ms: 1.49x faster                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.6 ms: 1.48x faster                                               |
| pickle_pure_python       | 270 us                                                      | 182 us: 1.48x faster                                                |
| sqlglot_parse            | 1.22 ms                                                     | 827 us: 1.47x faster                                                |
| raytrace                 | 273 ms                                                      | 186 ms: 1.47x faster                                                |
| nbody                    | 71.3 ms                                                     | 49.7 ms: 1.44x faster                                               |
| go                       | 139 ms                                                      | 96.8 ms: 1.43x faster                                               |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                               |
| richards                 | 42.4 ms                                                     | 30.6 ms: 1.39x faster                                               |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                                |
| generators               | 32.4 ms                                                     | 24.1 ms: 1.34x faster                                               |
| float                    | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.08 ms: 1.31x faster                                               |
| tomli_loads              | 1.67 sec                                                    | 1.29 sec: 1.29x faster                                              |
| html5lib                 | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                               |
| tornado_http             | 108 ms                                                      | 85.0 ms: 1.27x faster                                               |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                              |
| pprint_safe_repr         | 592 ms                                                      | 482 ms: 1.23x faster                                                |
| hexiom                   | 5.74 ms                                                     | 4.69 ms: 1.23x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                              |
| bench_thread_pool        | 958 us                                                      | 792 us: 1.21x faster                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                               |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                |
| regex_compile            | 106 ms                                                      | 90.2 ms: 1.18x faster                                               |
| fannkuch                 | 256 ms                                                      | 220 ms: 1.16x faster                                                |
| scimark_sor              | 106 ms                                                      | 92.0 ms: 1.15x faster                                               |
| xml_etree_process        | 44.5 ms                                                     | 38.5 ms: 1.15x faster                                               |
| sympy_sum                | 107 ms                                                      | 94.4 ms: 1.13x faster                                               |
| scimark_lu               | 85.8 ms                                                     | 76.4 ms: 1.12x faster                                               |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                               |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                |
| django_template          | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                               |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                               |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.09x faster                                               |
| genshi_text              | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                               |
| nqueens                  | 66.6 ms                                                     | 61.7 ms: 1.08x faster                                               |
| pycparser                | 930 ms                                                      | 862 ms: 1.08x faster                                                |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.6 ms: 1.07x faster                                               |
| logging_format           | 6.76 us                                                     | 6.31 us: 1.07x faster                                               |
| sympy_str                | 194 ms                                                      | 183 ms: 1.06x faster                                                |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                               |
| logging_simple           | 6.22 us                                                     | 5.91 us: 1.05x faster                                               |
| xml_etree_parse          | 96.8 ms                                                     | 92.0 ms: 1.05x faster                                               |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                |
| 2to3                     | 246 ms                                                      | 236 ms: 1.04x faster                                                |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                               |
| xml_etree_generate       | 55.5 ms                                                     | 53.4 ms: 1.04x faster                                               |
| meteor_contest           | 75.9 ms                                                     | 75.0 ms: 1.01x faster                                               |
| sympy_expand             | 314 ms                                                      | 316 ms: 1.01x slower                                                |
| pathlib                  | 75.7 ms                                                     | 76.1 ms: 1.01x slower                                               |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                               |
| python_startup           | 20.6 ms                                                     | 21.1 ms: 1.02x slower                                               |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                               |
| genshi_xml               | 41.0 ms                                                     | 45.9 ms: 1.12x slower                                               |
| bench_mp_pool            | 62.0 ms                                                     | 69.6 ms: 1.12x slower                                               |
| create_gc_cycles         | 800 us                                                      | 904 us: 1.13x slower                                                |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                               |
| coverage                 | 39.0 ms                                                     | 46.2 ms: 1.18x slower                                               |
| async_generators         | 222 ms                                                      | 270 ms: 1.22x slower                                                |
| regex_v8                 | 15.4 ms                                                     | 19.9 ms: 1.29x slower                                               |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                        |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240702-3.14.0a0-a03affd-JIT/bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown