# Results vs. 3.10.4

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-amd64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.0 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.2 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 266 ms: 1.98x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 577 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.4 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 82.3 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.7 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.8 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.03 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.92x faster                                                       |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 266 ms: 1.98x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 577 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| pylint                   | 350 ms                                                      | 228 ms: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.7 ns: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| go                       | 139 ms                                                      | 98.5 ms: 1.41x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.4 us: 1.41x faster                                                      |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.39x faster                                                     |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 888 us: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 539 ms: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.3 ms: 1.32x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.5 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.46 ms: 1.29x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.03 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.0 ms: 1.21x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| thrift                   | 617 us                                                      | 530 us: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.16x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.2 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 824 us: 1.16x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.3 ms: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.7 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| scimark_sor              | 106 ms                                                      | 92.2 ms: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 67.6 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.3 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                      |
| float                    | 61.7 ms                                                     | 56.4 ms: 1.09x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 549 ms: 1.08x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.4 ms: 1.07x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                                     |
| 2to3                     | 246 ms                                                      | 231 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 312 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.2 ms: 1.02x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 78.3 ms: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.8 ms: 1.04x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| scimark_fft              | 187 ms                                                      | 205 ms: 1.10x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 68.8 ms: 1.11x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.12x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 909 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| fannkuch                 | 256 ms                                                      | 294 ms: 1.15x slower                                                       |
| nbody                    | 71.3 ms                                                     | 82.3 ms: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (3): pycparser, logging_format, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown