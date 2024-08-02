# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| chameleon      | 5.79 ms                                                     | 5.11 ms: 1.13x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                      |
| tornado_http   | 108 ms                                                      | 84.9 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 272 ms: 1.94x faster                                                       |
| async_tree_none         | 435 ms                                                      | 226 ms: 1.93x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 598 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.5 ms: 1.41x faster                                                      |
| float          | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                      |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.2 ms: 1.22x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 173 us: 1.56x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.47x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.1 ms: 1.08x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.8 ms: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.5 ms: 1.06x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.69 us: 1.05x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.5 us: 1.02x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.90 us: 1.06x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.37 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.7 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 272 ms: 1.94x faster                                                       |
| async_tree_none          | 435 ms                                                      | 226 ms: 1.93x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 598 ms: 1.85x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.33 ms: 1.79x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.1 ms: 1.71x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.0 ns: 1.69x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.57x faster                                                      |
| richards_super           | 52.2 ms                                                     | 33.3 ms: 1.57x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 173 us: 1.56x faster                                                       |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.0 ms: 1.52x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 799 us: 1.52x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 481 ms: 1.52x faster                                                       |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.5 ms: 1.49x faster                                                      |
| pylint                   | 350 ms                                                      | 236 ms: 1.48x faster                                                       |
| go                       | 139 ms                                                      | 93.8 ms: 1.48x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.45x faster                                                     |
| richards                 | 42.4 ms                                                     | 29.5 ms: 1.44x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                      |
| nbody                    | 71.3 ms                                                     | 50.5 ms: 1.41x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.6 us: 1.40x faster                                                      |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 945 ms: 1.29x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 459 ms: 1.29x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.8 ms: 1.28x faster                                                      |
| tornado_http             | 108 ms                                                      | 84.9 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.17 ms: 1.25x faster                                                      |
| pycparser                | 930 ms                                                      | 750 ms: 1.24x faster                                                       |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.65 ms: 1.23x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 69.9 ms: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| regex_compile            | 106 ms                                                      | 87.2 ms: 1.22x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.20x faster                                                     |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.5 ms: 1.16x faster                                                      |
| fannkuch                 | 256 ms                                                      | 222 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 842 us: 1.14x faster                                                       |
| chameleon                | 5.79 ms                                                     | 5.11 ms: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.0 ms: 1.09x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.21 us: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.7 ms: 1.08x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.75 us: 1.08x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.1 ms: 1.08x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                      |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.08x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.8 ms: 1.07x faster                                                      |
| deepcopy                 | 255 us                                                      | 238 us: 1.07x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.07 us: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 91.5 ms: 1.06x faster                                                      |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.69 us: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.5 ms: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.5 us: 1.02x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 78.8 ms: 1.04x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.90 us: 1.06x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.37 us: 1.08x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.7 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 907 us: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.48 ms: 1.14x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 71.3 ms: 1.15x slower                                                      |
| async_generators         | 222 ms                                                      | 257 ms: 1.16x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| coverage                 | 39.0 ms                                                     | 45.8 ms: 1.18x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (2): pidigits, flaskblogging
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown