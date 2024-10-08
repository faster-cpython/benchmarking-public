# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x slower
- HPT reliability: 99.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                | 266 ms: 1.00x slower                                                            |
| docutils       | 2.74 sec                                                              | 2.73 sec: 1.01x faster                                                          |
| html5lib       | 64.7 ms                                                               | 65.9 ms: 1.02x slower                                                           |
| tornado_http   | 90.2 ms                                                               | 90.6 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets | 560 ms                                                                | 554 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl    | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                                          |
| coroutines         | 22.2 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (10): async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_memoization_tg, async_generators, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.0 ms                                                               | 76.4 ms: 1.02x faster                                                           |
| nbody          | 87.7 ms                                                               | 86.4 ms: 1.02x faster                                                           |
| pidigits       | 188 ms                                                                | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 224 ms                                                                | 216 ms: 1.04x faster                                                            |
| regex_effbot   | 3.68 ms                                                               | 3.70 ms: 1.01x slower                                                           |
| regex_compile  | 131 ms                                                                | 135 ms: 1.03x slower                                                            |
| regex_v8       | 24.3 ms                                                               | 25.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 59.8 ms                                                               | 58.7 ms: 1.02x faster                                                           |
| xml_etree_generate   | 85.9 ms                                                               | 85.2 ms: 1.01x faster                                                           |
| unpickle_pure_python | 214 us                                                                | 213 us: 1.00x faster                                                            |
| pickle_pure_python   | 304 us                                                                | 307 us: 1.01x slower                                                            |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| tomli_loads          | 2.04 sec                                                              | 2.10 sec: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.06 ms: 1.01x faster                                                           |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                               | 22.8 ms: 1.03x faster                                                           |
| genshi_xml      | 51.4 ms                                                               | 50.2 ms: 1.03x faster                                                           |
| mako            | 11.3 ms                                                               | 11.4 ms: 1.01x slower                                                           |
| django_template | 34.2 ms                                                               | 35.5 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna                | 224 ms                                                                | 216 ms: 1.04x faster                                                            |
| generators               | 28.9 ms                                                               | 27.9 ms: 1.04x faster                                                           |
| gc_traversal             | 3.75 ms                                                               | 3.65 ms: 1.03x faster                                                           |
| genshi_text              | 23.5 ms                                                               | 22.8 ms: 1.03x faster                                                           |
| genshi_xml               | 51.4 ms                                                               | 50.2 ms: 1.03x faster                                                           |
| float                    | 78.0 ms                                                               | 76.4 ms: 1.02x faster                                                           |
| pycparser                | 1.18 sec                                                              | 1.15 sec: 1.02x faster                                                          |
| xml_etree_process        | 59.8 ms                                                               | 58.7 ms: 1.02x faster                                                           |
| nbody                    | 87.7 ms                                                               | 86.4 ms: 1.02x faster                                                           |
| deepcopy                 | 267 us                                                                | 263 us: 1.02x faster                                                            |
| create_gc_cycles         | 1.75 ms                                                               | 1.73 ms: 1.01x faster                                                           |
| deltablue                | 3.26 ms                                                               | 3.22 ms: 1.01x faster                                                           |
| asyncio_websockets       | 560 ms                                                                | 554 ms: 1.01x faster                                                            |
| xml_etree_generate       | 85.9 ms                                                               | 85.2 ms: 1.01x faster                                                           |
| python_startup_no_site   | 7.11 ms                                                               | 7.06 ms: 1.01x faster                                                           |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| docutils                 | 2.74 sec                                                              | 2.73 sec: 1.01x faster                                                          |
| pidigits                 | 188 ms                                                                | 187 ms: 1.00x faster                                                            |
| richards                 | 46.6 ms                                                               | 46.5 ms: 1.00x faster                                                           |
| unpickle_pure_python     | 214 us                                                                | 213 us: 1.00x faster                                                            |
| mdp                      | 2.52 sec                                                              | 2.52 sec: 1.00x slower                                                          |
| sympy_integrate          | 19.8 ms                                                               | 19.8 ms: 1.00x slower                                                           |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                                          |
| 2to3                     | 265 ms                                                                | 266 ms: 1.00x slower                                                            |
| tornado_http             | 90.2 ms                                                               | 90.6 ms: 1.00x slower                                                           |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                           |
| sqlglot_optimize         | 53.4 ms                                                               | 53.8 ms: 1.01x slower                                                           |
| sqlglot_normalize        | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| regex_effbot             | 3.68 ms                                                               | 3.70 ms: 1.01x slower                                                           |
| sqlglot_transpile        | 1.58 ms                                                               | 1.59 ms: 1.01x slower                                                           |
| typing_runtime_protocols | 164 us                                                                | 166 us: 1.01x slower                                                            |
| pickle_pure_python       | 304 us                                                                | 307 us: 1.01x slower                                                            |
| fannkuch                 | 405 ms                                                                | 409 ms: 1.01x slower                                                            |
| chaos                    | 58.8 ms                                                               | 59.5 ms: 1.01x slower                                                           |
| raytrace                 | 260 ms                                                                | 264 ms: 1.01x slower                                                            |
| mako                     | 11.3 ms                                                               | 11.4 ms: 1.01x slower                                                           |
| sympy_str                | 271 ms                                                                | 275 ms: 1.01x slower                                                            |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| meteor_contest           | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| comprehensions           | 16.5 us                                                               | 16.8 us: 1.01x slower                                                           |
| go                       | 142 ms                                                                | 144 ms: 1.01x slower                                                            |
| nqueens                  | 78.8 ms                                                               | 80.0 ms: 1.01x slower                                                           |
| sympy_expand             | 460 ms                                                                | 467 ms: 1.02x slower                                                            |
| scimark_lu               | 114 ms                                                                | 116 ms: 1.02x slower                                                            |
| html5lib                 | 64.7 ms                                                               | 65.9 ms: 1.02x slower                                                           |
| scimark_monte_carlo      | 68.0 ms                                                               | 69.4 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult  | 4.60 ms                                                               | 4.71 ms: 1.02x slower                                                           |
| coroutines               | 22.2 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| logging_format           | 6.05 us                                                               | 6.19 us: 1.02x slower                                                           |
| spectral_norm            | 109 ms                                                                | 112 ms: 1.02x slower                                                            |
| regex_compile            | 131 ms                                                                | 135 ms: 1.03x slower                                                            |
| deepcopy_reduce          | 2.69 us                                                               | 2.77 us: 1.03x slower                                                           |
| hexiom                   | 6.14 ms                                                               | 6.33 ms: 1.03x slower                                                           |
| thrift                   | 770 us                                                                | 794 us: 1.03x slower                                                            |
| tomli_loads              | 2.04 sec                                                              | 2.10 sec: 1.03x slower                                                          |
| regex_v8                 | 24.3 ms                                                               | 25.1 ms: 1.03x slower                                                           |
| django_template          | 34.2 ms                                                               | 35.5 ms: 1.04x slower                                                           |
| logging_simple           | 5.42 us                                                               | 5.63 us: 1.04x slower                                                           |
| scimark_fft              | 353 ms                                                                | 367 ms: 1.04x slower                                                            |
| pyflate                  | 470 ms                                                                | 490 ms: 1.04x slower                                                            |
| crypto_pyaes             | 71.6 ms                                                               | 74.8 ms: 1.04x slower                                                           |
| scimark_sor              | 125 ms                                                                | 134 ms: 1.07x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (28): async_tree_io_tg, async_tree_none_tg, xml_etree_parse, async_tree_none, telco, async_tree_io, pathlib, async_tree_memoization_tg, async_generators, json, bench_mp_pool, pprint_pformat, pprint_safe_repr, json_loads, bench_thread_pool, asyncio_tcp, bpe_tokeniser, richards_super, coverage, logging_silent, sympy_sum, xml_etree_iterparse, pylint, async_tree_cpu_io_mixed_tg, deepcopy_memo, async_tree_cpu_io_mixed, dask, async_tree_memoization

# HPT report

- Reliability score: 99.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x