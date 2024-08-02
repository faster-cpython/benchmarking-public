# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 209 ms: 1.18x faster                                                       |
| chameleon      | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 34.1 ms: 1.50x faster                                                      |
| tornado_http   | 108 ms                                                      | 82.5 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 267 ms: 1.97x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 587 ms: 1.89x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.8 ms: 1.26x faster                                                      |
| nbody          | 71.3 ms                                                     | 68.4 ms: 1.04x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.4 ms: 1.37x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.53 ms: 1.66x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 119 us: 1.54x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 177 us: 1.52x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 90.1 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.7 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.88 us: 1.02x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.17 us: 1.05x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.07x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.11 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.20 ms: 1.46x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                                      |
| django_template | 28.9 ms                                                     | 22.0 ms: 1.31x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 32.1 ms: 1.28x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 99.6 us: 3.37x faster                                                      |
| deltablue                | 4.19 ms                                                     | 1.92 ms: 2.19x faster                                                      |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 267 ms: 1.97x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 587 ms: 1.89x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 52.9 ns: 1.79x faster                                                      |
| go                       | 139 ms                                                      | 81.4 ms: 1.71x faster                                                      |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                       |
| generators               | 32.4 ms                                                     | 19.1 ms: 1.70x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.3 ms: 1.67x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.53 ms: 1.66x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| raytrace                 | 273 ms                                                      | 167 ms: 1.63x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.3 ms: 1.61x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 764 us: 1.59x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.68 ms: 1.56x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 55.1 ms: 1.56x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.5 ms: 1.54x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 119 us: 1.54x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 177 us: 1.52x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 973 us: 1.52x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 34.1 ms: 1.50x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.20 ms: 1.46x faster                                                      |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.1 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.50 sec: 1.40x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.7 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.4 ms: 1.37x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 703 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.5 ms: 1.32x faster                                                      |
| django_template          | 28.9 ms                                                     | 22.0 ms: 1.31x faster                                                      |
| tornado_http             | 108 ms                                                      | 82.5 ms: 1.31x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 564 ms: 1.30x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 22.3 us: 1.29x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 32.1 ms: 1.28x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 963 ms: 1.27x faster                                                       |
| float                    | 61.7 ms                                                     | 48.8 ms: 1.26x faster                                                      |
| sympy_sum                | 107 ms                                                      | 84.9 ms: 1.26x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 471 ms: 1.26x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.26x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 493 us: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.1 ms: 1.24x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.24x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| chameleon                | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                      |
| sympy_str                | 194 ms                                                      | 160 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 33.3 ms: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                      |
| 2to3                     | 246 ms                                                      | 209 ms: 1.18x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                                       |
| deepcopy                 | 255 us                                                      | 218 us: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 818 us: 1.17x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 57.4 ms: 1.16x faster                                                      |
| sympy_expand             | 314 ms                                                      | 272 ms: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.13x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.27 us: 1.08x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.1 ms: 1.08x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.82 us: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.57 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.7 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.4 ms: 1.05x faster                                                      |
| nbody                    | 71.3 ms                                                     | 68.4 ms: 1.04x faster                                                      |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.88 us: 1.02x faster                                                      |
| fannkuch                 | 256 ms                                                      | 251 ms: 1.02x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.17 us: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.9 ms: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.09x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| coverage                 | 39.0 ms                                                     | 43.2 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 892 us: 1.12x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.7 ms: 1.12x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.11 us: 1.13x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (5): python_startup, json, json_loads, flaskblogging, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown