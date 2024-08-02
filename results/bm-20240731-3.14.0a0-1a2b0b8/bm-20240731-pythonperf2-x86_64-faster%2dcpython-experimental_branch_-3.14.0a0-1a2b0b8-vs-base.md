# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 81.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.99 sec                                                                    | 3.01 sec: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| coroutines       | 22.2 ms                                                                     | 21.5 ms: 1.03x faster                                                                 |
| asyncio_tcp      | 377 ms                                                                      | 375 ms: 1.00x faster                                                                  |
| async_generators | 361 ms                                                                      | 365 ms: 1.01x slower                                                                  |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (10): asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.5 ms                                                                     | 80.2 ms: 1.02x faster                                                                 |
| nbody          | 86.8 ms                                                                     | 85.6 ms: 1.01x faster                                                                 |
| pidigits       | 253 ms                                                                      | 254 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                                      | 236 ms: 1.03x faster                                                                  |
| regex_v8       | 25.8 ms                                                                     | 25.6 ms: 1.01x faster                                                                 |
| regex_compile  | 141 ms                                                                      | 143 ms: 1.02x slower                                                                  |
| regex_effbot   | 3.45 ms                                                                     | 3.56 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.42 sec                                                                    | 2.21 sec: 1.10x faster                                                                |
| unpickle_pure_python | 217 us                                                                      | 210 us: 1.04x faster                                                                  |
| pickle_pure_python   | 323 us                                                                      | 321 us: 1.01x faster                                                                  |
| json_dumps           | 10.7 ms                                                                     | 10.8 ms: 1.00x slower                                                                 |
| xml_etree_iterparse  | 102 ms                                                                      | 104 ms: 1.02x slower                                                                  |
| xml_etree_parse      | 142 ms                                                                      | 145 ms: 1.02x slower                                                                  |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (3): xml_etree_process, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.10 ms                                                                     | 9.08 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml     | 55.5 ms                                                                     | 54.7 ms: 1.01x faster                                                                 |
| genshi_text    | 25.8 ms                                                                     | 27.1 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads              | 2.42 sec                                                                    | 2.21 sec: 1.10x faster                                                                |
| unpickle_pure_python     | 217 us                                                                      | 210 us: 1.04x faster                                                                  |
| coroutines               | 22.2 ms                                                                     | 21.5 ms: 1.03x faster                                                                 |
| regex_dna                | 244 ms                                                                      | 236 ms: 1.03x faster                                                                  |
| crypto_pyaes             | 73.4 ms                                                                     | 71.0 ms: 1.03x faster                                                                 |
| coverage                 | 81.0 ms                                                                     | 78.8 ms: 1.03x faster                                                                 |
| raytrace                 | 273 ms                                                                      | 266 ms: 1.03x faster                                                                  |
| scimark_monte_carlo      | 68.3 ms                                                                     | 66.5 ms: 1.03x faster                                                                 |
| sqlglot_parse            | 1.44 ms                                                                     | 1.40 ms: 1.02x faster                                                                 |
| richards                 | 52.2 ms                                                                     | 51.0 ms: 1.02x faster                                                                 |
| sqlglot_transpile        | 1.82 ms                                                                     | 1.78 ms: 1.02x faster                                                                 |
| float                    | 81.5 ms                                                                     | 80.2 ms: 1.02x faster                                                                 |
| nbody                    | 86.8 ms                                                                     | 85.6 ms: 1.01x faster                                                                 |
| genshi_xml               | 55.5 ms                                                                     | 54.7 ms: 1.01x faster                                                                 |
| logging_simple           | 6.34 us                                                                     | 6.25 us: 1.01x faster                                                                 |
| mdp                      | 2.54 sec                                                                    | 2.50 sec: 1.01x faster                                                                |
| logging_format           | 7.00 us                                                                     | 6.91 us: 1.01x faster                                                                 |
| deltablue                | 3.40 ms                                                                     | 3.36 ms: 1.01x faster                                                                 |
| richards_super           | 57.9 ms                                                                     | 57.3 ms: 1.01x faster                                                                 |
| go                       | 161 ms                                                                      | 160 ms: 1.01x faster                                                                  |
| scimark_sor              | 116 ms                                                                      | 115 ms: 1.01x faster                                                                  |
| pickle_pure_python       | 323 us                                                                      | 321 us: 1.01x faster                                                                  |
| regex_v8                 | 25.8 ms                                                                     | 25.6 ms: 1.01x faster                                                                 |
| typing_runtime_protocols | 177 us                                                                      | 176 us: 1.01x faster                                                                  |
| pprint_safe_repr         | 834 ms                                                                      | 829 ms: 1.01x faster                                                                  |
| fannkuch                 | 362 ms                                                                      | 360 ms: 1.01x faster                                                                  |
| asyncio_tcp              | 377 ms                                                                      | 375 ms: 1.00x faster                                                                  |
| bpe_tokeniser            | 4.92 sec                                                                    | 4.90 sec: 1.00x faster                                                                |
| python_startup_no_site   | 9.10 ms                                                                     | 9.08 ms: 1.00x faster                                                                 |
| sympy_integrate          | 23.5 ms                                                                     | 23.5 ms: 1.00x slower                                                                 |
| json_dumps               | 10.7 ms                                                                     | 10.8 ms: 1.00x slower                                                                 |
| pidigits                 | 253 ms                                                                      | 254 ms: 1.01x slower                                                                  |
| thrift                   | 879 us                                                                      | 886 us: 1.01x slower                                                                  |
| chaos                    | 62.0 ms                                                                     | 62.5 ms: 1.01x slower                                                                 |
| docutils                 | 2.99 sec                                                                    | 3.01 sec: 1.01x slower                                                                |
| pyflate                  | 487 ms                                                                      | 491 ms: 1.01x slower                                                                  |
| async_generators         | 361 ms                                                                      | 365 ms: 1.01x slower                                                                  |
| sympy_sum                | 154 ms                                                                      | 156 ms: 1.01x slower                                                                  |
| deepcopy                 | 287 us                                                                      | 290 us: 1.01x slower                                                                  |
| logging_silent           | 96.3 ns                                                                     | 97.4 ns: 1.01x slower                                                                 |
| pathlib                  | 16.0 ms                                                                     | 16.2 ms: 1.01x slower                                                                 |
| sympy_str                | 295 ms                                                                      | 299 ms: 1.01x slower                                                                  |
| hexiom                   | 6.29 ms                                                                     | 6.39 ms: 1.02x slower                                                                 |
| regex_compile            | 141 ms                                                                      | 143 ms: 1.02x slower                                                                  |
| meteor_contest           | 125 ms                                                                      | 128 ms: 1.02x slower                                                                  |
| gc_traversal             | 4.66 ms                                                                     | 4.75 ms: 1.02x slower                                                                 |
| sympy_expand             | 501 ms                                                                      | 511 ms: 1.02x slower                                                                  |
| nqueens                  | 89.0 ms                                                                     | 90.7 ms: 1.02x slower                                                                 |
| comprehensions           | 17.3 us                                                                     | 17.6 us: 1.02x slower                                                                 |
| xml_etree_iterparse      | 102 ms                                                                      | 104 ms: 1.02x slower                                                                  |
| scimark_lu               | 97.1 ms                                                                     | 99.2 ms: 1.02x slower                                                                 |
| xml_etree_parse          | 142 ms                                                                      | 145 ms: 1.02x slower                                                                  |
| telco                    | 7.87 ms                                                                     | 8.09 ms: 1.03x slower                                                                 |
| regex_effbot             | 3.45 ms                                                                     | 3.56 ms: 1.03x slower                                                                 |
| deepcopy_memo            | 29.4 us                                                                     | 30.5 us: 1.03x slower                                                                 |
| pycparser                | 1.22 sec                                                                    | 1.28 sec: 1.05x slower                                                                |
| genshi_text              | 25.8 ms                                                                     | 27.1 ms: 1.05x slower                                                                 |
| scimark_fft              | 290 ms                                                                      | 310 ms: 1.07x slower                                                                  |
| scimark_sparse_mat_mult  | 4.02 ms                                                                     | 4.44 ms: 1.11x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (31): bench_mp_pool, xml_etree_process, asyncio_websockets, json_loads, sqlglot_normalize, async_tree_none_tg, xml_etree_generate, async_tree_memoization_tg, python_startup, pprint_pformat, mako, spectral_norm, generators, html5lib, sqlglot_optimize, asyncio_tcp_ssl, 2to3, django_template, json, tornado_http, deepcopy_reduce, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, bench_thread_pool, pylint, async_tree_cpu_io_mixed, async_tree_io_tg, dask, create_gc_cycles, async_tree_io

# HPT report

- Reliability score: 81.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x