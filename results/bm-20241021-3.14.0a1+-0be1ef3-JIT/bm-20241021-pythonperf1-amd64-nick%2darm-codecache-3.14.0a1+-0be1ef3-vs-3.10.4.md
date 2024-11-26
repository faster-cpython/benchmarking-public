# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: windows-amd64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.237x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 240 ms: 1.02x faster                                                 |
| docutils       | 1.92 sec                                                    | 1.84 sec: 1.04x faster                                               |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                |
| tornado_http   | 108 ms                                                      | 98.0 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                       | 1.12x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 218 ms: 2.00x faster                                                 |
| async_tree_io           | 1.11 sec                                                    | 566 ms: 1.96x faster                                                 |
| async_tree_memoization  | 526 ms                                                      | 277 ms: 1.90x faster                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                 |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                |
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                       | 1.21x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.7 ms: 1.22x faster                                                |
| regex_dna      | 136 ms                                                      | 122 ms: 1.11x faster                                                 |
| regex_v8       | 15.4 ms                                                     | 15.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                       | 1.08x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                |
| pickle_pure_python   | 270 us                                                      | 199 us: 1.36x faster                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                               |
| unpickle_pure_python | 183 us                                                      | 142 us: 1.29x faster                                                 |
| xml_etree_process    | 44.5 ms                                                     | 36.0 ms: 1.23x faster                                                |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                |
| xml_etree_parse      | 96.8 ms                                                     | 95.5 ms: 1.01x faster                                                |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.2 ms: 1.18x slower                                                |
| python_startup_no_site | 15.5 ms                                                     | 18.5 ms: 1.20x slower                                                |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                |
| django_template | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                |
| genshi_xml      | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                 |
| async_tree_none          | 435 ms                                                      | 218 ms: 2.00x faster                                                 |
| async_tree_io            | 1.11 sec                                                    | 566 ms: 1.96x faster                                                 |
| async_tree_memoization   | 526 ms                                                      | 277 ms: 1.90x faster                                                 |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                |
| deepcopy_memo            | 28.8 us                                                     | 15.8 us: 1.82x faster                                                |
| mako                     | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                |
| logging_silent           | 94.6 ns                                                     | 54.6 ns: 1.73x faster                                                |
| go                       | 139 ms                                                      | 82.2 ms: 1.69x faster                                                |
| scimark_sor              | 106 ms                                                      | 63.7 ms: 1.67x faster                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.1 ms: 1.59x faster                                                |
| scimark_lu               | 85.8 ms                                                     | 54.1 ms: 1.59x faster                                                |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                                |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.52x faster                                                |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                |
| pyflate                  | 409 ms                                                      | 274 ms: 1.49x faster                                                 |
| richards_super           | 52.2 ms                                                     | 35.0 ms: 1.49x faster                                                |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                |
| sqlglot_parse            | 1.22 ms                                                     | 850 us: 1.43x faster                                                 |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                 |
| spectral_norm            | 77.3 ms                                                     | 55.7 ms: 1.39x faster                                                |
| richards                 | 42.4 ms                                                     | 30.8 ms: 1.38x faster                                                |
| pprint_safe_repr         | 592 ms                                                      | 433 ms: 1.37x faster                                                 |
| raytrace                 | 273 ms                                                      | 200 ms: 1.36x faster                                                 |
| pickle_pure_python       | 270 us                                                      | 199 us: 1.36x faster                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 906 ms: 1.35x faster                                                 |
| nbody                    | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                |
| hexiom                   | 5.74 ms                                                     | 4.28 ms: 1.34x faster                                                |
| pycparser                | 930 ms                                                      | 696 ms: 1.34x faster                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                |
| pylint                   | 350 ms                                                      | 268 ms: 1.31x faster                                                 |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                |
| unpickle_pure_python     | 183 us                                                      | 142 us: 1.29x faster                                                 |
| dulwich_log              | 50.5 ms                                                     | 39.9 ms: 1.27x faster                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.21 ms: 1.24x faster                                                |
| xml_etree_process        | 44.5 ms                                                     | 36.0 ms: 1.23x faster                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                |
| regex_compile            | 106 ms                                                      | 86.7 ms: 1.22x faster                                                |
| fannkuch                 | 256 ms                                                      | 212 ms: 1.21x faster                                                 |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.20x faster                                                 |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                 |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.17x faster                                               |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                |
| django_template          | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                |
| bench_thread_pool        | 958 us                                                      | 846 us: 1.13x faster                                                 |
| regex_dna                | 136 ms                                                      | 122 ms: 1.11x faster                                                 |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                |
| tornado_http             | 108 ms                                                      | 98.0 ms: 1.11x faster                                                |
| sympy_sum                | 107 ms                                                      | 98.0 ms: 1.09x faster                                                |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                 |
| genshi_xml               | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                |
| nqueens                  | 66.6 ms                                                     | 62.7 ms: 1.06x faster                                                |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                 |
| meteor_contest           | 75.9 ms                                                     | 71.9 ms: 1.06x faster                                                |
| logging_format           | 6.76 us                                                     | 6.44 us: 1.05x faster                                                |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                 |
| docutils                 | 1.92 sec                                                    | 1.84 sec: 1.04x faster                                               |
| logging_simple           | 6.22 us                                                     | 6.05 us: 1.03x faster                                                |
| 2to3                     | 246 ms                                                      | 240 ms: 1.02x faster                                                 |
| sympy_integrate          | 15.3 ms                                                     | 15.0 ms: 1.02x faster                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                |
| xml_etree_parse          | 96.8 ms                                                     | 95.5 ms: 1.01x faster                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 39.4 ms: 1.01x faster                                                |
| pidigits                 | 149 ms                                                      | 148 ms: 1.00x faster                                                 |
| regex_v8                 | 15.4 ms                                                     | 15.5 ms: 1.01x slower                                                |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                |
| pathlib                  | 75.7 ms                                                     | 80.3 ms: 1.06x slower                                                |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                                |
| python_startup           | 20.6 ms                                                     | 24.2 ms: 1.18x slower                                                |
| async_generators         | 222 ms                                                      | 264 ms: 1.19x slower                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 18.5 ms: 1.20x slower                                                |
| coverage                 | 39.0 ms                                                     | 47.8 ms: 1.23x slower                                                |
| gc_traversal             | 1.41 ms                                                     | 1.94 ms: 1.38x slower                                                |
| bench_mp_pool            | 62.0 ms                                                     | 89.1 ms: 1.44x slower                                                |
| create_gc_cycles         | 800 us                                                      | 1.39 ms: 1.74x slower                                                |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.237x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown