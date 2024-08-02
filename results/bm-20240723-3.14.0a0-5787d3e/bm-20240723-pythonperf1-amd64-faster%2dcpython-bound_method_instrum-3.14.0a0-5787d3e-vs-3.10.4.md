# Results vs. 3.10.4

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-amd64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                               |
| html5lib       | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                                                |
| tornado_http   | 108 ms                                                      | 91.6 ms: 1.18x faster                                                                |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 258 ms: 2.04x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 214 ms: 2.04x faster                                                                 |
| async_tree_io           | 1.11 sec                                                    | 547 ms: 2.03x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 382 ms: 1.67x faster                                                                 |
| Geometric mean          | (ref)                                                       | 1.94x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.3 ms: 1.10x faster                                                                |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                                 |
| nbody          | 71.3 ms                                                     | 83.8 ms: 1.18x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.4 ms: 1.17x faster                                                                |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.00 ms: 1.53x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                                 |
| xml_etree_process    | 44.5 ms                                                     | 40.6 ms: 1.10x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                               |
| xml_etree_parse      | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.0 us: 1.00x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 58.1 ms: 1.05x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                                |
| mako            | 9.03 ms                                                     | 7.48 ms: 1.21x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.12x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 258 ms: 2.04x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.04x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 547 ms: 2.03x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.89x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 382 ms: 1.67x faster                                                                 |
| pylint                   | 350 ms                                                      | 221 ms: 1.59x faster                                                                 |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.00 ms: 1.53x faster                                                                |
| raytrace                 | 273 ms                                                      | 179 ms: 1.52x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 62.6 ns: 1.51x faster                                                                |
| richards_super           | 52.2 ms                                                     | 35.1 ms: 1.49x faster                                                                |
| go                       | 139 ms                                                      | 95.5 ms: 1.45x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                                |
| chaos                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                                |
| deepcopy                 | 255 us                                                      | 184 us: 1.38x faster                                                                 |
| asyncio_tcp              | 732 ms                                                      | 533 ms: 1.37x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 893 us: 1.36x faster                                                                 |
| richards                 | 42.4 ms                                                     | 31.4 ms: 1.35x faster                                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 21.7 us: 1.33x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 65.9 ms: 1.30x faster                                                                |
| pyflate                  | 409 ms                                                      | 316 ms: 1.30x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                                 |
| hexiom                   | 5.74 ms                                                     | 4.46 ms: 1.29x faster                                                                |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                                               |
| crypto_pyaes             | 62.5 ms                                                     | 50.2 ms: 1.25x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                                 |
| django_template          | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                                |
| mako                     | 9.03 ms                                                     | 7.48 ms: 1.21x faster                                                                |
| sympy_sum                | 107 ms                                                      | 89.3 ms: 1.20x faster                                                                |
| pycparser                | 930 ms                                                      | 781 ms: 1.19x faster                                                                 |
| bench_thread_pool        | 958 us                                                      | 806 us: 1.19x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                                |
| tornado_http             | 108 ms                                                      | 91.6 ms: 1.18x faster                                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.79 sec: 1.18x faster                                                               |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.17x faster                                                                |
| regex_compile            | 106 ms                                                      | 90.4 ms: 1.17x faster                                                                |
| scimark_sor              | 106 ms                                                      | 90.9 ms: 1.17x faster                                                                |
| thrift                   | 617 us                                                      | 530 us: 1.17x faster                                                                 |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 34.6 ms: 1.15x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.1 ms: 1.14x faster                                                                |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                               |
| genshi_xml               | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                                |
| sqlglot_normalize        | 205 ms                                                      | 184 ms: 1.12x faster                                                                 |
| sympy_str                | 194 ms                                                      | 174 ms: 1.12x faster                                                                 |
| float                    | 61.7 ms                                                     | 56.3 ms: 1.10x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 40.6 ms: 1.10x faster                                                                |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                                 |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                               |
| tomli_loads              | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                                |
| sympy_expand             | 314 ms                                                      | 298 ms: 1.06x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 63.2 ms: 1.05x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 563 ms: 1.05x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 73.5 ms: 1.05x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                                |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                                                |
| json_loads               | 14.0 us                                                     | 14.0 us: 1.00x faster                                                                |
| logging_simple           | 6.22 us                                                     | 6.20 us: 1.00x faster                                                                |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 58.1 ms: 1.05x slower                                                                |
| python_startup           | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                                |
| pathlib                  | 75.7 ms                                                     | 80.5 ms: 1.06x slower                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.90 ms: 1.06x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 67.3 ms: 1.09x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                                |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                                 |
| create_gc_cycles         | 800 us                                                      | 903 us: 1.13x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                                                |
| scimark_fft              | 187 ms                                                      | 219 ms: 1.17x slower                                                                 |
| fannkuch                 | 256 ms                                                      | 300 ms: 1.17x slower                                                                 |
| nbody                    | 71.3 ms                                                     | 83.8 ms: 1.18x slower                                                                |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.21x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                                         |

Benchmark hidden because not significant (1): meteor_contest
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown