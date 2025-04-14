# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.226x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.15x faster                                                               |
| html5lib       | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                                |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 426 ms: 2.60x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.30x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 343 ms: 1.86x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                                |
| nbody          | 71.3 ms                                                     | 69.2 ms: 1.03x faster                                                                |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.9 ms: 1.23x faster                                                                |
| regex_dna      | 136 ms                                                      | 112 ms: 1.22x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.90 ms: 1.33x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 146 us: 1.26x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 224 us: 1.20x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                               |
| xml_etree_parse      | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                                |
| xml_etree_process    | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 58.9 ms: 1.06x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.83 ms: 1.32x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.3 ms: 1.15x faster                                                                |
| django_template | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 426 ms: 2.60x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.37x faster                                                                |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.30x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 343 ms: 1.86x faster                                                                 |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                                 |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 58.8 ns: 1.61x faster                                                                |
| richards_super           | 52.2 ms                                                     | 32.8 ms: 1.59x faster                                                                |
| go                       | 139 ms                                                      | 89.1 ms: 1.56x faster                                                                |
| richards                 | 42.4 ms                                                     | 28.9 ms: 1.47x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 19.8 us: 1.45x faster                                                                |
| chaos                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 60.4 ms: 1.42x faster                                                                |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 56.0 ms: 1.38x faster                                                                |
| raytrace                 | 273 ms                                                      | 200 ms: 1.37x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 77.7 ms: 1.37x faster                                                                |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.31 ms: 1.33x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.90 ms: 1.33x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.83 ms: 1.32x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.3 ms: 1.32x faster                                                                |
| pyflate                  | 409 ms                                                      | 310 ms: 1.32x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 146 us: 1.26x faster                                                                 |
| pycparser                | 930 ms                                                      | 742 ms: 1.25x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 50.2 ms: 1.25x faster                                                                |
| regex_compile            | 106 ms                                                      | 85.9 ms: 1.23x faster                                                                |
| regex_dna                | 136 ms                                                      | 112 ms: 1.22x faster                                                                 |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| sympy_sum                | 107 ms                                                      | 88.7 ms: 1.21x faster                                                                |
| thrift                   | 617 us                                                      | 512 us: 1.21x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 224 us: 1.20x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.19x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.16x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.16x faster                                                               |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.3 ms: 1.15x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.15x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 518 ms: 1.14x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 1.60 sec: 1.11x faster                                                               |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                                 |
| django_template          | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 866 us: 1.11x faster                                                                 |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                                 |
| genshi_xml               | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                                |
| scimark_fft              | 187 ms                                                      | 178 ms: 1.06x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 63.9 ms: 1.04x faster                                                                |
| nbody                    | 71.3 ms                                                     | 69.2 ms: 1.03x faster                                                                |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.03x faster                                                                |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                                 |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                                 |
| logging_format           | 6.76 us                                                     | 6.97 us: 1.03x slower                                                                |
| meteor_contest           | 75.9 ms                                                     | 78.3 ms: 1.03x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.47 us: 1.04x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 58.9 ms: 1.06x slower                                                                |
| fannkuch                 | 256 ms                                                      | 276 ms: 1.08x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.85 ms: 1.23x slower                                                                |
| coverage                 | 39.0 ms                                                     | 49.5 ms: 1.27x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 88.3 ms: 1.42x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.03 ms: 1.44x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.226x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown