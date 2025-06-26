# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.279x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 398 ms: 2.78x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.55x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 326 ms: 1.95x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                                |
| nbody          | 71.3 ms                                                     | 65.3 ms: 1.09x faster                                                                |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.8 ms: 1.33x faster                                                                |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                                |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.29x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 38.7 ms: 1.15x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| python_startup         | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 14.8 ms: 1.33x faster                                                                |
| mako            | 9.03 ms                                                     | 6.80 ms: 1.33x faster                                                                |
| django_template | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.29x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 398 ms: 2.78x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.55x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                                |
| mdp                      | 1.78 sec                                                    | 811 ms: 2.20x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 326 ms: 1.95x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                                |
| go                       | 139 ms                                                      | 76.5 ms: 1.82x faster                                                                |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.69x faster                                                                |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.60x faster                                                                |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                                                |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                                |
| raytrace                 | 273 ms                                                      | 178 ms: 1.53x faster                                                                 |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 57.8 ms: 1.48x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                                |
| pyflate                  | 409 ms                                                      | 287 ms: 1.43x faster                                                                 |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.04 ms: 1.42x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 76.7 ms: 1.38x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 46.8 ms: 1.34x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 14.8 ms: 1.33x faster                                                                |
| regex_compile            | 106 ms                                                      | 79.8 ms: 1.33x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.80 ms: 1.33x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                                |
| pycparser                | 930 ms                                                      | 713 ms: 1.30x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.29x faster                                                                 |
| thrift                   | 617 us                                                      | 504 us: 1.22x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                                |
| sympy_sum                | 107 ms                                                      | 88.1 ms: 1.21x faster                                                                |
| django_template          | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                               |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| spectral_norm            | 77.3 ms                                                     | 66.2 ms: 1.17x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 38.7 ms: 1.15x faster                                                                |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                                 |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 532 ms: 1.11x faster                                                                 |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                                 |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                                |
| nbody                    | 71.3 ms                                                     | 65.3 ms: 1.09x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 61.3 ms: 1.09x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.09x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.08x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                                |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                                 |
| meteor_contest           | 75.9 ms                                                     | 70.7 ms: 1.07x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                                |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                                 |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.02x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                                                |
| logging_simple           | 6.22 us                                                     | 6.26 us: 1.01x slower                                                                |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                                |
| async_generators         | 222 ms                                                      | 226 ms: 1.02x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.53 ms: 1.15x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 319 ns: 3.37x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                                         |

Benchmark hidden because not significant (1): logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.279x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown