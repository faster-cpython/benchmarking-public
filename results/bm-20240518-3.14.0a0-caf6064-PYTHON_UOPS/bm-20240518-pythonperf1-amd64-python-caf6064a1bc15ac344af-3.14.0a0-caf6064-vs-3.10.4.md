# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| chameleon      | 5.79 ms                                                     | 5.12 ms: 1.13x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                      |
| tornado_http   | 108 ms                                                      | 87.0 ms: 1.25x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                                       |
| async_tree_none         | 435 ms                                                      | 231 ms: 1.88x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 612 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 400 ms: 1.59x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.79x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 53.6 ms: 1.15x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 75.0 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_compile  | 106 ms                                                      | 106 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.81 ms: 1.58x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.19x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.5 ms: 1.12x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.58 us: 1.06x faster                                                      |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.6 ms: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.81 us: 1.03x slower                                                      |
| pickle               | 6.85 us                                                     | 7.11 us: 1.04x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.93 us: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

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
| mako            | 9.03 ms                                                     | 7.35 ms: 1.23x faster                                                      |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.91x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                                       |
| async_tree_none          | 435 ms                                                      | 231 ms: 1.88x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 612 ms: 1.81x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.0 ms: 1.63x faster                                                      |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.59 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 400 ms: 1.59x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.81 ms: 1.58x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.54x faster                                                       |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| pylint                   | 350 ms                                                      | 232 ms: 1.51x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.2 ms: 1.50x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.50 sec: 1.41x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 68.2 ns: 1.39x faster                                                      |
| go                       | 139 ms                                                      | 100 ms: 1.38x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 881 us: 1.38x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.2 ms: 1.27x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                                     |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                                       |
| comprehensions           | 16.5 us                                                     | 13.1 us: 1.26x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                      |
| tornado_http             | 108 ms                                                      | 87.0 ms: 1.25x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.3 ms: 1.23x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.35 ms: 1.23x faster                                                      |
| thrift                   | 617 us                                                      | 511 us: 1.21x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.6 ms: 1.20x faster                                                      |
| pycparser                | 930 ms                                                      | 777 ms: 1.20x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.18x faster                                                      |
| float                    | 61.7 ms                                                     | 53.6 ms: 1.15x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 839 us: 1.14x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                     |
| chameleon                | 5.79 ms                                                     | 5.12 ms: 1.13x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 39.5 ms: 1.12x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 530 ms: 1.12x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 77.2 ms: 1.11x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.23 ms: 1.10x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| sympy_sum                | 107 ms                                                      | 99.3 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.58 us: 1.06x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.5 ms: 1.05x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 74.5 ms: 1.04x faster                                                      |
| python_startup           | 20.6 ms                                                     | 20.0 ms: 1.03x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 38.6 ms: 1.03x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 28.0 us: 1.03x faster                                                      |
| deepcopy                 | 255 us                                                      | 249 us: 1.03x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.15 us: 1.03x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                      |
| regex_compile            | 106 ms                                                      | 106 ms: 1.00x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.7 ms: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.6 ms: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.81 us: 1.03x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.11 us: 1.04x slower                                                      |
| scimark_fft              | 187 ms                                                      | 195 ms: 1.04x slower                                                       |
| fannkuch                 | 256 ms                                                      | 267 ms: 1.05x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.2 ms: 1.05x slower                                                      |
| nbody                    | 71.3 ms                                                     | 75.0 ms: 1.05x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.93 us: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                      |
| sympy_expand             | 314 ms                                                      | 337 ms: 1.07x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 67.6 ms: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 245 ms: 1.10x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.01 ms: 1.11x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 912 us: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 44.8 ms: 1.15x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.91 ms: 1.25x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (6): nqueens, flaskblogging, sympy_str, logging_simple, xml_etree_iterparse, regex_v8
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown