# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-amd64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.07x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                               |
| html5lib       | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                                                |
| tornado_http   | 108 ms                                                      | 92.6 ms: 1.17x faster                                                                |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 218 ms: 1.99x faster                                                                 |
| async_tree_io           | 1.11 sec                                                    | 583 ms: 1.90x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 387 ms: 1.65x faster                                                                 |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.8 ms: 1.09x faster                                                                |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                                 |
| nbody          | 71.3 ms                                                     | 83.5 ms: 1.17x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                                 |
| regex_compile  | 106 ms                                                      | 90.4 ms: 1.17x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                                |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 146 us: 1.25x faster                                                                 |
| xml_etree_process    | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                               |
| xml_etree_parse      | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.8 ms: 1.01x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.97 ms: 1.30x faster                                                                |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.93x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 218 ms: 1.99x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 583 ms: 1.90x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 387 ms: 1.65x faster                                                                 |
| generators               | 32.4 ms                                                     | 20.8 ms: 1.56x faster                                                                |
| pylint                   | 350 ms                                                      | 226 ms: 1.55x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 62.7 ns: 1.51x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                                |
| richards_super           | 52.2 ms                                                     | 36.5 ms: 1.43x faster                                                                |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.42x faster                                                                |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                                 |
| go                       | 139 ms                                                      | 99.2 ms: 1.40x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 61.6 ms: 1.39x faster                                                                |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                                |
| sqlglot_parse            | 1.22 ms                                                     | 890 us: 1.37x faster                                                                 |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                                 |
| asyncio_tcp              | 732 ms                                                      | 540 ms: 1.35x faster                                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.59 sec: 1.33x faster                                                               |
| hexiom                   | 5.74 ms                                                     | 4.33 ms: 1.33x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.31x faster                                                                |
| richards                 | 42.4 ms                                                     | 32.5 ms: 1.31x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.97 ms: 1.30x faster                                                                |
| pyflate                  | 409 ms                                                      | 316 ms: 1.29x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 146 us: 1.25x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                                                |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                               |
| scimark_sor              | 106 ms                                                      | 90.2 ms: 1.18x faster                                                                |
| thrift                   | 617 us                                                      | 526 us: 1.17x faster                                                                 |
| sympy_sum                | 107 ms                                                      | 91.2 ms: 1.17x faster                                                                |
| regex_compile            | 106 ms                                                      | 90.4 ms: 1.17x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                                |
| tornado_http             | 108 ms                                                      | 92.6 ms: 1.17x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 43.2 ms: 1.17x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.0 ms: 1.17x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 824 us: 1.16x faster                                                                 |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 68.3 ms: 1.13x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                               |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                                |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                                |
| float                    | 61.7 ms                                                     | 56.8 ms: 1.09x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 551 ms: 1.07x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                                 |
| 2to3                     | 246 ms                                                      | 231 ms: 1.07x faster                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 63.1 ms: 1.06x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                                |
| pycparser                | 930 ms                                                      | 883 ms: 1.05x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.03x faster                                                                |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.8 ms: 1.01x slower                                                                |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                                 |
| logging_simple           | 6.22 us                                                     | 6.34 us: 1.02x slower                                                                |
| meteor_contest           | 75.9 ms                                                     | 78.5 ms: 1.03x slower                                                                |
| pathlib                  | 75.7 ms                                                     | 78.9 ms: 1.04x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                                |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                                |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.09x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 68.2 ms: 1.10x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.12x slower                                                                |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                                 |
| fannkuch                 | 256 ms                                                      | 290 ms: 1.13x slower                                                                 |
| create_gc_cycles         | 800 us                                                      | 910 us: 1.14x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                                |
| nbody                    | 71.3 ms                                                     | 83.5 ms: 1.17x slower                                                                |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.22x slower                                                                |
| telco                    | 3.94 ms                                                     | 5.02 ms: 1.27x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                         |

Benchmark hidden because not significant (3): json, logging_format, json_loads
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown