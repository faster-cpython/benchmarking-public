# Results vs. base

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.00x faster
- HPT reliability: 96.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 273 ms: 1.01x slower                                                            |
| html5lib       | 65.1 ms                                                               | 64.2 ms: 1.01x faster                                                           |
| tornado_http   | 92.8 ms                                                               | 92.1 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization | 424 ms                                                                | 410 ms: 1.03x faster                                                            |
| async_generators       | 463 ms                                                                | 456 ms: 1.01x faster                                                            |
| coroutines             | 22.5 ms                                                               | 22.8 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_none, asyncio_tcp, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 70.9 ms                                                               | 70.4 ms: 1.01x faster                                                           |
| nbody          | 79.9 ms                                                               | 79.4 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.70 ms: 1.03x faster                                                           |
| regex_v8       | 25.3 ms                                                               | 24.8 ms: 1.02x faster                                                           |
| regex_compile  | 133 ms                                                                | 134 ms: 1.00x slower                                                            |
| regex_dna      | 223 ms                                                                | 227 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process | 56.4 ms                                                               | 55.3 ms: 1.02x faster                                                           |
| json_loads        | 27.9 us                                                               | 27.8 us: 1.01x faster                                                           |
| Geometric mean    | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (7): tomli_loads, xml_etree_generate, xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.16 ms: 1.00x faster                                                           |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.2 ms                                                               | 35.9 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240801-linux-x86_64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                      | 2.76 sec                                                              | 2.55 sec: 1.08x faster                                                          |
| async_tree_memoization   | 424 ms                                                                | 410 ms: 1.03x faster                                                            |
| regex_effbot             | 3.81 ms                                                               | 3.70 ms: 1.03x faster                                                           |
| scimark_fft              | 315 ms                                                                | 308 ms: 1.02x faster                                                            |
| typing_runtime_protocols | 174 us                                                                | 170 us: 1.02x faster                                                            |
| logging_format           | 6.13 us                                                               | 6.00 us: 1.02x faster                                                           |
| xml_etree_process        | 56.4 ms                                                               | 55.3 ms: 1.02x faster                                                           |
| logging_simple           | 5.58 us                                                               | 5.47 us: 1.02x faster                                                           |
| regex_v8                 | 25.3 ms                                                               | 24.8 ms: 1.02x faster                                                           |
| richards_super           | 47.2 ms                                                               | 46.5 ms: 1.02x faster                                                           |
| async_generators         | 463 ms                                                                | 456 ms: 1.01x faster                                                            |
| html5lib                 | 65.1 ms                                                               | 64.2 ms: 1.01x faster                                                           |
| comprehensions           | 16.3 us                                                               | 16.1 us: 1.01x faster                                                           |
| go                       | 144 ms                                                                | 142 ms: 1.01x faster                                                            |
| scimark_sor              | 128 ms                                                                | 127 ms: 1.01x faster                                                            |
| sqlglot_transpile        | 1.63 ms                                                               | 1.61 ms: 1.01x faster                                                           |
| spectral_norm            | 103 ms                                                                | 102 ms: 1.01x faster                                                            |
| sympy_expand             | 507 ms                                                                | 503 ms: 1.01x faster                                                            |
| tornado_http             | 92.8 ms                                                               | 92.1 ms: 1.01x faster                                                           |
| django_template          | 36.2 ms                                                               | 35.9 ms: 1.01x faster                                                           |
| float                    | 70.9 ms                                                               | 70.4 ms: 1.01x faster                                                           |
| nbody                    | 79.9 ms                                                               | 79.4 ms: 1.01x faster                                                           |
| json_loads               | 27.9 us                                                               | 27.8 us: 1.01x faster                                                           |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                           |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                            |
| create_gc_cycles         | 1.77 ms                                                               | 1.77 ms: 1.00x faster                                                           |
| python_startup_no_site   | 7.17 ms                                                               | 7.16 ms: 1.00x faster                                                           |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| fannkuch                 | 363 ms                                                                | 364 ms: 1.00x slower                                                            |
| regex_compile            | 133 ms                                                                | 134 ms: 1.00x slower                                                            |
| 2to3                     | 272 ms                                                                | 273 ms: 1.01x slower                                                            |
| bpe_tokeniser            | 4.49 sec                                                              | 4.51 sec: 1.01x slower                                                          |
| bench_thread_pool        | 815 us                                                                | 821 us: 1.01x slower                                                            |
| sympy_integrate          | 22.3 ms                                                               | 22.6 ms: 1.01x slower                                                           |
| scimark_lu               | 123 ms                                                                | 125 ms: 1.01x slower                                                            |
| crypto_pyaes             | 67.1 ms                                                               | 67.9 ms: 1.01x slower                                                           |
| coroutines               | 22.5 ms                                                               | 22.8 ms: 1.01x slower                                                           |
| gc_traversal             | 3.76 ms                                                               | 3.81 ms: 1.01x slower                                                           |
| thrift                   | 782 us                                                                | 796 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult  | 4.31 ms                                                               | 4.39 ms: 1.02x slower                                                           |
| json                     | 5.12 ms                                                               | 5.22 ms: 1.02x slower                                                           |
| regex_dna                | 223 ms                                                                | 227 ms: 1.02x slower                                                            |
| generators               | 32.4 ms                                                               | 33.3 ms: 1.03x slower                                                           |
| telco                    | 7.82 ms                                                               | 8.07 ms: 1.03x slower                                                           |
| pprint_pformat           | 1.45 sec                                                              | 1.50 sec: 1.04x slower                                                          |
| pprint_safe_repr         | 706 ms                                                                | 733 ms: 1.04x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (44): async_tree_memoization_tg, async_tree_none_tg, pyflate, tomli_loads, nqueens, xml_etree_generate, async_tree_io, async_tree_io_tg, xml_etree_parse, coverage, deepcopy_memo, richards, sqlglot_parse, async_tree_cpu_io_mixed_tg, sqlglot_normalize, docutils, genshi_text, unpickle_pure_python, bench_mp_pool, asyncio_tcp_ssl, hexiom, raytrace, xml_etree_iterparse, chaos, pickle_pure_python, scimark_monte_carlo, sqlglot_optimize, async_tree_none, mako, dask, asyncio_tcp, sympy_str, pylint, asyncio_websockets, deltablue, json_dumps, async_tree_cpu_io_mixed, pycparser, meteor_contest, sympy_sum, logging_silent, genshi_xml, deepcopy, deepcopy_reduce

# HPT report

- Reliability score: 96.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x