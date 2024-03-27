# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_binary_op
- machine: windows-amd64
- commit hash: 8183250
- commit date: 2024-03-27
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 213 ms: 1.15x faster                                                                  |
| chameleon      | 5.79 ms                                                     | 4.76 ms: 1.21x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                                |
| html5lib       | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                                 |
| tornado_http   | 108 ms                                                      | 84.0 ms: 1.29x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 223 ms: 1.95x faster                                                                  |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                                  |
| async_tree_io           | 1.11 sec                                                    | 585 ms: 1.90x faster                                                                  |
| async_tree_cpu_io_mixed | 638 ms                                                      | 382 ms: 1.67x faster                                                                  |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.8 ms: 1.19x faster                                                                 |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                                  |
| nbody          | 71.3 ms                                                     | 77.5 ms: 1.09x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.3 ms: 1.30x faster                                                                 |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.55 ms: 1.65x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 179 us: 1.51x faster                                                                  |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.45x faster                                                                  |
| xml_etree_process    | 44.5 ms                                                     | 37.3 ms: 1.19x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                                |
| unpickle             | 9.09 us                                                     | 8.47 us: 1.07x faster                                                                 |
| xml_etree_parse      | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                                 |
| xml_etree_generate   | 55.5 ms                                                     | 54.3 ms: 1.02x faster                                                                 |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                                 |
| unpickle_list        | 2.71 us                                                     | 2.82 us: 1.04x slower                                                                 |
| pickle_list          | 2.75 us                                                     | 2.87 us: 1.04x slower                                                                 |
| pickle_dict          | 17.2 us                                                     | 18.1 us: 1.06x slower                                                                 |
| pickle               | 6.85 us                                                     | 7.26 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                                                 |
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.35 ms: 1.42x faster                                                                 |
| django_template | 28.9 ms                                                     | 22.6 ms: 1.28x faster                                                                 |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                                 |
| genshi_xml      | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 71.6 us: 4.69x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.04 ms: 2.06x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 223 ms: 1.95x faster                                                                  |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                                  |
| async_tree_io            | 1.11 sec                                                    | 585 ms: 1.90x faster                                                                  |
| logging_silent           | 94.6 ns                                                     | 56.6 ns: 1.67x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 382 ms: 1.67x faster                                                                  |
| pylint                   | 350 ms                                                      | 210 ms: 1.67x faster                                                                  |
| json_dumps               | 9.16 ms                                                     | 5.55 ms: 1.65x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 32.0 ms: 1.63x faster                                                                 |
| raytrace                 | 273 ms                                                      | 169 ms: 1.62x faster                                                                  |
| go                       | 139 ms                                                      | 88.4 ms: 1.57x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 784 us: 1.55x faster                                                                  |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                                 |
| asyncio_tcp              | 732 ms                                                      | 478 ms: 1.53x faster                                                                  |
| hexiom                   | 5.74 ms                                                     | 3.78 ms: 1.52x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 179 us: 1.51x faster                                                                  |
| scimark_lu               | 85.8 ms                                                     | 57.1 ms: 1.50x faster                                                                 |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.49x faster                                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 990 us: 1.49x faster                                                                  |
| richards                 | 42.4 ms                                                     | 28.6 ms: 1.48x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 42.0 ms: 1.47x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.45x faster                                                                  |
| mako                     | 9.03 ms                                                     | 6.35 ms: 1.42x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                                 |
| pycparser                | 930 ms                                                      | 684 ms: 1.36x faster                                                                  |
| pyflate                  | 409 ms                                                      | 302 ms: 1.35x faster                                                                  |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.6 ms: 1.34x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                                                 |
| deepcopy_memo            | 28.8 us                                                     | 21.7 us: 1.32x faster                                                                 |
| regex_compile            | 106 ms                                                      | 81.3 ms: 1.30x faster                                                                 |
| tornado_http             | 108 ms                                                      | 84.0 ms: 1.29x faster                                                                 |
| sympy_sum                | 107 ms                                                      | 83.5 ms: 1.28x faster                                                                 |
| django_template          | 28.9 ms                                                     | 22.6 ms: 1.28x faster                                                                 |
| mypy2                    | 555 ms                                                      | 438 ms: 1.27x faster                                                                  |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 85.2 ms: 1.25x faster                                                                 |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 985 ms: 1.24x faster                                                                  |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.24x faster                                                                 |
| sympy_str                | 194 ms                                                      | 159 ms: 1.22x faster                                                                  |
| pprint_safe_repr         | 592 ms                                                      | 485 ms: 1.22x faster                                                                  |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                                |
| chameleon                | 5.79 ms                                                     | 4.76 ms: 1.21x faster                                                                 |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.74 sec: 1.21x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 801 us: 1.20x faster                                                                  |
| float                    | 61.7 ms                                                     | 51.8 ms: 1.19x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 37.3 ms: 1.19x faster                                                                 |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                                  |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                                 |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 33.8 ms: 1.18x faster                                                                 |
| deepcopy                 | 255 us                                                      | 217 us: 1.18x faster                                                                  |
| genshi_xml               | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 270 ms: 1.16x faster                                                                  |
| 2to3                     | 246 ms                                                      | 213 ms: 1.15x faster                                                                  |
| sqlglot_normalize        | 205 ms                                                      | 178 ms: 1.15x faster                                                                  |
| tomli_loads              | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.13x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                                 |
| aiohttp                  | 995 us                                                      | 901 us: 1.10x faster                                                                  |
| create_gc_cycles         | 800 us                                                      | 729 us: 1.10x faster                                                                  |
| unpack_sequence          | 39.6 ns                                                     | 36.6 ns: 1.08x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 62.0 ms: 1.07x faster                                                                 |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.07x faster                                                                 |
| unpickle                 | 9.09 us                                                     | 8.47 us: 1.07x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                 |
| meteor_contest           | 75.9 ms                                                     | 71.5 ms: 1.06x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 75.0 ms: 1.03x faster                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 54.3 ms: 1.02x faster                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                                 |
| logging_format           | 6.76 us                                                     | 6.65 us: 1.02x faster                                                                 |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                                  |
| python_startup           | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                                                 |
| logging_simple           | 6.22 us                                                     | 6.18 us: 1.01x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 77.5 ms: 1.02x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 63.9 ms: 1.03x slower                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.81 ms: 1.03x slower                                                                 |
| unpickle_list            | 2.71 us                                                     | 2.82 us: 1.04x slower                                                                 |
| pickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 1.48 ms: 1.05x slower                                                                 |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                                  |
| pickle_dict              | 17.2 us                                                     | 18.1 us: 1.06x slower                                                                 |
| pickle                   | 6.85 us                                                     | 7.26 us: 1.06x slower                                                                 |
| fannkuch                 | 256 ms                                                      | 274 ms: 1.07x slower                                                                  |
| nbody                    | 71.3 ms                                                     | 77.5 ms: 1.09x slower                                                                 |
| scimark_fft              | 187 ms                                                      | 209 ms: 1.12x slower                                                                  |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.88 ms: 1.24x slower                                                                 |
| thrift                   | 617 us                                                      | 8.20 ms: 13.29x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                          |

Benchmark hidden because not significant (2): json_loads, regex_v8
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240327-3.13.0a5+-8183250/bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x


# Memory

- memory change: unknown