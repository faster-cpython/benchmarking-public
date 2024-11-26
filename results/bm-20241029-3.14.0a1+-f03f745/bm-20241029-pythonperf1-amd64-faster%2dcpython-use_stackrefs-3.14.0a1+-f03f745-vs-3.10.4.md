# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.065x faster
- HPT reliability: 95.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                         |
| html5lib       | 51.0 ms                                                     | 45.0 ms: 1.13x faster                                                          |
| tornado_http   | 108 ms                                                      | 96.4 ms: 1.12x faster                                                          |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 592 ms: 1.87x faster                                                           |
| async_tree_none         | 435 ms                                                      | 237 ms: 1.84x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 294 ms: 1.79x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 402 ms: 1.58x faster                                                           |
| Geometric mean          | (ref)                                                       | 1.77x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| nbody          | 71.3 ms                                                     | 89.4 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                           |
| regex_compile  | 106 ms                                                      | 99.9 ms: 1.06x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                          |
| regex_v8       | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|---------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps          | 9.16 ms                                                     | 7.13 ms: 1.28x faster                                                          |
| pickle_pure_python  | 270 us                                                      | 249 us: 1.08x faster                                                           |
| xml_etree_parse     | 96.8 ms                                                     | 96.0 ms: 1.01x faster                                                          |
| xml_etree_process   | 44.5 ms                                                     | 45.9 ms: 1.03x slower                                                          |
| tomli_loads         | 1.67 sec                                                    | 1.77 sec: 1.06x slower                                                         |
| json_loads          | 14.0 us                                                     | 14.9 us: 1.06x slower                                                          |
| xml_etree_iterparse | 65.0 ms                                                     | 69.9 ms: 1.08x slower                                                          |
| xml_etree_generate  | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                          |
| Geometric mean      | (ref)                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                          |
| python_startup         | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 8.02 ms: 1.13x faster                                                          |
| django_template | 28.9 ms                                                     | 28.4 ms: 1.02x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 42.6 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 126 us: 2.66x faster                                                           |
| async_tree_io            | 1.11 sec                                                    | 592 ms: 1.87x faster                                                           |
| async_tree_none          | 435 ms                                                      | 237 ms: 1.84x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 294 ms: 1.79x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.60 ms: 1.61x faster                                                          |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 402 ms: 1.58x faster                                                           |
| pylint                   | 350 ms                                                      | 234 ms: 1.50x faster                                                           |
| logging_silent           | 94.6 ns                                                     | 71.3 ns: 1.33x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 7.13 ms: 1.28x faster                                                          |
| generators               | 32.4 ms                                                     | 25.2 ms: 1.28x faster                                                          |
| go                       | 139 ms                                                      | 110 ms: 1.27x faster                                                           |
| richards_super           | 52.2 ms                                                     | 41.4 ms: 1.26x faster                                                          |
| raytrace                 | 273 ms                                                      | 220 ms: 1.24x faster                                                           |
| deepcopy                 | 255 us                                                      | 212 us: 1.20x faster                                                           |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                           |
| sqlglot_parse            | 1.22 ms                                                     | 1.02 ms: 1.19x faster                                                          |
| chaos                    | 61.7 ms                                                     | 52.0 ms: 1.19x faster                                                          |
| sqlglot_transpile        | 1.48 ms                                                     | 1.25 ms: 1.18x faster                                                          |
| deepcopy_memo            | 28.8 us                                                     | 24.9 us: 1.16x faster                                                          |
| sqlite_synth             | 1.91 us                                                     | 1.66 us: 1.15x faster                                                          |
| richards                 | 42.4 ms                                                     | 36.9 ms: 1.15x faster                                                          |
| scimark_lu               | 85.8 ms                                                     | 74.6 ms: 1.15x faster                                                          |
| pyflate                  | 409 ms                                                      | 358 ms: 1.14x faster                                                           |
| pycparser                | 930 ms                                                      | 820 ms: 1.13x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 45.0 ms: 1.13x faster                                                          |
| comprehensions           | 16.5 us                                                     | 14.6 us: 1.13x faster                                                          |
| dulwich_log              | 50.5 ms                                                     | 44.7 ms: 1.13x faster                                                          |
| mako                     | 9.03 ms                                                     | 8.02 ms: 1.13x faster                                                          |
| bench_thread_pool        | 958 us                                                      | 851 us: 1.13x faster                                                           |
| tornado_http             | 108 ms                                                      | 96.4 ms: 1.12x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 5.14 ms: 1.12x faster                                                          |
| sympy_sum                | 107 ms                                                      | 95.9 ms: 1.12x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 57.4 ms: 1.09x faster                                                          |
| mdp                      | 1.78 sec                                                    | 1.64 sec: 1.09x faster                                                         |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                         |
| pickle_pure_python       | 270 us                                                      | 249 us: 1.08x faster                                                           |
| thrift                   | 617 us                                                      | 572 us: 1.08x faster                                                           |
| sympy_integrate          | 15.3 ms                                                     | 14.4 ms: 1.06x faster                                                          |
| regex_compile            | 106 ms                                                      | 99.9 ms: 1.06x faster                                                          |
| coroutines               | 16.0 ms                                                     | 15.1 ms: 1.06x faster                                                          |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 54.7 ms: 1.05x faster                                                          |
| scimark_sor              | 106 ms                                                      | 103 ms: 1.03x faster                                                           |
| regex_v8                 | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                          |
| sympy_str                | 194 ms                                                      | 191 ms: 1.02x faster                                                           |
| django_template          | 28.9 ms                                                     | 28.4 ms: 1.02x faster                                                          |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| xml_etree_parse          | 96.8 ms                                                     | 96.0 ms: 1.01x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 2.19 us: 1.01x faster                                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 40.3 ms: 1.01x slower                                                          |
| pprint_pformat           | 1.22 sec                                                    | 1.25 sec: 1.02x slower                                                         |
| xml_etree_process        | 44.5 ms                                                     | 45.9 ms: 1.03x slower                                                          |
| json                     | 3.14 ms                                                     | 3.24 ms: 1.03x slower                                                          |
| pprint_safe_repr         | 592 ms                                                      | 614 ms: 1.04x slower                                                           |
| genshi_xml               | 41.0 ms                                                     | 42.6 ms: 1.04x slower                                                          |
| sqlglot_normalize        | 205 ms                                                      | 214 ms: 1.04x slower                                                           |
| spectral_norm            | 77.3 ms                                                     | 80.7 ms: 1.04x slower                                                          |
| sympy_expand             | 314 ms                                                      | 329 ms: 1.05x slower                                                           |
| pathlib                  | 75.7 ms                                                     | 79.7 ms: 1.05x slower                                                          |
| tomli_loads              | 1.67 sec                                                    | 1.77 sec: 1.06x slower                                                         |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                          |
| meteor_contest           | 75.9 ms                                                     | 81.5 ms: 1.07x slower                                                          |
| xml_etree_iterparse      | 65.0 ms                                                     | 69.9 ms: 1.08x slower                                                          |
| nqueens                  | 66.6 ms                                                     | 73.3 ms: 1.10x slower                                                          |
| logging_format           | 6.76 us                                                     | 7.61 us: 1.13x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                          |
| logging_simple           | 6.22 us                                                     | 7.15 us: 1.15x slower                                                          |
| python_startup           | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                          |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.18 ms: 1.17x slower                                                          |
| scimark_fft              | 187 ms                                                      | 226 ms: 1.20x slower                                                           |
| async_generators         | 222 ms                                                      | 273 ms: 1.23x slower                                                           |
| coverage                 | 39.0 ms                                                     | 48.8 ms: 1.25x slower                                                          |
| nbody                    | 71.3 ms                                                     | 89.4 ms: 1.25x slower                                                          |
| fannkuch                 | 256 ms                                                      | 330 ms: 1.29x slower                                                           |
| telco                    | 3.94 ms                                                     | 5.17 ms: 1.31x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 84.0 ms: 1.35x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 1.92 ms: 1.36x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.72x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.06x faster                                                                   |

Benchmark hidden because not significant (4): float, unpickle_pure_python, 2to3, genshi_text
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.065x faster
# HPT report

- Reliability score: 95.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown