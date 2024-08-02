# Results vs. base

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 26aa174
- commit date: 2024-07-08
- overall geometric mean: 1.00x faster
- HPT reliability: 97.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                | 261 ms: 1.00x faster                                                   |
| docutils       | 2.69 sec                                                              | 2.71 sec: 1.01x slower                                                 |
| html5lib       | 65.3 ms                                                               | 65.8 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 86.9 ms                                                               | 85.0 ms: 1.02x faster                                                  |
| float          | 76.3 ms                                                               | 75.5 ms: 1.01x faster                                                  |
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                | 129 ms: 1.00x faster                                                   |
| regex_effbot   | 3.73 ms                                                               | 3.82 ms: 1.02x slower                                                  |
| regex_dna      | 221 ms                                                                | 229 ms: 1.04x slower                                                   |
| regex_v8       | 24.0 ms                                                               | 25.8 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 10.8 ms                                                               | 10.5 ms: 1.03x faster                                                  |
| unpickle_pure_python | 211 us                                                                | 208 us: 1.02x faster                                                   |
| xml_etree_process    | 59.6 ms                                                               | 58.8 ms: 1.01x faster                                                  |
| xml_etree_generate   | 85.4 ms                                                               | 84.7 ms: 1.01x faster                                                  |
| pickle_pure_python   | 300 us                                                                | 299 us: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (4): xml_etree_parse, tomli_loads, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                  |
| python_startup_no_site | 7.05 ms                                                               | 7.04 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.5 ms                                                               | 33.7 ms: 1.02x faster                                                  |
| mako            | 11.0 ms                                                               | 11.0 ms: 1.00x slower                                                  |
| genshi_xml      | 49.5 ms                                                               | 50.8 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pyflate                  | 464 ms                                                                | 443 ms: 1.05x faster                                                   |
| crypto_pyaes             | 73.3 ms                                                               | 70.5 ms: 1.04x faster                                                  |
| deltablue                | 3.24 ms                                                               | 3.14 ms: 1.03x faster                                                  |
| json_dumps               | 10.8 ms                                                               | 10.5 ms: 1.03x faster                                                  |
| logging_silent           | 99.7 ns                                                               | 97.1 ns: 1.03x faster                                                  |
| django_template          | 34.5 ms                                                               | 33.7 ms: 1.02x faster                                                  |
| scimark_lu               | 114 ms                                                                | 112 ms: 1.02x faster                                                   |
| nbody                    | 86.9 ms                                                               | 85.0 ms: 1.02x faster                                                  |
| logging_simple           | 5.62 us                                                               | 5.50 us: 1.02x faster                                                  |
| nqueens                  | 80.6 ms                                                               | 78.9 ms: 1.02x faster                                                  |
| fannkuch                 | 394 ms                                                                | 386 ms: 1.02x faster                                                   |
| coroutines               | 23.0 ms                                                               | 22.6 ms: 1.02x faster                                                  |
| typing_runtime_protocols | 166 us                                                                | 162 us: 1.02x faster                                                   |
| raytrace                 | 261 ms                                                                | 256 ms: 1.02x faster                                                   |
| unpickle_pure_python     | 211 us                                                                | 208 us: 1.02x faster                                                   |
| sqlglot_transpile        | 1.58 ms                                                               | 1.56 ms: 1.02x faster                                                  |
| richards_super           | 52.3 ms                                                               | 51.4 ms: 1.02x faster                                                  |
| hexiom                   | 6.11 ms                                                               | 6.01 ms: 1.02x faster                                                  |
| thrift                   | 805 us                                                                | 793 us: 1.02x faster                                                   |
| async_generators         | 434 ms                                                                | 427 ms: 1.02x faster                                                   |
| xml_etree_process        | 59.6 ms                                                               | 58.8 ms: 1.01x faster                                                  |
| deepcopy_reduce          | 2.69 us                                                               | 2.66 us: 1.01x faster                                                  |
| comprehensions           | 16.5 us                                                               | 16.3 us: 1.01x faster                                                  |
| logging_format           | 6.29 us                                                               | 6.20 us: 1.01x faster                                                  |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                   |
| bpe_tokeniser            | 4.88 sec                                                              | 4.82 sec: 1.01x faster                                                 |
| richards                 | 46.3 ms                                                               | 45.8 ms: 1.01x faster                                                  |
| spectral_norm            | 112 ms                                                                | 110 ms: 1.01x faster                                                   |
| float                    | 76.3 ms                                                               | 75.5 ms: 1.01x faster                                                  |
| xml_etree_generate       | 85.4 ms                                                               | 84.7 ms: 1.01x faster                                                  |
| pathlib                  | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                  |
| sqlglot_normalize        | 108 ms                                                                | 107 ms: 1.01x faster                                                   |
| sympy_sum                | 151 ms                                                                | 150 ms: 1.01x faster                                                   |
| asyncio_websockets       | 557 ms                                                                | 554 ms: 1.01x faster                                                   |
| pickle_pure_python       | 300 us                                                                | 299 us: 1.01x faster                                                   |
| sympy_integrate          | 19.8 ms                                                               | 19.7 ms: 1.00x faster                                                  |
| regex_compile            | 129 ms                                                                | 129 ms: 1.00x faster                                                   |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                  |
| dulwich_log              | 64.4 ms                                                               | 64.1 ms: 1.00x faster                                                  |
| 2to3                     | 262 ms                                                                | 261 ms: 1.00x faster                                                   |
| python_startup_no_site   | 7.05 ms                                                               | 7.04 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.78 sec: 1.00x slower                                                 |
| sqlglot_optimize         | 53.3 ms                                                               | 53.4 ms: 1.00x slower                                                  |
| bench_thread_pool        | 789 us                                                                | 791 us: 1.00x slower                                                   |
| mako                     | 11.0 ms                                                               | 11.0 ms: 1.00x slower                                                  |
| pprint_pformat           | 1.51 sec                                                              | 1.52 sec: 1.00x slower                                                 |
| scimark_fft              | 360 ms                                                                | 362 ms: 1.01x slower                                                   |
| pidigits                 | 186 ms                                                                | 188 ms: 1.01x slower                                                   |
| coverage                 | 91.8 ms                                                               | 92.4 ms: 1.01x slower                                                  |
| html5lib                 | 65.3 ms                                                               | 65.8 ms: 1.01x slower                                                  |
| docutils                 | 2.69 sec                                                              | 2.71 sec: 1.01x slower                                                 |
| deepcopy                 | 259 us                                                                | 261 us: 1.01x slower                                                   |
| deepcopy_memo            | 29.3 us                                                               | 29.5 us: 1.01x slower                                                  |
| json                     | 5.06 ms                                                               | 5.11 ms: 1.01x slower                                                  |
| create_gc_cycles         | 1.72 ms                                                               | 1.75 ms: 1.02x slower                                                  |
| telco                    | 8.13 ms                                                               | 8.26 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult  | 4.73 ms                                                               | 4.81 ms: 1.02x slower                                                  |
| asyncio_tcp              | 474 ms                                                                | 485 ms: 1.02x slower                                                   |
| regex_effbot             | 3.73 ms                                                               | 3.82 ms: 1.02x slower                                                  |
| genshi_xml               | 49.5 ms                                                               | 50.8 ms: 1.03x slower                                                  |
| regex_dna                | 221 ms                                                                | 229 ms: 1.04x slower                                                   |
| pycparser                | 1.13 sec                                                              | 1.17 sec: 1.04x slower                                                 |
| mdp                      | 2.53 sec                                                              | 2.66 sec: 1.05x slower                                                 |
| gc_traversal             | 3.51 ms                                                               | 3.76 ms: 1.07x slower                                                  |
| regex_v8                 | 24.0 ms                                                               | 25.8 ms: 1.08x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (26): xml_etree_parse, async_tree_none, sympy_expand, scimark_monte_carlo, pylint, async_tree_io_tg, go, sqlglot_parse, async_tree_cpu_io_mixed, chaos, tornado_http, dask, tomli_loads, json_loads, async_tree_cpu_io_mixed_tg, bench_mp_pool, sympy_str, async_tree_memoization, pprint_safe_repr, xml_etree_iterparse, async_tree_none_tg, generators, async_tree_memoization_tg, genshi_text, scimark_sor, async_tree_io

# HPT report

- Reliability score: 97.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x