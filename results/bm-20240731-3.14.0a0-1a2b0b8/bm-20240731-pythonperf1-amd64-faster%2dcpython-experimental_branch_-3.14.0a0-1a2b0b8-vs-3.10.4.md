# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                               |
| html5lib       | 51.0 ms                                                     | 42.3 ms: 1.21x faster                                                                |
| tornado_http   | 108 ms                                                      | 93.4 ms: 1.16x faster                                                                |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                                 |
| async_tree_io           | 1.11 sec                                                    | 573 ms: 1.93x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 388 ms: 1.64x faster                                                                 |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.6 ms: 1.09x faster                                                                |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                                 |
| nbody          | 71.3 ms                                                     | 92.0 ms: 1.29x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| regex_compile  | 106 ms                                                      | 95.0 ms: 1.12x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.43 ms: 1.42x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                                 |
| xml_etree_process    | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                                               |
| xml_etree_parse      | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.0 ms: 1.02x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 58.1 ms: 1.05x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.13x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.25 ms: 1.25x faster                                                                |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 36.8 ms: 1.11x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 573 ms: 1.93x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.82x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 388 ms: 1.64x faster                                                                 |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                                 |
| generators               | 32.4 ms                                                     | 22.0 ms: 1.47x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 64.4 ns: 1.47x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.43 ms: 1.42x faster                                                                |
| richards_super           | 52.2 ms                                                     | 37.0 ms: 1.41x faster                                                                |
| raytrace                 | 273 ms                                                      | 196 ms: 1.40x faster                                                                 |
| go                       | 139 ms                                                      | 99.7 ms: 1.39x faster                                                                |
| chaos                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                                |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 21.1 us: 1.36x faster                                                                |
| asyncio_tcp              | 732 ms                                                      | 539 ms: 1.36x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 906 us: 1.34x faster                                                                 |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 65.5 ms: 1.31x faster                                                                |
| richards                 | 42.4 ms                                                     | 32.8 ms: 1.29x faster                                                                |
| mako                     | 9.03 ms                                                     | 7.25 ms: 1.25x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.24x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                                 |
| pyflate                  | 409 ms                                                      | 330 ms: 1.24x faster                                                                 |
| pycparser                | 930 ms                                                      | 752 ms: 1.24x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 42.3 ms: 1.21x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 51.8 ms: 1.21x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 808 us: 1.18x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 42.7 ms: 1.18x faster                                                                |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                                 |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                                |
| sympy_sum                | 107 ms                                                      | 92.1 ms: 1.16x faster                                                                |
| tornado_http             | 108 ms                                                      | 93.4 ms: 1.16x faster                                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.85 sec: 1.14x faster                                                               |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.2 ms: 1.12x faster                                                                |
| regex_compile            | 106 ms                                                      | 95.0 ms: 1.12x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 36.8 ms: 1.11x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                                |
| scimark_sor              | 106 ms                                                      | 96.5 ms: 1.10x faster                                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                               |
| float                    | 61.7 ms                                                     | 56.6 ms: 1.09x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| sympy_str                | 194 ms                                                      | 181 ms: 1.07x faster                                                                 |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                                 |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.16 sec: 1.05x faster                                                               |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 74.1 ms: 1.04x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 569 ms: 1.04x faster                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 64.9 ms: 1.03x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                                |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.17 ms: 1.01x slower                                                                |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.0 ms: 1.02x slower                                                                |
| logging_format           | 6.76 us                                                     | 6.89 us: 1.02x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.39 us: 1.03x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                                |
| meteor_contest           | 75.9 ms                                                     | 79.0 ms: 1.04x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 58.1 ms: 1.05x slower                                                                |
| python_startup           | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.88 ms: 1.06x slower                                                                |
| pathlib                  | 75.7 ms                                                     | 80.5 ms: 1.06x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                                |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                                 |
| create_gc_cycles         | 800 us                                                      | 885 us: 1.11x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 69.1 ms: 1.11x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.13x slower                                                                |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                                                 |
| fannkuch                 | 256 ms                                                      | 301 ms: 1.18x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.22x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.93 ms: 1.25x slower                                                                |
| nbody                    | 71.3 ms                                                     | 92.0 ms: 1.29x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                         |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown