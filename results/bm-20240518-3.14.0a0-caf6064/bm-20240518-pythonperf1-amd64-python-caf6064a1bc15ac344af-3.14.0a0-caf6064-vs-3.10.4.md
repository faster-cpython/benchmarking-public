# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 207 ms: 1.19x faster                                                       |
| chameleon      | 5.79 ms                                                     | 4.79 ms: 1.21x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| html5lib       | 51.0 ms                                                     | 35.6 ms: 1.43x faster                                                      |
| tornado_http   | 108 ms                                                      | 82.3 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 215 ms: 2.03x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 260 ms: 2.02x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 578 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.2 ms: 1.20x faster                                                      |
| nbody          | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.9 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 176 us: 1.53x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.46x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.56 us: 1.06x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.81 us: 1.04x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.2 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.25 us: 1.06x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.0 ms: 1.03x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.53 ms: 1.38x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 14.8 ms: 1.34x faster                                                      |
| django_template | 28.9 ms                                                     | 21.8 ms: 1.33x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 31.5 ms: 1.30x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.34x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 99.7 us: 3.37x faster                                                      |
| deltablue                | 4.19 ms                                                     | 1.94 ms: 2.16x faster                                                      |
| async_tree_none          | 435 ms                                                      | 215 ms: 2.03x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 260 ms: 2.02x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 578 ms: 1.92x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 53.6 ns: 1.77x faster                                                      |
| richards_super           | 52.2 ms                                                     | 29.8 ms: 1.75x faster                                                      |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                       |
| raytrace                 | 273 ms                                                      | 161 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| go                       | 139 ms                                                      | 84.3 ms: 1.65x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 754 us: 1.61x faster                                                       |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.60x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.7 ms: 1.59x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.58x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 476 ms: 1.54x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.8 ms: 1.54x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 963 us: 1.53x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 176 us: 1.53x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.77 ms: 1.52x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.46x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.6 ms: 1.43x faster                                                      |
| pyflate                  | 409 ms                                                      | 286 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.49 sec: 1.41x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.1 ms: 1.39x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.53 ms: 1.38x faster                                                      |
| scimark_sor              | 106 ms                                                      | 77.3 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.9 ms: 1.36x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.5 ms: 1.34x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 14.8 ms: 1.34x faster                                                      |
| django_template          | 28.9 ms                                                     | 21.8 ms: 1.33x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.35 sec: 1.32x faster                                                     |
| tornado_http             | 108 ms                                                      | 82.3 ms: 1.32x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 31.5 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 723 ms: 1.29x faster                                                       |
| sympy_sum                | 107 ms                                                      | 83.9 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 489 us: 1.26x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 23.0 us: 1.25x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 989 ms: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 485 ms: 1.22x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 32.8 ms: 1.22x faster                                                      |
| chameleon                | 5.79 ms                                                     | 4.79 ms: 1.21x faster                                                      |
| float                    | 61.7 ms                                                     | 51.2 ms: 1.20x faster                                                      |
| sympy_str                | 194 ms                                                      | 162 ms: 1.20x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 804 us: 1.19x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 173 ms: 1.19x faster                                                       |
| 2to3                     | 246 ms                                                      | 207 ms: 1.19x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 65.1 ms: 1.19x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 57.1 ms: 1.17x faster                                                      |
| deepcopy                 | 255 us                                                      | 219 us: 1.17x faster                                                       |
| sympy_expand             | 314 ms                                                      | 270 ms: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.08 us: 1.11x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.67 us: 1.10x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.54 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.56 us: 1.06x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                      |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                      |
| python_startup           | 20.6 ms                                                     | 20.0 ms: 1.03x faster                                                      |
| nbody                    | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                      |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.81 us: 1.04x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.2 ms: 1.05x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.2 us: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.25 us: 1.06x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.0 ms: 1.06x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 888 us: 1.11x slower                                                       |
| coverage                 | 39.0 ms                                                     | 44.5 ms: 1.14x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.68 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (2): flaskblogging, fannkuch
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown