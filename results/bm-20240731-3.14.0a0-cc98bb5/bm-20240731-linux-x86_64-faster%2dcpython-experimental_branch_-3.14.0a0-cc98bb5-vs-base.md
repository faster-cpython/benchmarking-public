# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.00x faster
- HPT reliability: 97.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                | 261 ms: 1.01x faster                                                            |
| docutils       | 2.72 sec                                                              | 2.73 sec: 1.01x slower                                                          |
| html5lib       | 64.6 ms                                                               | 65.0 ms: 1.01x slower                                                           |
| tornado_http   | 89.7 ms                                                               | 90.0 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization | 420 ms                                                                | 401 ms: 1.05x faster                                                            |
| async_generators       | 434 ms                                                                | 429 ms: 1.01x faster                                                            |
| async_tree_none        | 326 ms                                                                | 323 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl        | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| coroutines             | 22.3 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.4 ms                                                               | 75.9 ms: 1.03x faster                                                           |
| nbody          | 86.0 ms                                                               | 84.5 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 132 ms                                                                | 131 ms: 1.01x faster                                                            |
| regex_v8       | 24.5 ms                                                               | 25.2 ms: 1.03x slower                                                           |
| regex_dna      | 219 ms                                                                | 226 ms: 1.03x slower                                                            |
| regex_effbot   | 3.66 ms                                                               | 3.78 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 158 ms                                                                | 153 ms: 1.03x faster                                                            |
| xml_etree_process    | 60.0 ms                                                               | 59.3 ms: 1.01x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                               | 85.5 ms: 1.01x faster                                                           |
| pickle_pure_python   | 303 us                                                                | 301 us: 1.01x faster                                                            |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.01x slower                                                            |
| tomli_loads          | 2.07 sec                                                              | 2.09 sec: 1.01x slower                                                          |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 23.5 ms                                                               | 22.4 ms: 1.05x faster                                                           |
| genshi_xml     | 51.7 ms                                                               | 49.5 ms: 1.04x faster                                                           |
| mako           | 10.9 ms                                                               | 11.2 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                      | 2.71 sec                                                              | 2.52 sec: 1.08x faster                                                          |
| genshi_text              | 23.5 ms                                                               | 22.4 ms: 1.05x faster                                                           |
| richards_super           | 53.0 ms                                                               | 50.6 ms: 1.05x faster                                                           |
| async_tree_memoization   | 420 ms                                                                | 401 ms: 1.05x faster                                                            |
| genshi_xml               | 51.7 ms                                                               | 49.5 ms: 1.04x faster                                                           |
| richards                 | 46.9 ms                                                               | 45.1 ms: 1.04x faster                                                           |
| go                       | 141 ms                                                                | 136 ms: 1.04x faster                                                            |
| float                    | 78.4 ms                                                               | 75.9 ms: 1.03x faster                                                           |
| logging_simple           | 5.58 us                                                               | 5.42 us: 1.03x faster                                                           |
| scimark_sor              | 124 ms                                                                | 121 ms: 1.03x faster                                                            |
| xml_etree_parse          | 158 ms                                                                | 153 ms: 1.03x faster                                                            |
| logging_format           | 6.19 us                                                               | 6.03 us: 1.03x faster                                                           |
| deltablue                | 3.19 ms                                                               | 3.12 ms: 1.02x faster                                                           |
| nbody                    | 86.0 ms                                                               | 84.5 ms: 1.02x faster                                                           |
| sqlglot_parse            | 1.27 ms                                                               | 1.25 ms: 1.02x faster                                                           |
| chaos                    | 58.7 ms                                                               | 57.9 ms: 1.01x faster                                                           |
| xml_etree_process        | 60.0 ms                                                               | 59.3 ms: 1.01x faster                                                           |
| typing_runtime_protocols | 167 us                                                                | 165 us: 1.01x faster                                                            |
| scimark_monte_carlo      | 67.4 ms                                                               | 66.7 ms: 1.01x faster                                                           |
| deepcopy_reduce          | 2.74 us                                                               | 2.71 us: 1.01x faster                                                           |
| nqueens                  | 80.2 ms                                                               | 79.4 ms: 1.01x faster                                                           |
| deepcopy                 | 265 us                                                                | 262 us: 1.01x faster                                                            |
| async_generators         | 434 ms                                                                | 429 ms: 1.01x faster                                                            |
| fannkuch                 | 407 ms                                                                | 403 ms: 1.01x faster                                                            |
| json                     | 5.15 ms                                                               | 5.10 ms: 1.01x faster                                                           |
| generators               | 28.5 ms                                                               | 28.2 ms: 1.01x faster                                                           |
| pathlib                  | 15.7 ms                                                               | 15.6 ms: 1.01x faster                                                           |
| async_tree_none          | 326 ms                                                                | 323 ms: 1.01x faster                                                            |
| regex_compile            | 132 ms                                                                | 131 ms: 1.01x faster                                                            |
| sqlglot_normalize        | 108 ms                                                                | 107 ms: 1.01x faster                                                            |
| xml_etree_generate       | 86.1 ms                                                               | 85.5 ms: 1.01x faster                                                           |
| 2to3                     | 263 ms                                                                | 261 ms: 1.01x faster                                                            |
| sqlglot_optimize         | 53.6 ms                                                               | 53.3 ms: 1.01x faster                                                           |
| pickle_pure_python       | 303 us                                                                | 301 us: 1.01x faster                                                            |
| raytrace                 | 257 ms                                                                | 257 ms: 1.00x faster                                                            |
| python_startup_no_site   | 7.05 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| deepcopy_memo            | 29.6 us                                                               | 29.7 us: 1.00x slower                                                           |
| create_gc_cycles         | 1.73 ms                                                               | 1.73 ms: 1.00x slower                                                           |
| tornado_http             | 89.7 ms                                                               | 90.0 ms: 1.00x slower                                                           |
| bench_thread_pool        | 784 us                                                                | 788 us: 1.00x slower                                                            |
| docutils                 | 2.72 sec                                                              | 2.73 sec: 1.01x slower                                                          |
| unpickle_pure_python     | 212 us                                                                | 213 us: 1.01x slower                                                            |
| tomli_loads              | 2.07 sec                                                              | 2.09 sec: 1.01x slower                                                          |
| html5lib                 | 64.6 ms                                                               | 65.0 ms: 1.01x slower                                                           |
| comprehensions           | 16.5 us                                                               | 16.6 us: 1.01x slower                                                           |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| scimark_lu               | 113 ms                                                                | 114 ms: 1.01x slower                                                            |
| bpe_tokeniser            | 4.81 sec                                                              | 4.87 sec: 1.01x slower                                                          |
| crypto_pyaes             | 71.4 ms                                                               | 72.3 ms: 1.01x slower                                                           |
| sympy_sum                | 150 ms                                                                | 152 ms: 1.01x slower                                                            |
| pprint_safe_repr         | 736 ms                                                                | 748 ms: 1.02x slower                                                            |
| coroutines               | 22.3 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| hexiom                   | 6.16 ms                                                               | 6.28 ms: 1.02x slower                                                           |
| pprint_pformat           | 1.50 sec                                                              | 1.53 sec: 1.02x slower                                                          |
| scimark_sparse_mat_mult  | 4.68 ms                                                               | 4.79 ms: 1.02x slower                                                           |
| regex_v8                 | 24.5 ms                                                               | 25.2 ms: 1.03x slower                                                           |
| mako                     | 10.9 ms                                                               | 11.2 ms: 1.03x slower                                                           |
| regex_dna                | 219 ms                                                                | 226 ms: 1.03x slower                                                            |
| regex_effbot             | 3.66 ms                                                               | 3.78 ms: 1.03x slower                                                           |
| gc_traversal             | 3.53 ms                                                               | 3.65 ms: 1.03x slower                                                           |
| spectral_norm            | 110 ms                                                                | 113 ms: 1.03x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (27): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, async_tree_io_tg, xml_etree_iterparse, async_tree_memoization_tg, meteor_contest, pylint, telco, json_loads, scimark_fft, dask, coverage, sympy_integrate, sqlglot_transpile, pidigits, pyflate, asyncio_tcp, sympy_expand, bench_mp_pool, django_template, pycparser, asyncio_websockets, thrift, sympy_str, logging_silent

# HPT report

- Reliability score: 97.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x