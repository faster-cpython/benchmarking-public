# Results vs. 3.10.4

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 235 ms: 1.04x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.28x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.8 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 199 ms: 2.19x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 521 ms: 2.13x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 251 ms: 2.09x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.01x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.1 ms: 1.42x faster                                                      |
| float          | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.6 ms: 1.21x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.73 ms: 1.60x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 176 us: 1.53x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.35x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.2 ms: 1.04x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| django_template | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 45.6 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                       |
| async_tree_none          | 435 ms                                                      | 199 ms: 2.19x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 521 ms: 2.13x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 251 ms: 2.09x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 15.6 us: 1.85x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 46.1 ms: 1.68x faster                                                      |
| pyflate                  | 409 ms                                                      | 245 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.1 us: 1.63x faster                                                      |
| richards_super           | 52.2 ms                                                     | 32.4 ms: 1.61x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.73 ms: 1.60x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.58x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 39.8 ms: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                                       |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.53x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 176 us: 1.53x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.9 ms: 1.51x faster                                                      |
| pylint                   | 350 ms                                                      | 232 ms: 1.51x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 808 us: 1.50x faster                                                       |
| go                       | 139 ms                                                      | 93.3 ms: 1.49x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.48x faster                                                     |
| richards                 | 42.4 ms                                                     | 28.8 ms: 1.48x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                      |
| deepcopy                 | 255 us                                                      | 179 us: 1.42x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.1 ms: 1.42x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 518 ms: 1.41x faster                                                       |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.35x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.08 ms: 1.31x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 944 ms: 1.29x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 461 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.28x faster                                                      |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 732 ms: 1.27x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.7 ms: 1.27x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.60 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.1 ms: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 505 us: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                     |
| regex_compile            | 106 ms                                                      | 87.6 ms: 1.21x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 807 us: 1.19x faster                                                       |
| fannkuch                 | 256 ms                                                      | 220 ms: 1.16x faster                                                       |
| tornado_http             | 108 ms                                                      | 93.8 ms: 1.15x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                      |
| sympy_sum                | 107 ms                                                      | 94.4 ms: 1.13x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.5 ms: 1.12x faster                                                      |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.7 ms: 1.12x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.17 us: 1.10x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.69 us: 1.09x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 189 ms: 1.09x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.2 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 181 ms: 1.08x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.2 ms: 1.04x faster                                                      |
| 2to3                     | 246 ms                                                      | 235 ms: 1.04x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 316 ms: 1.00x slower                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.6 ms: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 45.6 ms: 1.11x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.45 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 906 us: 1.13x slower                                                       |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 71.1 ms: 1.15x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (1): json
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown