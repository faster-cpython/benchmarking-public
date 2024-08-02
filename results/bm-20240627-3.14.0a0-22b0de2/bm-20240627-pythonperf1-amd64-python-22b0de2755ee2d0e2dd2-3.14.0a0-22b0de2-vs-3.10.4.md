# Results vs. 3.10.4

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-amd64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| tornado_http   | 108 ms                                                      | 82.7 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_none         | 435 ms                                                      | 218 ms: 2.00x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 570 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 387 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 58.3 ms: 1.06x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 83.8 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.1 ms: 1.20x faster                                                      |
| regex_dna      | 136 ms                                                      | 127 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 16.5 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.00 ms: 1.53x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 161 us: 1.14x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.7 ms: 1.04x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| mako            | 9.03 ms                                                     | 7.87 ms: 1.15x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 218 ms: 2.00x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 570 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 212 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 387 ms: 1.65x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.00 ms: 1.53x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 483 ms: 1.52x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.7 ms: 1.51x faster                                                      |
| raytrace                 | 273 ms                                                      | 186 ms: 1.47x faster                                                       |
| go                       | 139 ms                                                      | 95.8 ms: 1.45x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 66.3 ns: 1.43x faster                                                      |
| generators               | 32.4 ms                                                     | 23.3 ms: 1.39x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                      |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                       |
| richards                 | 42.4 ms                                                     | 31.1 ms: 1.36x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.57 sec: 1.35x faster                                                     |
| sqlglot_parse            | 1.22 ms                                                     | 911 us: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.8 us: 1.32x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.5 us: 1.32x faster                                                      |
| tornado_http             | 108 ms                                                      | 82.7 ms: 1.31x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 67.5 ms: 1.27x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.56 ms: 1.26x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.42 sec: 1.25x faster                                                     |
| pyflate                  | 409 ms                                                      | 328 ms: 1.25x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 771 us: 1.24x faster                                                       |
| pycparser                | 930 ms                                                      | 761 ms: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 88.8 ms: 1.21x faster                                                      |
| regex_compile            | 106 ms                                                      | 88.1 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 53.5 ms: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| thrift                   | 617 us                                                      | 528 us: 1.17x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.0 ms: 1.15x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.87 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 161 us: 1.14x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.2 ms: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 173 ms: 1.13x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.9 ms: 1.10x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                      |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| regex_dna                | 136 ms                                                      | 127 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.06x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                     |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                      |
| float                    | 61.7 ms                                                     | 58.3 ms: 1.06x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 564 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 74.7 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 64.8 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.7 ms: 1.04x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.0 ms: 1.06x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 16.5 ms: 1.07x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 902 us: 1.13x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.09 ms: 1.13x slower                                                      |
| async_generators         | 222 ms                                                      | 255 ms: 1.15x slower                                                       |
| scimark_fft              | 187 ms                                                      | 220 ms: 1.17x slower                                                       |
| nbody                    | 71.3 ms                                                     | 83.8 ms: 1.18x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.4 ms: 1.19x slower                                                      |
| fannkuch                 | 256 ms                                                      | 311 ms: 1.22x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.03 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (3): pathlib, logging_format, python_startup
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown