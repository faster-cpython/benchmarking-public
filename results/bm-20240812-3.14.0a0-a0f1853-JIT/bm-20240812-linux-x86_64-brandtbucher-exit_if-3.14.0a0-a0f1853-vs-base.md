# Results vs. base

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: a0f1853
- commit date: 2024-08-12
- overall geometric mean: 1.01x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 274 ms: 1.01x faster                                           |
| docutils       | 3.01 sec                                                              | 2.99 sec: 1.00x faster                                         |
| html5lib       | 66.7 ms                                                               | 66.1 ms: 1.01x faster                                          |
| tornado_http   | 94.0 ms                                                               | 92.3 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization | 428 ms                                                                | 412 ms: 1.04x faster                                           |
| asyncio_tcp            | 504 ms                                                                | 501 ms: 1.01x faster                                           |
| asyncio_tcp_ssl        | 1.82 sec                                                              | 1.81 sec: 1.00x faster                                         |
| async_generators       | 455 ms                                                                | 457 ms: 1.00x slower                                           |
| coroutines             | 22.9 ms                                                               | 23.3 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 80.0 ms: 1.02x faster                                          |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                               | 24.4 ms: 1.06x faster                                          |
| regex_effbot   | 3.76 ms                                                               | 3.70 ms: 1.02x faster                                          |
| regex_compile  | 138 ms                                                                | 136 ms: 1.02x faster                                           |
| regex_dna      | 218 ms                                                                | 217 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 308 us                                                                | 300 us: 1.03x faster                                           |
| unpickle_pure_python | 215 us                                                                | 210 us: 1.02x faster                                           |
| json_dumps           | 10.3 ms                                                               | 10.2 ms: 1.02x faster                                          |
| tomli_loads          | 1.92 sec                                                              | 1.90 sec: 1.01x faster                                         |
| xml_etree_process    | 56.7 ms                                                               | 56.4 ms: 1.01x faster                                          |
| xml_etree_generate   | 81.0 ms                                                               | 80.6 ms: 1.00x faster                                          |
| json_loads           | 27.9 us                                                               | 27.7 us: 1.00x faster                                          |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                          |
| python_startup_no_site | 7.18 ms                                                               | 7.13 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 34.9 ms                                                               | 35.2 ms: 1.01x slower                                          |
| mako            | 9.69 ms                                                               | 9.82 ms: 1.01x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8                 | 26.0 ms                                                               | 24.4 ms: 1.06x faster                                          |
| async_tree_memoization   | 428 ms                                                                | 412 ms: 1.04x faster                                           |
| raytrace                 | 273 ms                                                                | 264 ms: 1.03x faster                                           |
| gc_traversal             | 3.89 ms                                                               | 3.76 ms: 1.03x faster                                          |
| comprehensions           | 16.7 us                                                               | 16.2 us: 1.03x faster                                          |
| fannkuch                 | 375 ms                                                                | 365 ms: 1.03x faster                                           |
| pickle_pure_python       | 308 us                                                                | 300 us: 1.03x faster                                           |
| unpickle_pure_python     | 215 us                                                                | 210 us: 1.02x faster                                           |
| pathlib                  | 16.4 ms                                                               | 16.0 ms: 1.02x faster                                          |
| scimark_lu               | 111 ms                                                                | 109 ms: 1.02x faster                                           |
| nbody                    | 81.6 ms                                                               | 80.0 ms: 1.02x faster                                          |
| tornado_http             | 94.0 ms                                                               | 92.3 ms: 1.02x faster                                          |
| regex_effbot             | 3.76 ms                                                               | 3.70 ms: 1.02x faster                                          |
| hexiom                   | 6.85 ms                                                               | 6.73 ms: 1.02x faster                                          |
| scimark_monte_carlo      | 63.0 ms                                                               | 62.0 ms: 1.02x faster                                          |
| json_dumps               | 10.3 ms                                                               | 10.2 ms: 1.02x faster                                          |
| logging_format           | 6.06 us                                                               | 5.97 us: 1.02x faster                                          |
| regex_compile            | 138 ms                                                                | 136 ms: 1.02x faster                                           |
| crypto_pyaes             | 66.6 ms                                                               | 65.7 ms: 1.01x faster                                          |
| bpe_tokeniser            | 4.56 sec                                                              | 4.49 sec: 1.01x faster                                         |
| thrift                   | 797 us                                                                | 786 us: 1.01x faster                                           |
| logging_simple           | 5.49 us                                                               | 5.42 us: 1.01x faster                                          |
| go                       | 146 ms                                                                | 144 ms: 1.01x faster                                           |
| sympy_integrate          | 23.0 ms                                                               | 22.7 ms: 1.01x faster                                          |
| typing_runtime_protocols | 170 us                                                                | 168 us: 1.01x faster                                           |
| telco                    | 7.92 ms                                                               | 7.83 ms: 1.01x faster                                          |
| richards_super           | 46.6 ms                                                               | 46.1 ms: 1.01x faster                                          |
| create_gc_cycles         | 1.78 ms                                                               | 1.76 ms: 1.01x faster                                          |
| sqlglot_transpile        | 1.65 ms                                                               | 1.64 ms: 1.01x faster                                          |
| bench_thread_pool        | 821 us                                                                | 813 us: 1.01x faster                                           |
| generators               | 33.5 ms                                                               | 33.2 ms: 1.01x faster                                          |
| tomli_loads              | 1.92 sec                                                              | 1.90 sec: 1.01x faster                                         |
| html5lib                 | 66.7 ms                                                               | 66.1 ms: 1.01x faster                                          |
| sqlglot_parse            | 1.30 ms                                                               | 1.29 ms: 1.01x faster                                          |
| sympy_str                | 300 ms                                                                | 298 ms: 1.01x faster                                           |
| richards                 | 40.3 ms                                                               | 40.0 ms: 1.01x faster                                          |
| deltablue                | 3.14 ms                                                               | 3.11 ms: 1.01x faster                                          |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                          |
| python_startup_no_site   | 7.18 ms                                                               | 7.13 ms: 1.01x faster                                          |
| xml_etree_process        | 56.7 ms                                                               | 56.4 ms: 1.01x faster                                          |
| asyncio_tcp              | 504 ms                                                                | 501 ms: 1.01x faster                                           |
| 2to3                     | 276 ms                                                                | 274 ms: 1.01x faster                                           |
| sympy_expand             | 506 ms                                                                | 504 ms: 1.01x faster                                           |
| xml_etree_generate       | 81.0 ms                                                               | 80.6 ms: 1.00x faster                                          |
| regex_dna                | 218 ms                                                                | 217 ms: 1.00x faster                                           |
| json_loads               | 27.9 us                                                               | 27.7 us: 1.00x faster                                          |
| docutils                 | 3.01 sec                                                              | 2.99 sec: 1.00x faster                                         |
| deepcopy_memo            | 26.4 us                                                               | 26.3 us: 1.00x faster                                          |
| logging_silent           | 98.3 ns                                                               | 98.0 ns: 1.00x faster                                          |
| meteor_contest           | 105 ms                                                                | 105 ms: 1.00x faster                                           |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x faster                                           |
| asyncio_tcp_ssl          | 1.82 sec                                                              | 1.81 sec: 1.00x faster                                         |
| async_generators         | 455 ms                                                                | 457 ms: 1.00x slower                                           |
| django_template          | 34.9 ms                                                               | 35.2 ms: 1.01x slower                                          |
| sqlglot_normalize        | 112 ms                                                                | 113 ms: 1.01x slower                                           |
| deepcopy                 | 258 us                                                                | 261 us: 1.01x slower                                           |
| mako                     | 9.69 ms                                                               | 9.82 ms: 1.01x slower                                          |
| scimark_sparse_mat_mult  | 4.42 ms                                                               | 4.50 ms: 1.02x slower                                          |
| coroutines               | 22.9 ms                                                               | 23.3 ms: 1.02x slower                                          |
| pyflate                  | 434 ms                                                                | 452 ms: 1.04x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (29): pprint_pformat, pylint, async_tree_memoization_tg, async_tree_none_tg, pprint_safe_repr, xml_etree_parse, chaos, async_tree_io_tg, coverage, async_tree_cpu_io_mixed_tg, scimark_sor, async_tree_cpu_io_mixed, spectral_norm, bench_mp_pool, nqueens, float, mdp, scimark_fft, sqlglot_optimize, genshi_xml, xml_etree_iterparse, sympy_sum, asyncio_websockets, async_tree_none, pycparser, async_tree_io, genshi_text, json, deepcopy_reduce

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x