# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.151x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.06x faster                                                           |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                         |
| html5lib       | 51.0 ms                                                     | 41.2 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 444 ms: 2.50x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 234 ms: 2.24x faster                                                           |
| async_tree_none         | 435 ms                                                      | 199 ms: 2.19x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 355 ms: 1.80x faster                                                           |
| Geometric mean          | (ref)                                                       | 2.17x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.5 ms: 1.20x faster                                                          |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                           |
| nbody          | 71.3 ms                                                     | 78.4 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                           |
| regex_compile  | 106 ms                                                      | 92.9 ms: 1.14x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.49 ms: 1.11x faster                                                          |
| regex_v8       | 15.4 ms                                                     | 15.2 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.11 ms: 1.29x faster                                                          |
| pickle_pure_python   | 270 us                                                      | 244 us: 1.10x faster                                                           |
| unpickle_pure_python | 183 us                                                      | 170 us: 1.08x faster                                                           |
| xml_etree_parse      | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                          |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                         |
| xml_etree_process    | 44.5 ms                                                     | 44.2 ms: 1.00x faster                                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.7 ms: 1.01x slower                                                          |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.07x slower                                                          |
| xml_etree_generate   | 55.5 ms                                                     | 61.2 ms: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                          |
| python_startup_no_site | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 17.6 ms: 1.13x faster                                                          |
| mako            | 9.03 ms                                                     | 8.26 ms: 1.09x faster                                                          |
| django_template | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 39.5 ms: 1.04x faster                                                          |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.91x faster                                                           |
| pathlib                  | 75.7 ms                                                     | 30.0 ms: 2.52x faster                                                          |
| async_tree_io            | 1.11 sec                                                    | 444 ms: 2.50x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 234 ms: 2.24x faster                                                           |
| async_tree_none          | 435 ms                                                      | 199 ms: 2.19x faster                                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 355 ms: 1.80x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.39 ms: 1.75x faster                                                          |
| pylint                   | 350 ms                                                      | 202 ms: 1.73x faster                                                           |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                          |
| go                       | 139 ms                                                      | 94.8 ms: 1.47x faster                                                          |
| raytrace                 | 273 ms                                                      | 197 ms: 1.39x faster                                                           |
| richards_super           | 52.2 ms                                                     | 37.8 ms: 1.38x faster                                                          |
| logging_silent           | 94.6 ns                                                     | 69.6 ns: 1.36x faster                                                          |
| chaos                    | 61.7 ms                                                     | 45.9 ms: 1.35x faster                                                          |
| deepcopy                 | 255 us                                                      | 198 us: 1.29x faster                                                           |
| json_dumps               | 9.16 ms                                                     | 7.11 ms: 1.29x faster                                                          |
| deepcopy_memo            | 28.8 us                                                     | 22.4 us: 1.28x faster                                                          |
| sqlglot_parse            | 1.22 ms                                                     | 954 us: 1.27x faster                                                           |
| richards                 | 42.4 ms                                                     | 33.4 ms: 1.27x faster                                                          |
| comprehensions           | 16.5 us                                                     | 13.0 us: 1.27x faster                                                          |
| sqlglot_transpile        | 1.48 ms                                                     | 1.17 ms: 1.26x faster                                                          |
| html5lib                 | 51.0 ms                                                     | 41.2 ms: 1.24x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 4.75 ms: 1.21x faster                                                          |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                          |
| float                    | 61.7 ms                                                     | 51.5 ms: 1.20x faster                                                          |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                          |
| pyflate                  | 409 ms                                                      | 344 ms: 1.19x faster                                                           |
| pycparser                | 930 ms                                                      | 786 ms: 1.18x faster                                                           |
| scimark_lu               | 85.8 ms                                                     | 73.9 ms: 1.16x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 66.7 ms: 1.16x faster                                                          |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                           |
| sympy_sum                | 107 ms                                                      | 92.8 ms: 1.15x faster                                                          |
| thrift                   | 617 us                                                      | 539 us: 1.15x faster                                                           |
| regex_compile            | 106 ms                                                      | 92.9 ms: 1.14x faster                                                          |
| scimark_sor              | 106 ms                                                      | 93.3 ms: 1.14x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.5 ms: 1.14x faster                                                          |
| genshi_text              | 19.8 ms                                                     | 17.6 ms: 1.13x faster                                                          |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                         |
| regex_effbot             | 1.66 ms                                                     | 1.49 ms: 1.11x faster                                                          |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                          |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 56.6 ms: 1.10x faster                                                          |
| pickle_pure_python       | 270 us                                                      | 244 us: 1.10x faster                                                           |
| bench_thread_pool        | 958 us                                                      | 869 us: 1.10x faster                                                           |
| mdp                      | 1.78 sec                                                    | 1.62 sec: 1.10x faster                                                         |
| mako                     | 9.03 ms                                                     | 8.26 ms: 1.09x faster                                                          |
| unpickle_pure_python     | 183 us                                                      | 170 us: 1.08x faster                                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 37.2 ms: 1.07x faster                                                          |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                           |
| 2to3                     | 246 ms                                                      | 231 ms: 1.06x faster                                                           |
| xml_etree_parse          | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                          |
| django_template          | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 2.09 us: 1.05x faster                                                          |
| genshi_xml               | 41.0 ms                                                     | 39.5 ms: 1.04x faster                                                          |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                         |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                          |
| regex_v8                 | 15.4 ms                                                     | 15.2 ms: 1.01x faster                                                          |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 1.20 sec: 1.01x faster                                                         |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                           |
| xml_etree_process        | 44.5 ms                                                     | 44.2 ms: 1.00x faster                                                          |
| pprint_safe_repr         | 592 ms                                                      | 596 ms: 1.01x slower                                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.7 ms: 1.01x slower                                                          |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                           |
| meteor_contest           | 75.9 ms                                                     | 78.7 ms: 1.04x slower                                                          |
| async_generators         | 222 ms                                                      | 236 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.91 ms: 1.07x slower                                                          |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.07x slower                                                          |
| nqueens                  | 66.6 ms                                                     | 71.8 ms: 1.08x slower                                                          |
| logging_format           | 6.76 us                                                     | 7.43 us: 1.10x slower                                                          |
| nbody                    | 71.3 ms                                                     | 78.4 ms: 1.10x slower                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 61.2 ms: 1.10x slower                                                          |
| logging_simple           | 6.22 us                                                     | 6.95 us: 1.12x slower                                                          |
| scimark_fft              | 187 ms                                                      | 210 ms: 1.12x slower                                                           |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                          |
| coverage                 | 39.0 ms                                                     | 48.3 ms: 1.24x slower                                                          |
| fannkuch                 | 256 ms                                                      | 317 ms: 1.24x slower                                                           |
| telco                    | 3.94 ms                                                     | 5.01 ms: 1.27x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 85.5 ms: 1.38x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 2.02 ms: 1.43x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.58x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                                   |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250220-3.14.0a5+-d270553/bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.151x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown