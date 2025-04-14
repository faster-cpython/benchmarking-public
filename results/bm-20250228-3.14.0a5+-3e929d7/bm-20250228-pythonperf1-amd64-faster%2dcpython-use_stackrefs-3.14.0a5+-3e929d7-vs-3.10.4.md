# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.213x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                           |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                         |
| html5lib       | 51.0 ms                                                     | 41.0 ms: 1.25x faster                                                          |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 423 ms: 2.62x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 221 ms: 2.38x faster                                                           |
| async_tree_none         | 435 ms                                                      | 188 ms: 2.32x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 345 ms: 1.85x faster                                                           |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                          |
| nbody          | 71.3 ms                                                     | 68.6 ms: 1.04x faster                                                          |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.9 ms: 1.23x faster                                                          |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                           |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                          |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.97 ms: 1.32x faster                                                          |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                           |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                         |
| pickle_pure_python   | 270 us                                                      | 230 us: 1.17x faster                                                           |
| xml_etree_parse      | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                          |
| xml_etree_process    | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                          |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                          |
| xml_etree_generate   | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                          |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.93 ms: 1.30x faster                                                          |
| genshi_text     | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                          |
| django_template | 28.9 ms                                                     | 26.4 ms: 1.09x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                          |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.99x faster                                                           |
| async_tree_io            | 1.11 sec                                                    | 423 ms: 2.62x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 221 ms: 2.38x faster                                                           |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                          |
| async_tree_none          | 435 ms                                                      | 188 ms: 2.32x faster                                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 345 ms: 1.85x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                          |
| pylint                   | 350 ms                                                      | 202 ms: 1.73x faster                                                           |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                          |
| logging_silent           | 94.6 ns                                                     | 58.5 ns: 1.62x faster                                                          |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                          |
| go                       | 139 ms                                                      | 88.8 ms: 1.56x faster                                                          |
| deepcopy_memo            | 28.8 us                                                     | 19.5 us: 1.48x faster                                                          |
| richards                 | 42.4 ms                                                     | 29.1 ms: 1.46x faster                                                          |
| chaos                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                          |
| deepcopy                 | 255 us                                                      | 183 us: 1.39x faster                                                           |
| raytrace                 | 273 ms                                                      | 197 ms: 1.39x faster                                                           |
| scimark_lu               | 85.8 ms                                                     | 62.4 ms: 1.38x faster                                                          |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.37x faster                                                          |
| sqlglot_parse            | 1.22 ms                                                     | 892 us: 1.36x faster                                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                          |
| float                    | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                          |
| scimark_sor              | 106 ms                                                      | 80.3 ms: 1.32x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 4.36 ms: 1.32x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 6.97 ms: 1.32x faster                                                          |
| pyflate                  | 409 ms                                                      | 312 ms: 1.31x faster                                                           |
| mako                     | 9.03 ms                                                     | 6.93 ms: 1.30x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 60.0 ms: 1.29x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.6 ms: 1.28x faster                                                          |
| html5lib                 | 51.0 ms                                                     | 41.0 ms: 1.25x faster                                                          |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                           |
| crypto_pyaes             | 62.5 ms                                                     | 50.5 ms: 1.24x faster                                                          |
| regex_compile            | 106 ms                                                      | 85.9 ms: 1.23x faster                                                          |
| pycparser                | 930 ms                                                      | 761 ms: 1.22x faster                                                           |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                          |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                           |
| sympy_sum                | 107 ms                                                      | 89.6 ms: 1.19x faster                                                          |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                          |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                         |
| pickle_pure_python       | 270 us                                                      | 230 us: 1.17x faster                                                           |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                          |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                          |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                           |
| genshi_text              | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                          |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                         |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.12x faster                                                          |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                         |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                         |
| bench_thread_pool        | 958 us                                                      | 861 us: 1.11x faster                                                           |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                           |
| pprint_safe_repr         | 592 ms                                                      | 540 ms: 1.10x faster                                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                          |
| django_template          | 28.9 ms                                                     | 26.4 ms: 1.09x faster                                                          |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                           |
| genshi_xml               | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                          |
| xml_etree_parse          | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                          |
| xml_etree_process        | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                                          |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.61 ms: 1.04x faster                                                          |
| nbody                    | 71.3 ms                                                     | 68.6 ms: 1.04x faster                                                          |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                           |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.02x faster                                                          |
| nqueens                  | 66.6 ms                                                     | 65.3 ms: 1.02x faster                                                          |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                          |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                           |
| meteor_contest           | 75.9 ms                                                     | 76.8 ms: 1.01x slower                                                          |
| scimark_fft              | 187 ms                                                      | 190 ms: 1.01x slower                                                           |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                           |
| logging_format           | 6.76 us                                                     | 7.06 us: 1.04x slower                                                          |
| logging_simple           | 6.22 us                                                     | 6.52 us: 1.05x slower                                                          |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                          |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                           |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                          |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                          |
| telco                    | 3.94 ms                                                     | 4.93 ms: 1.25x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 86.4 ms: 1.39x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 2.01 ms: 1.43x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-3e929d7/bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.213x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown