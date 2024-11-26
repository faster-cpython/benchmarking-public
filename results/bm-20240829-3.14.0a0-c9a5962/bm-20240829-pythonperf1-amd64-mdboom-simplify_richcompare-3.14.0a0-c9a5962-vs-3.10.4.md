# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.160x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.7 ms: 1.29x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 211 ms: 2.06x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 582 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.89x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 58.6 ms: 1.05x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.02x slower                                                       |
| nbody          | 71.3 ms                                                     | 87.8 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 92.4 ms: 1.15x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.32 ms: 1.45x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.4 ms: 1.09x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.12 ms: 1.27x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                       |
| async_tree_none          | 435 ms                                                      | 211 ms: 2.06x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 582 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| generators               | 32.4 ms                                                     | 20.5 ms: 1.58x faster                                                      |
| go                       | 139 ms                                                      | 88.1 ms: 1.58x faster                                                      |
| pylint                   | 350 ms                                                      | 227 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 64.8 ns: 1.46x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.32 ms: 1.45x faster                                                      |
| richards_super           | 52.2 ms                                                     | 37.2 ms: 1.41x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                      |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 536 ms: 1.36x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                      |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.2 us: 1.36x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 910 us: 1.34x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.60 sec: 1.32x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 65.3 ms: 1.31x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.5 ms: 1.30x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.30x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.7 ms: 1.29x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.3 ms: 1.27x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.52 ms: 1.27x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.12 ms: 1.27x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                       |
| pyflate                  | 409 ms                                                      | 327 ms: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 521 us: 1.19x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.18x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 818 us: 1.17x faster                                                       |
| tornado_http             | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                      |
| regex_compile            | 106 ms                                                      | 92.4 ms: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                      |
| scimark_sor              | 106 ms                                                      | 93.8 ms: 1.13x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.6 ms: 1.11x faster                                                      |
| pycparser                | 930 ms                                                      | 839 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                      |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 72.2 ms: 1.07x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                       |
| float                    | 61.7 ms                                                     | 58.6 ms: 1.05x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 569 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 64.7 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.02x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.48 us: 1.04x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 79.5 ms: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.6 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.92 ms: 1.07x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.4 ms: 1.09x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.0 ms: 1.11x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 251 ms: 1.13x slower                                                       |
| scimark_fft              | 187 ms                                                      | 214 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 919 us: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 300 ms: 1.17x slower                                                       |
| nbody                    | 71.3 ms                                                     | 87.8 ms: 1.23x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.9 ms: 1.28x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.20 ms: 1.32x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.160x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown