# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.6 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 208 ms: 2.10x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 255 ms: 2.07x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 572 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 80.9 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.28x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.7 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.5 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.92 ms: 1.30x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                      |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 208 ms: 2.10x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 255 ms: 2.07x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 572 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                      |
| go                       | 139 ms                                                      | 84.5 ms: 1.64x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| generators               | 32.4 ms                                                     | 20.8 ms: 1.56x faster                                                      |
| pylint                   | 350 ms                                                      | 228 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.7 ns: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.1 ms: 1.45x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.9 us: 1.45x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                      |
| raytrace                 | 273 ms                                                      | 191 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 532 ms: 1.38x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 884 us: 1.37x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 62.6 ms: 1.37x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.56 sec: 1.36x faster                                                     |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                       |
| richards                 | 42.4 ms                                                     | 31.6 ms: 1.34x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.32 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.31x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.92 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 323 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                      |
| pycparser                | 930 ms                                                      | 744 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                       |
| scimark_sor              | 106 ms                                                      | 87.7 ms: 1.21x faster                                                      |
| sympy_sum                | 107 ms                                                      | 89.9 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.8 ms: 1.18x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 816 us: 1.17x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.2 ms: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.6 ms: 1.16x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 67.1 ms: 1.15x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.56 sec: 1.14x faster                                                     |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 35.9 ms: 1.11x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| float                    | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 543 ms: 1.09x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.09x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 190 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.0 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 94.7 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.70 ms: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.0 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.38 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 78.8 ms: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.5 ms: 1.05x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 68.5 ms: 1.10x slower                                                      |
| scimark_fft              | 187 ms                                                      | 207 ms: 1.11x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                       |
| fannkuch                 | 256 ms                                                      | 288 ms: 1.13x slower                                                       |
| nbody                    | 71.3 ms                                                     | 80.9 ms: 1.14x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 908 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.03 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): json
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown