# Results vs. 3.10.4

- fork: mdboom
- ref: remove_pragma
- machine: windows-amd64
- commit hash: a03affd
- commit date: 2024-07-02
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                              |
| html5lib       | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                               |
| tornado_http   | 108 ms                                                      | 82.5 ms: 1.31x faster                                               |
| Geometric mean | (ref)                                                       | 1.19x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 263 ms: 2.00x faster                                                |
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                |
| async_tree_io           | 1.11 sec                                                    | 565 ms: 1.96x faster                                                |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 57.8 ms: 1.07x faster                                               |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                |
| nbody          | 71.3 ms                                                     | 86.1 ms: 1.21x slower                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                |
| regex_compile  | 106 ms                                                      | 92.2 ms: 1.15x faster                                               |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                       | 1.08x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.13 ms: 1.49x faster                                               |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                |
| unpickle_pure_python | 183 us                                                      | 154 us: 1.19x faster                                                |
| xml_etree_process    | 44.5 ms                                                     | 41.8 ms: 1.06x faster                                               |
| tomli_loads          | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                              |
| xml_etree_parse      | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.2 ms: 1.03x slower                                               |
| xml_etree_generate   | 55.5 ms                                                     | 60.2 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.8 ms: 1.01x slower                                               |
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                               |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                               |
| mako            | 9.03 ms                                                     | 7.84 ms: 1.15x faster                                               |
| genshi_xml      | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                               |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                |
| async_tree_memoization   | 526 ms                                                      | 263 ms: 2.00x faster                                                |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                |
| async_tree_io            | 1.11 sec                                                    | 565 ms: 1.96x faster                                                |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                |
| pylint                   | 350 ms                                                      | 213 ms: 1.64x faster                                                |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                               |
| asyncio_tcp              | 732 ms                                                      | 486 ms: 1.51x faster                                                |
| raytrace                 | 273 ms                                                      | 182 ms: 1.51x faster                                                |
| json_dumps               | 9.16 ms                                                     | 6.13 ms: 1.49x faster                                               |
| logging_silent           | 94.6 ns                                                     | 63.4 ns: 1.49x faster                                               |
| go                       | 139 ms                                                      | 97.9 ms: 1.42x faster                                               |
| richards                 | 42.4 ms                                                     | 30.3 ms: 1.40x faster                                               |
| generators               | 32.4 ms                                                     | 23.1 ms: 1.40x faster                                               |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.40x faster                                              |
| chaos                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                               |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.38x faster                                               |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                |
| deepcopy_memo            | 28.8 us                                                     | 21.5 us: 1.34x faster                                               |
| sqlglot_parse            | 1.22 ms                                                     | 919 us: 1.32x faster                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                               |
| tornado_http             | 108 ms                                                      | 82.5 ms: 1.31x faster                                               |
| hexiom                   | 5.74 ms                                                     | 4.48 ms: 1.28x faster                                               |
| pyflate                  | 409 ms                                                      | 323 ms: 1.27x faster                                                |
| scimark_lu               | 85.8 ms                                                     | 67.8 ms: 1.26x faster                                               |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                |
| html5lib                 | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                               |
| bench_thread_pool        | 958 us                                                      | 770 us: 1.24x faster                                                |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 154 us: 1.19x faster                                                |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                |
| crypto_pyaes             | 62.5 ms                                                     | 53.0 ms: 1.18x faster                                               |
| scimark_sor              | 106 ms                                                      | 90.4 ms: 1.17x faster                                               |
| sympy_sum                | 107 ms                                                      | 91.2 ms: 1.17x faster                                               |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                               |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                               |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                               |
| mako                     | 9.03 ms                                                     | 7.84 ms: 1.15x faster                                               |
| regex_compile            | 106 ms                                                      | 92.2 ms: 1.15x faster                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                               |
| thrift                   | 617 us                                                      | 546 us: 1.13x faster                                                |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.2 ms: 1.12x faster                                               |
| sqlglot_optimize         | 39.8 ms                                                     | 35.8 ms: 1.11x faster                                               |
| pycparser                | 930 ms                                                      | 839 ms: 1.11x faster                                                |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                               |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                |
| sqlglot_normalize        | 205 ms                                                      | 190 ms: 1.08x faster                                                |
| spectral_norm            | 77.3 ms                                                     | 72.2 ms: 1.07x faster                                               |
| float                    | 61.7 ms                                                     | 57.8 ms: 1.07x faster                                               |
| xml_etree_process        | 44.5 ms                                                     | 41.8 ms: 1.06x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                              |
| genshi_xml               | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                               |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                               |
| pprint_safe_repr         | 592 ms                                                      | 565 ms: 1.05x faster                                                |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                               |
| tomli_loads              | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                              |
| nqueens                  | 66.6 ms                                                     | 64.8 ms: 1.03x faster                                               |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                |
| xml_etree_parse          | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                               |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                |
| python_startup           | 20.6 ms                                                     | 20.8 ms: 1.01x slower                                               |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                               |
| logging_simple           | 6.22 us                                                     | 6.38 us: 1.03x slower                                               |
| meteor_contest           | 75.9 ms                                                     | 78.0 ms: 1.03x slower                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.2 ms: 1.03x slower                                               |
| bench_mp_pool            | 62.0 ms                                                     | 65.8 ms: 1.06x slower                                               |
| xml_etree_generate       | 55.5 ms                                                     | 60.2 ms: 1.08x slower                                               |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.10x slower                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.99 ms: 1.10x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                               |
| create_gc_cycles         | 800 us                                                      | 899 us: 1.12x slower                                                |
| async_generators         | 222 ms                                                      | 257 ms: 1.16x slower                                                |
| scimark_fft              | 187 ms                                                      | 220 ms: 1.18x slower                                                |
| fannkuch                 | 256 ms                                                      | 305 ms: 1.19x slower                                                |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                               |
| nbody                    | 71.3 ms                                                     | 86.1 ms: 1.21x slower                                               |
| telco                    | 3.94 ms                                                     | 4.97 ms: 1.26x slower                                               |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                        |

Benchmark hidden because not significant (3): json_loads, pathlib, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240702-3.14.0a0-a03affd/bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown