# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-amd64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.235x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                     |
| docutils       | 1.92 sec                                                    | 1.81 sec: 1.06x faster                                                   |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                    |
| tornado_http   | 108 ms                                                      | 98.5 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                       | 1.13x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                     |
| async_tree_io           | 1.11 sec                                                    | 565 ms: 1.96x faster                                                     |
| async_tree_memoization  | 526 ms                                                      | 283 ms: 1.86x faster                                                     |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.65x faster                                                     |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                    |
| float          | 61.7 ms                                                     | 48.0 ms: 1.28x faster                                                    |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.20x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.6 ms: 1.28x faster                                                    |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                     |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                    |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                       | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                    |
| pickle_pure_python   | 270 us                                                      | 197 us: 1.37x faster                                                     |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                   |
| unpickle_pure_python | 183 us                                                      | 141 us: 1.30x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                    |
| xml_etree_generate   | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                    |
| xml_etree_parse      | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                    |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                    |
| python_startup         | 20.6 ms                                                     | 24.2 ms: 1.18x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.09 ms: 1.77x faster                                                    |
| django_template | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                    |
| genshi_text     | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                    |
| genshi_xml      | 41.0 ms                                                     | 40.3 ms: 1.02x faster                                                    |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.92x faster                                                     |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                     |
| async_tree_io            | 1.11 sec                                                    | 565 ms: 1.96x faster                                                     |
| async_tree_memoization   | 526 ms                                                      | 283 ms: 1.86x faster                                                     |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                                    |
| deepcopy_memo            | 28.8 us                                                     | 16.2 us: 1.78x faster                                                    |
| mako                     | 9.03 ms                                                     | 5.09 ms: 1.77x faster                                                    |
| logging_silent           | 94.6 ns                                                     | 54.5 ns: 1.74x faster                                                    |
| go                       | 139 ms                                                      | 82.4 ms: 1.69x faster                                                    |
| scimark_sor              | 106 ms                                                      | 63.1 ms: 1.68x faster                                                    |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.65x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 53.3 ms: 1.61x faster                                                    |
| scimark_monte_carlo      | 57.3 ms                                                     | 35.8 ms: 1.60x faster                                                    |
| crypto_pyaes             | 62.5 ms                                                     | 39.7 ms: 1.57x faster                                                    |
| chaos                    | 61.7 ms                                                     | 39.7 ms: 1.55x faster                                                    |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                    |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                                    |
| pyflate                  | 409 ms                                                      | 276 ms: 1.48x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                    |
| spectral_norm            | 77.3 ms                                                     | 53.2 ms: 1.45x faster                                                    |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                    |
| sqlglot_parse            | 1.22 ms                                                     | 858 us: 1.42x faster                                                     |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 197 us: 1.37x faster                                                     |
| pylint                   | 350 ms                                                      | 258 ms: 1.36x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 900 ms: 1.35x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.25 ms: 1.35x faster                                                    |
| nbody                    | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                    |
| pprint_safe_repr         | 592 ms                                                      | 442 ms: 1.34x faster                                                     |
| raytrace                 | 273 ms                                                      | 206 ms: 1.33x faster                                                     |
| richards                 | 42.4 ms                                                     | 32.0 ms: 1.32x faster                                                    |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                    |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                                    |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                   |
| unpickle_pure_python     | 183 us                                                      | 141 us: 1.30x faster                                                     |
| float                    | 61.7 ms                                                     | 48.0 ms: 1.28x faster                                                    |
| regex_compile            | 106 ms                                                      | 82.6 ms: 1.28x faster                                                    |
| xml_etree_process        | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                    |
| dulwich_log              | 50.5 ms                                                     | 40.3 ms: 1.25x faster                                                    |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.24 ms: 1.22x faster                                                    |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.21x faster                                                   |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                     |
| fannkuch                 | 256 ms                                                      | 213 ms: 1.20x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                    |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                     |
| thrift                   | 617 us                                                      | 531 us: 1.16x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                    |
| bench_thread_pool        | 958 us                                                      | 837 us: 1.14x faster                                                     |
| sympy_sum                | 107 ms                                                      | 95.5 ms: 1.12x faster                                                    |
| xml_etree_generate       | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                    |
| tornado_http             | 108 ms                                                      | 98.5 ms: 1.10x faster                                                    |
| django_template          | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                    |
| meteor_contest           | 75.9 ms                                                     | 70.0 ms: 1.08x faster                                                    |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                    |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                    |
| nqueens                  | 66.6 ms                                                     | 62.7 ms: 1.06x faster                                                    |
| docutils                 | 1.92 sec                                                    | 1.81 sec: 1.06x faster                                                   |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                    |
| sympy_integrate          | 15.3 ms                                                     | 14.8 ms: 1.03x faster                                                    |
| xml_etree_parse          | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                    |
| logging_format           | 6.76 us                                                     | 6.58 us: 1.03x faster                                                    |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                    |
| sqlglot_optimize         | 39.8 ms                                                     | 38.8 ms: 1.03x faster                                                    |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                    |
| logging_simple           | 6.22 us                                                     | 6.08 us: 1.02x faster                                                    |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 40.3 ms: 1.02x faster                                                    |
| sqlglot_normalize        | 205 ms                                                      | 202 ms: 1.02x faster                                                     |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                     |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                    |
| pathlib                  | 75.7 ms                                                     | 81.1 ms: 1.07x slower                                                    |
| telco                    | 3.94 ms                                                     | 4.51 ms: 1.14x slower                                                    |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                    |
| python_startup           | 20.6 ms                                                     | 24.2 ms: 1.18x slower                                                    |
| async_generators         | 222 ms                                                      | 267 ms: 1.21x slower                                                     |
| coverage                 | 39.0 ms                                                     | 49.5 ms: 1.27x slower                                                    |
| gc_traversal             | 1.41 ms                                                     | 1.95 ms: 1.39x slower                                                    |
| bench_mp_pool            | 62.0 ms                                                     | 87.2 ms: 1.40x slower                                                    |
| create_gc_cycles         | 800 us                                                      | 1.41 ms: 1.76x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                             |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.235x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown