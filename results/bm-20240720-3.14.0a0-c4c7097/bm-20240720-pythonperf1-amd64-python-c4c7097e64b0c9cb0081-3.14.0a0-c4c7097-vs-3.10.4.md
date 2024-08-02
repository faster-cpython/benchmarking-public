# Results vs. 3.10.4

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                      |
| tornado_http   | 108 ms                                                      | 91.3 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_none         | 435 ms                                                      | 216 ms: 2.01x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 556 ms: 1.99x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.4 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| nbody          | 71.3 ms                                                     | 77.3 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.8 ms: 1.22x faster                                                      |
| regex_dna      | 136 ms                                                      | 126 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.92 ms: 1.55x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 199 us: 1.35x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 141 us: 1.30x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.51 sec: 1.11x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.4 ms: 1.04x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.11 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 23.0 ms: 1.26x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.20x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.07 ms: 2.02x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 216 ms: 2.01x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 556 ms: 1.99x faster                                                       |
| pylint                   | 350 ms                                                      | 209 ms: 1.68x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.9 ns: 1.63x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| raytrace                 | 273 ms                                                      | 169 ms: 1.62x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.92 ms: 1.55x faster                                                      |
| generators               | 32.4 ms                                                     | 20.9 ms: 1.55x faster                                                      |
| go                       | 139 ms                                                      | 91.0 ms: 1.53x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.6 us: 1.47x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.9 ms: 1.47x faster                                                      |
| deepcopy                 | 255 us                                                      | 175 us: 1.46x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 847 us: 1.43x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.3 ms: 1.42x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.05 ms: 1.40x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 524 ms: 1.40x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.40x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 199 us: 1.35x faster                                                       |
| pyflate                  | 409 ms                                                      | 304 ms: 1.34x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 141 us: 1.30x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.64 sec: 1.28x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 48.9 ms: 1.28x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.11 ms: 1.27x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.0 ms: 1.26x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.8 ms: 1.22x faster                                                      |
| regex_compile            | 106 ms                                                      | 86.8 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| pycparser                | 930 ms                                                      | 766 ms: 1.21x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| sympy_sum                | 107 ms                                                      | 89.0 ms: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 514 us: 1.20x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 799 us: 1.20x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.9 ms: 1.20x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                      |
| tornado_http             | 108 ms                                                      | 91.3 ms: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.17x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 34.2 ms: 1.16x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 180 ms: 1.14x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 524 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| float                    | 61.7 ms                                                     | 55.4 ms: 1.11x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 69.5 ms: 1.11x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.51 sec: 1.11x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| regex_dna                | 136 ms                                                      | 126 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 298 ms: 1.06x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.48 us: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.99 us: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.4 ms: 1.04x slower                                                      |
| scimark_fft              | 187 ms                                                      | 198 ms: 1.06x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 80.3 ms: 1.06x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.1 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 240 ms: 1.08x slower                                                       |
| nbody                    | 71.3 ms                                                     | 77.3 ms: 1.08x slower                                                      |
| fannkuch                 | 256 ms                                                      | 280 ms: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 903 us: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                      |
| coverage                 | 39.0 ms                                                     | 79.8 ms: 2.05x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                               |

Benchmark hidden because not significant (4): json, xml_etree_iterparse, scimark_sparse_mat_mult, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown