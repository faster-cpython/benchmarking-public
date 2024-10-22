# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                               |
| html5lib       | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                                |
| tornado_http   | 108 ms                                                      | 92.6 ms: 1.17x faster                                                                |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 217 ms: 2.00x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                                 |
| async_tree_io           | 1.11 sec                                                    | 583 ms: 1.90x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                                 |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                                |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                                 |
| nbody          | 71.3 ms                                                     | 85.4 ms: 1.20x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.8 ms: 1.16x faster                                                                |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.20x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.54 sec: 1.09x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.5 ms: 1.04x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.06 ms: 1.28x faster                                                                |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.00x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 583 ms: 1.90x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                                 |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                                 |
| generators               | 32.4 ms                                                     | 21.5 ms: 1.51x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 63.6 ns: 1.49x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                                |
| richards_super           | 52.2 ms                                                     | 35.7 ms: 1.46x faster                                                                |
| raytrace                 | 273 ms                                                      | 192 ms: 1.43x faster                                                                 |
| go                       | 139 ms                                                      | 99.9 ms: 1.39x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                                |
| chaos                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                                |
| asyncio_tcp              | 732 ms                                                      | 534 ms: 1.37x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 897 us: 1.36x faster                                                                 |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                                 |
| richards                 | 42.4 ms                                                     | 31.5 ms: 1.35x faster                                                                |
| comprehensions           | 16.5 us                                                     | 12.4 us: 1.33x faster                                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 65.8 ms: 1.30x faster                                                                |
| mako                     | 9.03 ms                                                     | 7.06 ms: 1.28x faster                                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.65 sec: 1.28x faster                                                               |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                                 |
| pyflate                  | 409 ms                                                      | 328 ms: 1.25x faster                                                                 |
| hexiom                   | 5.74 ms                                                     | 4.62 ms: 1.24x faster                                                                |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                               |
| pycparser                | 930 ms                                                      | 755 ms: 1.23x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.20x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 52.2 ms: 1.20x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 808 us: 1.19x faster                                                                 |
| tornado_http             | 108 ms                                                      | 92.6 ms: 1.17x faster                                                                |
| sympy_sum                | 107 ms                                                      | 91.4 ms: 1.17x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                                                |
| thrift                   | 617 us                                                      | 531 us: 1.16x faster                                                                 |
| regex_compile            | 106 ms                                                      | 91.8 ms: 1.16x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.13x faster                                                                |
| scimark_sor              | 106 ms                                                      | 94.3 ms: 1.13x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                                |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                                 |
| float                    | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                               |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 52.7 ms: 1.09x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.54 sec: 1.09x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 71.8 ms: 1.08x faster                                                                |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                               |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 564 ms: 1.05x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                                |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 65.7 ms: 1.01x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                                |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                                |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                                |
| logging_format           | 6.76 us                                                     | 6.98 us: 1.03x slower                                                                |
| python_startup           | 20.6 ms                                                     | 21.5 ms: 1.04x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.87 ms: 1.05x slower                                                                |
| pathlib                  | 75.7 ms                                                     | 80.6 ms: 1.06x slower                                                                |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.10x slower                                                                |
| scimark_fft              | 187 ms                                                      | 208 ms: 1.11x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 902 us: 1.13x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                                |
| fannkuch                 | 256 ms                                                      | 302 ms: 1.18x slower                                                                 |
| nbody                    | 71.3 ms                                                     | 85.4 ms: 1.20x slower                                                                |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                                |
| telco                    | 3.94 ms                                                     | 5.05 ms: 1.28x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                         |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown