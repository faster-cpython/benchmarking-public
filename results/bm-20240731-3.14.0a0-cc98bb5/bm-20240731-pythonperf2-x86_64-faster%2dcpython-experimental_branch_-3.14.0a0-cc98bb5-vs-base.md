# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.01x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                      | 283 ms: 1.01x faster                                                                  |
| docutils       | 3.00 sec                                                                    | 2.98 sec: 1.01x faster                                                                |
| html5lib       | 72.4 ms                                                                     | 71.7 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_generators          | 364 ms                                                                      | 351 ms: 1.04x faster                                                                  |
| async_tree_io_tg          | 773 ms                                                                      | 758 ms: 1.02x faster                                                                  |
| async_tree_memoization_tg | 386 ms                                                                      | 380 ms: 1.02x faster                                                                  |
| coroutines                | 21.4 ms                                                                     | 21.4 ms: 1.00x faster                                                                 |
| asyncio_tcp               | 373 ms                                                                      | 376 ms: 1.01x slower                                                                  |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 80.3 ms                                                                     | 76.8 ms: 1.05x faster                                                                 |
| nbody          | 87.0 ms                                                                     | 85.7 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 245 ms                                                                      | 238 ms: 1.03x faster                                                                  |
| regex_v8       | 25.9 ms                                                                     | 25.3 ms: 1.03x faster                                                                 |
| regex_effbot   | 3.48 ms                                                                     | 3.51 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.26 sec                                                                    | 2.16 sec: 1.05x faster                                                                |
| unpickle_pure_python | 212 us                                                                      | 205 us: 1.03x faster                                                                  |
| json_dumps           | 10.9 ms                                                                     | 10.7 ms: 1.02x faster                                                                 |
| xml_etree_generate   | 85.7 ms                                                                     | 84.4 ms: 1.01x faster                                                                 |
| xml_etree_iterparse  | 101 ms                                                                      | 101 ms: 1.01x faster                                                                  |
| pickle_pure_python   | 321 us                                                                      | 319 us: 1.01x faster                                                                  |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (3): xml_etree_process, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.08 ms                                                                     | 9.06 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 39.5 ms                                                                     | 39.1 ms: 1.01x faster                                                                 |
| genshi_xml      | 53.8 ms                                                                     | 55.0 ms: 1.02x slower                                                                 |
| genshi_text     | 24.9 ms                                                                     | 25.7 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads               | 2.26 sec                                                                    | 2.16 sec: 1.05x faster                                                                |
| richards                  | 50.7 ms                                                                     | 48.4 ms: 1.05x faster                                                                 |
| float                     | 80.3 ms                                                                     | 76.8 ms: 1.05x faster                                                                 |
| create_gc_cycles          | 2.03 ms                                                                     | 1.94 ms: 1.05x faster                                                                 |
| gc_traversal              | 4.69 ms                                                                     | 4.49 ms: 1.04x faster                                                                 |
| pyflate                   | 478 ms                                                                      | 458 ms: 1.04x faster                                                                  |
| async_generators          | 364 ms                                                                      | 351 ms: 1.04x faster                                                                  |
| richards_super            | 56.5 ms                                                                     | 54.7 ms: 1.03x faster                                                                 |
| coverage                  | 81.1 ms                                                                     | 78.7 ms: 1.03x faster                                                                 |
| generators                | 28.9 ms                                                                     | 28.1 ms: 1.03x faster                                                                 |
| unpickle_pure_python      | 212 us                                                                      | 205 us: 1.03x faster                                                                  |
| regex_dna                 | 245 ms                                                                      | 238 ms: 1.03x faster                                                                  |
| regex_v8                  | 25.9 ms                                                                     | 25.3 ms: 1.03x faster                                                                 |
| json                      | 5.57 ms                                                                     | 5.45 ms: 1.02x faster                                                                 |
| async_tree_io_tg          | 773 ms                                                                      | 758 ms: 1.02x faster                                                                  |
| json_dumps                | 10.9 ms                                                                     | 10.7 ms: 1.02x faster                                                                 |
| scimark_lu                | 96.7 ms                                                                     | 95.0 ms: 1.02x faster                                                                 |
| async_tree_memoization_tg | 386 ms                                                                      | 380 ms: 1.02x faster                                                                  |
| nbody                     | 87.0 ms                                                                     | 85.7 ms: 1.02x faster                                                                 |
| bpe_tokeniser             | 4.96 sec                                                                    | 4.89 sec: 1.02x faster                                                                |
| hexiom                    | 6.31 ms                                                                     | 6.22 ms: 1.01x faster                                                                 |
| xml_etree_generate        | 85.7 ms                                                                     | 84.4 ms: 1.01x faster                                                                 |
| pprint_pformat            | 1.69 sec                                                                    | 1.67 sec: 1.01x faster                                                                |
| raytrace                  | 271 ms                                                                      | 267 ms: 1.01x faster                                                                  |
| sympy_expand              | 503 ms                                                                      | 496 ms: 1.01x faster                                                                  |
| logging_silent            | 96.8 ns                                                                     | 95.6 ns: 1.01x faster                                                                 |
| 2to3                      | 286 ms                                                                      | 283 ms: 1.01x faster                                                                  |
| sympy_str                 | 295 ms                                                                      | 291 ms: 1.01x faster                                                                  |
| chaos                     | 62.1 ms                                                                     | 61.4 ms: 1.01x faster                                                                 |
| pprint_safe_repr          | 828 ms                                                                      | 817 ms: 1.01x faster                                                                  |
| django_template           | 39.5 ms                                                                     | 39.1 ms: 1.01x faster                                                                 |
| logging_format            | 6.88 us                                                                     | 6.80 us: 1.01x faster                                                                 |
| html5lib                  | 72.4 ms                                                                     | 71.7 ms: 1.01x faster                                                                 |
| sympy_sum                 | 155 ms                                                                      | 153 ms: 1.01x faster                                                                  |
| comprehensions            | 17.5 us                                                                     | 17.4 us: 1.01x faster                                                                 |
| xml_etree_iterparse       | 101 ms                                                                      | 101 ms: 1.01x faster                                                                  |
| docutils                  | 3.00 sec                                                                    | 2.98 sec: 1.01x faster                                                                |
| sqlglot_optimize          | 59.4 ms                                                                     | 59.0 ms: 1.01x faster                                                                 |
| sqlglot_parse             | 1.39 ms                                                                     | 1.39 ms: 1.01x faster                                                                 |
| pickle_pure_python        | 321 us                                                                      | 319 us: 1.01x faster                                                                  |
| pathlib                   | 16.2 ms                                                                     | 16.1 ms: 1.01x faster                                                                 |
| logging_simple            | 6.21 us                                                                     | 6.18 us: 1.01x faster                                                                 |
| coroutines                | 21.4 ms                                                                     | 21.4 ms: 1.00x faster                                                                 |
| meteor_contest            | 128 ms                                                                      | 127 ms: 1.00x faster                                                                  |
| python_startup_no_site    | 9.08 ms                                                                     | 9.06 ms: 1.00x faster                                                                 |
| deepcopy                  | 289 us                                                                      | 292 us: 1.01x slower                                                                  |
| go                        | 156 ms                                                                      | 158 ms: 1.01x slower                                                                  |
| asyncio_tcp               | 373 ms                                                                      | 376 ms: 1.01x slower                                                                  |
| mdp                       | 2.56 sec                                                                    | 2.58 sec: 1.01x slower                                                                |
| scimark_monte_carlo       | 65.5 ms                                                                     | 66.1 ms: 1.01x slower                                                                 |
| scimark_sor               | 118 ms                                                                      | 119 ms: 1.01x slower                                                                  |
| regex_effbot              | 3.48 ms                                                                     | 3.51 ms: 1.01x slower                                                                 |
| fannkuch                  | 359 ms                                                                      | 365 ms: 1.02x slower                                                                  |
| deepcopy_reduce           | 2.92 us                                                                     | 2.97 us: 1.02x slower                                                                 |
| genshi_xml                | 53.8 ms                                                                     | 55.0 ms: 1.02x slower                                                                 |
| scimark_fft               | 301 ms                                                                      | 309 ms: 1.02x slower                                                                  |
| nqueens                   | 88.5 ms                                                                     | 91.1 ms: 1.03x slower                                                                 |
| genshi_text               | 24.9 ms                                                                     | 25.7 ms: 1.03x slower                                                                 |
| pycparser                 | 1.22 sec                                                                    | 1.26 sec: 1.03x slower                                                                |
| typing_runtime_protocols  | 172 us                                                                      | 180 us: 1.05x slower                                                                  |
| crypto_pyaes              | 70.9 ms                                                                     | 74.7 ms: 1.05x slower                                                                 |
| scimark_sparse_mat_mult   | 4.03 ms                                                                     | 4.49 ms: 1.12x slower                                                                 |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (28): async_tree_io, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, dask, async_tree_memoization, pylint, xml_etree_process, bench_mp_pool, sqlglot_normalize, sqlglot_transpile, async_tree_cpu_io_mixed, thrift, python_startup, deepcopy_memo, tornado_http, pidigits, json_loads, regex_compile, sympy_integrate, asyncio_tcp_ssl, spectral_norm, xml_etree_parse, deltablue, telco, mako, asyncio_websockets

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x