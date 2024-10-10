# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.00x slower
- HPT reliability: 54.37%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 317 ms                                                                      | 315 ms: 1.01x faster                                                     |
| docutils       | 3.23 sec                                                                    | 3.17 sec: 1.02x faster                                                   |
| html5lib       | 71.8 ms                                                                     | 73.1 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators | 386 ms                                                                      | 382 ms: 1.01x faster                                                     |
| coroutines       | 21.2 ms                                                                     | 22.1 ms: 1.04x slower                                                    |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (11): asyncio_tcp, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 86.9 ms                                                                     | 83.3 ms: 1.04x faster                                                    |
| float          | 76.0 ms                                                                     | 75.3 ms: 1.01x faster                                                    |
| pidigits       | 251 ms                                                                      | 251 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.7 ms                                                                     | 24.8 ms: 1.07x faster                                                    |
| regex_dna      | 252 ms                                                                      | 236 ms: 1.07x faster                                                     |
| regex_compile  | 153 ms                                                                      | 150 ms: 1.02x faster                                                     |
| regex_effbot   | 3.58 ms                                                                     | 3.60 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict          | 33.0 us                                                                     | 29.8 us: 1.11x faster                                                    |
| pickle_list          | 4.61 us                                                                     | 4.30 us: 1.07x faster                                                    |
| unpickle             | 15.8 us                                                                     | 14.8 us: 1.06x faster                                                    |
| pickle               | 10.8 us                                                                     | 10.3 us: 1.05x faster                                                    |
| xml_etree_generate   | 79.7 ms                                                                     | 78.8 ms: 1.01x faster                                                    |
| pickle_pure_python   | 327 us                                                                      | 325 us: 1.01x faster                                                     |
| json_loads           | 23.9 us                                                                     | 23.8 us: 1.01x faster                                                    |
| unpickle_pure_python | 218 us                                                                      | 219 us: 1.00x slower                                                     |
| unpickle_list        | 4.65 us                                                                     | 4.71 us: 1.01x slower                                                    |
| tomli_loads          | 2.12 sec                                                                    | 2.20 sec: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                                       | 1.02x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_process, json_dumps, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.19 ms                                                                     | 9.15 ms: 1.00x faster                                                    |
| genshi_text     | 29.4 ms                                                                     | 29.8 ms: 1.01x slower                                                    |
| genshi_xml      | 63.9 ms                                                                     | 66.2 ms: 1.04x slower                                                    |
| django_template | 41.9 ms                                                                     | 46.0 ms: 1.10x slower                                                    |
| Geometric mean  | (ref)                                                                       | 1.04x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict              | 33.0 us                                                                     | 29.8 us: 1.11x faster                                                    |
| gc_traversal             | 4.64 ms                                                                     | 4.31 ms: 1.08x faster                                                    |
| regex_v8                 | 26.7 ms                                                                     | 24.8 ms: 1.07x faster                                                    |
| pickle_list              | 4.61 us                                                                     | 4.30 us: 1.07x faster                                                    |
| regex_dna                | 252 ms                                                                      | 236 ms: 1.07x faster                                                     |
| unpickle                 | 15.8 us                                                                     | 14.8 us: 1.06x faster                                                    |
| pickle                   | 10.8 us                                                                     | 10.3 us: 1.05x faster                                                    |
| generators               | 39.0 ms                                                                     | 37.3 ms: 1.05x faster                                                    |
| nbody                    | 86.9 ms                                                                     | 83.3 ms: 1.04x faster                                                    |
| typing_runtime_protocols | 183 us                                                                      | 176 us: 1.04x faster                                                     |
| fannkuch                 | 358 ms                                                                      | 346 ms: 1.04x faster                                                     |
| sqlglot_transpile        | 1.99 ms                                                                     | 1.94 ms: 1.03x faster                                                    |
| docutils                 | 3.23 sec                                                                    | 3.17 sec: 1.02x faster                                                   |
| regex_compile            | 153 ms                                                                      | 150 ms: 1.02x faster                                                     |
| deepcopy                 | 306 us                                                                      | 300 us: 1.02x faster                                                     |
| sympy_integrate          | 27.4 ms                                                                     | 27.0 ms: 1.02x faster                                                    |
| pprint_safe_repr         | 774 ms                                                                      | 762 ms: 1.02x faster                                                     |
| sympy_sum                | 174 ms                                                                      | 172 ms: 1.01x faster                                                     |
| comprehensions           | 19.0 us                                                                     | 18.7 us: 1.01x faster                                                    |
| logging_silent           | 99.3 ns                                                                     | 98.1 ns: 1.01x faster                                                    |
| deepcopy_memo            | 27.6 us                                                                     | 27.3 us: 1.01x faster                                                    |
| async_generators         | 386 ms                                                                      | 382 ms: 1.01x faster                                                     |
| sympy_str                | 322 ms                                                                      | 318 ms: 1.01x faster                                                     |
| crypto_pyaes             | 70.9 ms                                                                     | 70.0 ms: 1.01x faster                                                    |
| sqlglot_parse            | 1.53 ms                                                                     | 1.51 ms: 1.01x faster                                                    |
| xml_etree_generate       | 79.7 ms                                                                     | 78.8 ms: 1.01x faster                                                    |
| float                    | 76.0 ms                                                                     | 75.3 ms: 1.01x faster                                                    |
| hexiom                   | 7.15 ms                                                                     | 7.09 ms: 1.01x faster                                                    |
| mdp                      | 2.62 sec                                                                    | 2.60 sec: 1.01x faster                                                   |
| pickle_pure_python       | 327 us                                                                      | 325 us: 1.01x faster                                                     |
| bpe_tokeniser            | 4.78 sec                                                                    | 4.75 sec: 1.01x faster                                                   |
| spectral_norm            | 83.3 ms                                                                     | 82.8 ms: 1.01x faster                                                    |
| json_loads               | 23.9 us                                                                     | 23.8 us: 1.01x faster                                                    |
| 2to3                     | 317 ms                                                                      | 315 ms: 1.01x faster                                                     |
| pathlib                  | 15.9 ms                                                                     | 15.8 ms: 1.01x faster                                                    |
| mako                     | 9.19 ms                                                                     | 9.15 ms: 1.00x faster                                                    |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                    |
| pidigits                 | 251 ms                                                                      | 251 ms: 1.00x slower                                                     |
| regex_effbot             | 3.58 ms                                                                     | 3.60 ms: 1.00x slower                                                    |
| unpickle_pure_python     | 218 us                                                                      | 219 us: 1.00x slower                                                     |
| telco                    | 7.59 ms                                                                     | 7.63 ms: 1.00x slower                                                    |
| pyflate                  | 453 ms                                                                      | 456 ms: 1.01x slower                                                     |
| sympy_expand             | 531 ms                                                                      | 534 ms: 1.01x slower                                                     |
| scimark_fft              | 278 ms                                                                      | 280 ms: 1.01x slower                                                     |
| sqlite_synth             | 2.70 us                                                                     | 2.73 us: 1.01x slower                                                    |
| json                     | 5.14 ms                                                                     | 5.19 ms: 1.01x slower                                                    |
| dulwich_log              | 64.2 ms                                                                     | 64.8 ms: 1.01x slower                                                    |
| meteor_contest           | 133 ms                                                                      | 134 ms: 1.01x slower                                                     |
| unpickle_list            | 4.65 us                                                                     | 4.71 us: 1.01x slower                                                    |
| create_gc_cycles         | 1.88 ms                                                                     | 1.90 ms: 1.01x slower                                                    |
| pycparser                | 1.29 sec                                                                    | 1.31 sec: 1.01x slower                                                   |
| genshi_text              | 29.4 ms                                                                     | 29.8 ms: 1.01x slower                                                    |
| sqlglot_normalize        | 133 ms                                                                      | 136 ms: 1.02x slower                                                     |
| scimark_lu               | 94.3 ms                                                                     | 96.0 ms: 1.02x slower                                                    |
| html5lib                 | 71.8 ms                                                                     | 73.1 ms: 1.02x slower                                                    |
| raytrace                 | 315 ms                                                                      | 323 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult  | 4.04 ms                                                                     | 4.15 ms: 1.03x slower                                                    |
| scimark_sor              | 102 ms                                                                      | 105 ms: 1.03x slower                                                     |
| thrift                   | 883 us                                                                      | 913 us: 1.03x slower                                                     |
| tomli_loads              | 2.12 sec                                                                    | 2.20 sec: 1.03x slower                                                   |
| genshi_xml               | 63.9 ms                                                                     | 66.2 ms: 1.04x slower                                                    |
| coroutines               | 21.2 ms                                                                     | 22.1 ms: 1.04x slower                                                    |
| go                       | 151 ms                                                                      | 158 ms: 1.05x slower                                                     |
| unpack_sequence          | 88.9 ns                                                                     | 94.8 ns: 1.07x slower                                                    |
| richards                 | 44.3 ms                                                                     | 47.3 ms: 1.07x slower                                                    |
| richards_super           | 51.1 ms                                                                     | 55.4 ms: 1.08x slower                                                    |
| django_template          | 41.9 ms                                                                     | 46.0 ms: 1.10x slower                                                    |
| bench_mp_pool            | 1.79 sec                                                                    | 3.26 sec: 1.82x slower                                                   |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (29): pylint, bench_thread_pool, asyncio_tcp, nqueens, xml_etree_process, async_tree_io_tg, pprint_pformat, async_tree_memoization_tg, asyncio_websockets, json_dumps, xml_etree_parse, scimark_monte_carlo, python_startup_no_site, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_io, async_tree_memoization, xml_etree_iterparse, sqlglot_optimize, deepcopy_reduce, logging_simple, coverage, tornado_http, deltablue, async_tree_cpu_io_mixed, chaos, logging_format, async_tree_none, async_tree_none_tg

# HPT report

- Reliability score: 54.37% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x