# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| chameleon      | 5.79 ms                                                     | 4.99 ms: 1.16x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                      |
| tornado_http   | 108 ms                                                      | 85.4 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 226 ms: 1.93x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 275 ms: 1.92x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 589 ms: 1.88x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.9 ms: 1.43x faster                                                      |
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| Geometric mean | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.6 ms: 1.22x faster                                                      |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.65 ms: 1.62x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 172 us: 1.56x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 124 us: 1.47x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.9 ms: 1.08x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.6 ms: 1.06x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.69 us: 1.05x faster                                                      |
| pickle_dict          | 17.2 us                                                     | 17.5 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.88 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.35 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.94 ms: 1.83x faster                                                      |
| django_template | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.8 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                       |
| async_tree_none          | 435 ms                                                      | 226 ms: 1.93x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 275 ms: 1.92x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 589 ms: 1.88x faster                                                       |
| mako                     | 9.03 ms                                                     | 4.94 ms: 1.83x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.32 ms: 1.80x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 54.5 ns: 1.74x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 44.9 ms: 1.72x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.65 ms: 1.62x faster                                                      |
| richards_super           | 52.2 ms                                                     | 32.3 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.4 ms: 1.56x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 172 us: 1.56x faster                                                       |
| pyflate                  | 409 ms                                                      | 262 ms: 1.56x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.8 ms: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 803 us: 1.51x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.9 ms: 1.51x faster                                                      |
| go                       | 139 ms                                                      | 92.6 ms: 1.50x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.5 ms: 1.49x faster                                                      |
| generators               | 32.4 ms                                                     | 22.0 ms: 1.47x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 124 us: 1.47x faster                                                       |
| pylint                   | 350 ms                                                      | 238 ms: 1.47x faster                                                       |
| nbody                    | 71.3 ms                                                     | 49.9 ms: 1.43x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.5 us: 1.41x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.52 sec: 1.39x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 545 ms: 1.34x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 924 ms: 1.32x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 450 ms: 1.32x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.6 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 67.5 ms: 1.27x faster                                                      |
| tornado_http             | 108 ms                                                      | 85.4 ms: 1.27x faster                                                      |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.65 ms: 1.24x faster                                                      |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                      |
| regex_compile            | 106 ms                                                      | 86.6 ms: 1.22x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.99 ms: 1.16x faster                                                      |
| thrift                   | 617 us                                                      | 533 us: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 832 us: 1.15x faster                                                       |
| fannkuch                 | 256 ms                                                      | 223 ms: 1.15x faster                                                       |
| sympy_sum                | 107 ms                                                      | 93.6 ms: 1.14x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| deepcopy                 | 255 us                                                      | 233 us: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.1 ms: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                     |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.9 ms: 1.08x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.04 us: 1.08x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 37.1 ms: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.31 us: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.88 us: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 91.6 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.69 us: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.2 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                       |
| pickle_dict              | 17.2 us                                                     | 17.5 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.6 ms: 1.05x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.88 us: 1.06x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.35 us: 1.07x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.8 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 906 us: 1.13x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.5 ms: 1.14x slower                                                      |
| coverage                 | 39.0 ms                                                     | 45.1 ms: 1.16x slower                                                      |
| async_generators         | 222 ms                                                      | 259 ms: 1.17x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.63 ms: 1.18x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (4): regex_v8, flaskblogging, pidigits, pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown