# Results vs. 3.10.4

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-amd64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| tornado_http   | 108 ms                                                      | 82.1 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.01x faster                                                       |
| async_tree_none         | 435 ms                                                      | 217 ms: 2.01x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 569 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 387 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 57.4 ms: 1.07x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 82.2 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.1 ms: 1.20x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.00 ms: 1.53x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 156 us: 1.18x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.0 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.63 sec: 1.03x faster                                                     |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.01x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.7 ms: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| mako            | 9.03 ms                                                     | 7.85 ms: 1.15x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.01x faster                                                       |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.01x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 569 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 387 ms: 1.65x faster                                                       |
| pylint                   | 350 ms                                                      | 213 ms: 1.64x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.00 ms: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.7 ms: 1.51x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 491 ms: 1.49x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 64.6 ns: 1.47x faster                                                      |
| go                       | 139 ms                                                      | 95.1 ms: 1.46x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                                     |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                       |
| generators               | 32.4 ms                                                     | 23.6 ms: 1.37x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.9 ms: 1.37x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.37x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 902 us: 1.35x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.6 us: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| tornado_http             | 108 ms                                                      | 82.1 ms: 1.32x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.0 ms: 1.28x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.50 ms: 1.28x faster                                                      |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 768 us: 1.25x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                     |
| regex_compile            | 106 ms                                                      | 88.1 ms: 1.20x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.9 ms: 1.20x faster                                                      |
| pycparser                | 930 ms                                                      | 781 ms: 1.19x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 52.6 ms: 1.19x faster                                                      |
| scimark_sor              | 106 ms                                                      | 89.4 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 156 us: 1.18x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                      |
| thrift                   | 617 us                                                      | 536 us: 1.15x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.85 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.0 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.6 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.07x faster                                                       |
| float                    | 61.7 ms                                                     | 57.4 ms: 1.07x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 556 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 42.0 ms: 1.06x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 73.2 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.63 sec: 1.03x faster                                                     |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.72 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.28 us: 1.01x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.4 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.7 ms: 1.08x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 895 us: 1.12x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.07 ms: 1.13x slower                                                      |
| scimark_fft              | 187 ms                                                      | 215 ms: 1.15x slower                                                       |
| nbody                    | 71.3 ms                                                     | 82.2 ms: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 45.4 ms: 1.16x slower                                                      |
| fannkuch                 | 256 ms                                                      | 303 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.86 ms: 1.23x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                               |

Benchmark hidden because not significant (4): json, pathlib, python_startup, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown