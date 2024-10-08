# Results vs. base

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: 852115b
- commit date: 2024-08-19
- overall geometric mean: 1.01x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                      | 289 ms: 1.02x slower                                                                |
| docutils       | 2.97 sec                                                                    | 2.99 sec: 1.01x slower                                                              |
| html5lib       | 72.5 ms                                                                     | 75.4 ms: 1.04x slower                                                               |
| tornado_http   | 116 ms                                                                      | 118 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| asyncio_tcp      | 374 ms                                                                      | 376 ms: 1.01x slower                                                                |
| async_generators | 362 ms                                                                      | 368 ms: 1.02x slower                                                                |
| coroutines       | 21.3 ms                                                                     | 21.8 ms: 1.02x slower                                                               |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (10): async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 80.8 ms                                                                     | 80.1 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                                     | 25.2 ms: 1.03x faster                                                               |
| regex_effbot   | 3.64 ms                                                                     | 3.66 ms: 1.00x slower                                                               |
| regex_dna      | 238 ms                                                                      | 239 ms: 1.01x slower                                                                |
| regex_compile  | 139 ms                                                                      | 140 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                                     | 10.6 ms: 1.01x faster                                                               |
| unpickle_pure_python | 214 us                                                                      | 213 us: 1.01x faster                                                                |
| pickle_pure_python   | 315 us                                                                      | 317 us: 1.01x slower                                                                |
| xml_etree_parse      | 141 ms                                                                      | 143 ms: 1.01x slower                                                                |
| xml_etree_iterparse  | 99.7 ms                                                                     | 102 ms: 1.02x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (4): tomli_loads, json_loads, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 9.05 ms                                                                     | 9.03 ms: 1.00x faster                                                               |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                                     | 25.7 ms: 1.03x slower                                                               |
| django_template | 38.4 ms                                                                     | 39.6 ms: 1.03x slower                                                               |
| genshi_xml      | 53.4 ms                                                                     | 55.1 ms: 1.03x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|--------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| scimark_monte_carlo      | 68.0 ms                                                                     | 64.7 ms: 1.05x faster                                                               |
| regex_v8                 | 26.0 ms                                                                     | 25.2 ms: 1.03x faster                                                               |
| telco                    | 8.19 ms                                                                     | 8.01 ms: 1.02x faster                                                               |
| hexiom                   | 6.33 ms                                                                     | 6.23 ms: 1.02x faster                                                               |
| deepcopy                 | 288 us                                                                      | 284 us: 1.01x faster                                                                |
| json_dumps               | 10.7 ms                                                                     | 10.6 ms: 1.01x faster                                                               |
| spectral_norm            | 96.6 ms                                                                     | 95.6 ms: 1.01x faster                                                               |
| float                    | 80.8 ms                                                                     | 80.1 ms: 1.01x faster                                                               |
| sqlglot_normalize        | 119 ms                                                                      | 118 ms: 1.01x faster                                                                |
| gc_traversal             | 4.47 ms                                                                     | 4.44 ms: 1.01x faster                                                               |
| raytrace                 | 265 ms                                                                      | 263 ms: 1.01x faster                                                                |
| sqlglot_optimize         | 59.1 ms                                                                     | 58.7 ms: 1.01x faster                                                               |
| meteor_contest           | 126 ms                                                                      | 125 ms: 1.01x faster                                                                |
| unpickle_pure_python     | 214 us                                                                      | 213 us: 1.01x faster                                                                |
| deepcopy_reduce          | 2.89 us                                                                     | 2.87 us: 1.00x faster                                                               |
| python_startup_no_site   | 9.05 ms                                                                     | 9.03 ms: 1.00x faster                                                               |
| pprint_pformat           | 1.68 sec                                                                    | 1.69 sec: 1.00x slower                                                              |
| regex_effbot             | 3.64 ms                                                                     | 3.66 ms: 1.00x slower                                                               |
| asyncio_tcp              | 374 ms                                                                      | 376 ms: 1.01x slower                                                                |
| docutils                 | 2.97 sec                                                                    | 2.99 sec: 1.01x slower                                                              |
| mdp                      | 2.50 sec                                                                    | 2.51 sec: 1.01x slower                                                              |
| regex_dna                | 238 ms                                                                      | 239 ms: 1.01x slower                                                                |
| pickle_pure_python       | 315 us                                                                      | 317 us: 1.01x slower                                                                |
| sympy_expand             | 500 ms                                                                      | 503 ms: 1.01x slower                                                                |
| deepcopy_memo            | 29.4 us                                                                     | 29.6 us: 1.01x slower                                                               |
| bpe_tokeniser            | 4.96 sec                                                                    | 5.00 sec: 1.01x slower                                                              |
| regex_compile            | 139 ms                                                                      | 140 ms: 1.01x slower                                                                |
| chaos                    | 61.3 ms                                                                     | 61.8 ms: 1.01x slower                                                               |
| pprint_safe_repr         | 820 ms                                                                      | 827 ms: 1.01x slower                                                                |
| pathlib                  | 15.9 ms                                                                     | 16.1 ms: 1.01x slower                                                               |
| json                     | 5.31 ms                                                                     | 5.37 ms: 1.01x slower                                                               |
| sqlglot_transpile        | 1.78 ms                                                                     | 1.80 ms: 1.01x slower                                                               |
| sympy_sum                | 154 ms                                                                      | 155 ms: 1.01x slower                                                                |
| xml_etree_parse          | 141 ms                                                                      | 143 ms: 1.01x slower                                                                |
| scimark_sor              | 115 ms                                                                      | 116 ms: 1.01x slower                                                                |
| sympy_str                | 293 ms                                                                      | 297 ms: 1.01x slower                                                                |
| nqueens                  | 89.7 ms                                                                     | 90.9 ms: 1.01x slower                                                               |
| sqlglot_parse            | 1.41 ms                                                                     | 1.43 ms: 1.01x slower                                                               |
| comprehensions           | 17.0 us                                                                     | 17.3 us: 1.02x slower                                                               |
| async_generators         | 362 ms                                                                      | 368 ms: 1.02x slower                                                                |
| crypto_pyaes             | 72.0 ms                                                                     | 73.3 ms: 1.02x slower                                                               |
| 2to3                     | 284 ms                                                                      | 289 ms: 1.02x slower                                                                |
| deltablue                | 3.35 ms                                                                     | 3.41 ms: 1.02x slower                                                               |
| coroutines               | 21.3 ms                                                                     | 21.8 ms: 1.02x slower                                                               |
| tornado_http             | 116 ms                                                                      | 118 ms: 1.02x slower                                                                |
| xml_etree_iterparse      | 99.7 ms                                                                     | 102 ms: 1.02x slower                                                                |
| thrift                   | 867 us                                                                      | 888 us: 1.02x slower                                                                |
| genshi_text              | 25.0 ms                                                                     | 25.7 ms: 1.03x slower                                                               |
| django_template          | 38.4 ms                                                                     | 39.6 ms: 1.03x slower                                                               |
| genshi_xml               | 53.4 ms                                                                     | 55.1 ms: 1.03x slower                                                               |
| typing_runtime_protocols | 174 us                                                                      | 180 us: 1.03x slower                                                                |
| generators               | 28.1 ms                                                                     | 29.1 ms: 1.03x slower                                                               |
| go                       | 157 ms                                                                      | 163 ms: 1.04x slower                                                                |
| coverage                 | 77.3 ms                                                                     | 80.3 ms: 1.04x slower                                                               |
| html5lib                 | 72.5 ms                                                                     | 75.4 ms: 1.04x slower                                                               |
| logging_simple           | 6.18 us                                                                     | 6.43 us: 1.04x slower                                                               |
| logging_format           | 6.77 us                                                                     | 7.09 us: 1.05x slower                                                               |
| pyflate                  | 464 ms                                                                      | 496 ms: 1.07x slower                                                                |
| Geometric mean           | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (31): async_tree_io, tomli_loads, async_tree_cpu_io_mixed_tg, json_loads, asyncio_websockets, async_tree_cpu_io_mixed, asyncio_tcp_ssl, xml_etree_process, xml_etree_generate, async_tree_none, scimark_lu, scimark_fft, pidigits, async_tree_none_tg, fannkuch, python_startup, scimark_sparse_mat_mult, async_tree_memoization, sympy_integrate, logging_silent, async_tree_io_tg, async_tree_memoization_tg, nbody, richards, pycparser, richards_super, mako, pylint, create_gc_cycles, bench_thread_pool, bench_mp_pool

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x