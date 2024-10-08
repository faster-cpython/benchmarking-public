# Results vs. base

- fork: serhiy-storchaka
- ref: pickle_save_global3
- machine: linux-x86_64
- commit hash: 5efa5a5
- commit date: 2024-07-30
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                | 263 ms: 1.00x slower                                                             |
| docutils       | 2.71 sec                                                              | 2.73 sec: 1.01x slower                                                           |
| html5lib       | 63.4 ms                                                               | 65.8 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl         | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                           |
| asyncio_tcp             | 484 ms                                                                | 487 ms: 1.01x slower                                                             |
| async_tree_none         | 320 ms                                                                | 324 ms: 1.01x slower                                                             |
| async_generators        | 437 ms                                                                | 443 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed | 554 ms                                                                | 567 ms: 1.02x slower                                                             |
| coroutines              | 22.3 ms                                                               | 22.9 ms: 1.03x slower                                                            |
| async_tree_memoization  | 396 ms                                                                | 425 ms: 1.07x slower                                                             |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                                                     |

Benchmark hidden because not significant (6): async_tree_none_tg, asyncio_websockets, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                                             |
| float          | 77.2 ms                                                               | 78.6 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                | 130 ms: 1.01x slower                                                             |
| regex_effbot   | 3.74 ms                                                               | 3.83 ms: 1.03x slower                                                            |
| regex_dna      | 221 ms                                                                | 227 ms: 1.03x slower                                                             |
| regex_v8       | 25.1 ms                                                               | 26.4 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_process    | 59.9 ms                                                               | 58.6 ms: 1.02x faster                                                            |
| xml_etree_generate   | 86.6 ms                                                               | 84.9 ms: 1.02x faster                                                            |
| json_dumps           | 10.5 ms                                                               | 10.3 ms: 1.02x faster                                                            |
| tomli_loads          | 2.06 sec                                                              | 2.04 sec: 1.01x faster                                                           |
| json_loads           | 27.9 us                                                               | 27.8 us: 1.00x faster                                                            |
| pickle_pure_python   | 301 us                                                                | 302 us: 1.00x slower                                                             |
| xml_etree_iterparse  | 104 ms                                                                | 105 ms: 1.01x slower                                                             |
| unpickle_pure_python | 209 us                                                                | 213 us: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                            |
| python_startup_no_site | 7.05 ms                                                               | 7.04 ms: 1.00x faster                                                            |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                            |
| mako            | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                            |
| genshi_xml      | 50.6 ms                                                               | 50.2 ms: 1.01x faster                                                            |
| django_template | 34.3 ms                                                               | 35.0 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                      | 2.68 sec                                                              | 2.52 sec: 1.06x faster                                                           |
| scimark_sparse_mat_mult  | 4.73 ms                                                               | 4.51 ms: 1.05x faster                                                            |
| json                     | 5.16 ms                                                               | 5.04 ms: 1.02x faster                                                            |
| xml_etree_process        | 59.9 ms                                                               | 58.6 ms: 1.02x faster                                                            |
| typing_runtime_protocols | 165 us                                                                | 161 us: 1.02x faster                                                             |
| xml_etree_generate       | 86.6 ms                                                               | 84.9 ms: 1.02x faster                                                            |
| json_dumps               | 10.5 ms                                                               | 10.3 ms: 1.02x faster                                                            |
| sqlglot_normalize        | 108 ms                                                                | 107 ms: 1.02x faster                                                             |
| genshi_text              | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                            |
| tomli_loads              | 2.06 sec                                                              | 2.04 sec: 1.01x faster                                                           |
| mako                     | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                            |
| spectral_norm            | 109 ms                                                                | 109 ms: 1.01x faster                                                             |
| genshi_xml               | 50.6 ms                                                               | 50.2 ms: 1.01x faster                                                            |
| pprint_pformat           | 1.53 sec                                                              | 1.52 sec: 1.01x faster                                                           |
| sqlglot_optimize         | 53.5 ms                                                               | 53.1 ms: 1.01x faster                                                            |
| json_loads               | 27.9 us                                                               | 27.8 us: 1.00x faster                                                            |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                            |
| python_startup_no_site   | 7.05 ms                                                               | 7.04 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                           |
| pidigits                 | 187 ms                                                                | 188 ms: 1.00x slower                                                             |
| bench_thread_pool        | 783 us                                                                | 786 us: 1.00x slower                                                             |
| 2to3                     | 262 ms                                                                | 263 ms: 1.00x slower                                                             |
| pickle_pure_python       | 301 us                                                                | 302 us: 1.00x slower                                                             |
| deepcopy                 | 260 us                                                                | 261 us: 1.00x slower                                                             |
| richards_super           | 51.6 ms                                                               | 51.8 ms: 1.01x slower                                                            |
| chaos                    | 58.2 ms                                                               | 58.6 ms: 1.01x slower                                                            |
| docutils                 | 2.71 sec                                                              | 2.73 sec: 1.01x slower                                                           |
| asyncio_tcp              | 484 ms                                                                | 487 ms: 1.01x slower                                                             |
| raytrace                 | 256 ms                                                                | 258 ms: 1.01x slower                                                             |
| scimark_sor              | 126 ms                                                                | 127 ms: 1.01x slower                                                             |
| nqueens                  | 79.0 ms                                                               | 79.6 ms: 1.01x slower                                                            |
| gc_traversal             | 3.53 ms                                                               | 3.56 ms: 1.01x slower                                                            |
| regex_compile            | 129 ms                                                                | 130 ms: 1.01x slower                                                             |
| bpe_tokeniser            | 4.80 sec                                                              | 4.84 sec: 1.01x slower                                                           |
| scimark_monte_carlo      | 66.5 ms                                                               | 67.2 ms: 1.01x slower                                                            |
| go                       | 138 ms                                                                | 140 ms: 1.01x slower                                                             |
| sqlglot_parse            | 1.27 ms                                                               | 1.28 ms: 1.01x slower                                                            |
| xml_etree_iterparse      | 104 ms                                                                | 105 ms: 1.01x slower                                                             |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                             |
| async_tree_none          | 320 ms                                                                | 324 ms: 1.01x slower                                                             |
| scimark_fft              | 354 ms                                                                | 359 ms: 1.01x slower                                                             |
| async_generators         | 437 ms                                                                | 443 ms: 1.01x slower                                                             |
| generators               | 28.1 ms                                                               | 28.5 ms: 1.01x slower                                                            |
| float                    | 77.2 ms                                                               | 78.6 ms: 1.02x slower                                                            |
| fannkuch                 | 396 ms                                                                | 403 ms: 1.02x slower                                                             |
| deepcopy_reduce          | 2.69 us                                                               | 2.74 us: 1.02x slower                                                            |
| deepcopy_memo            | 29.1 us                                                               | 29.7 us: 1.02x slower                                                            |
| unpickle_pure_python     | 209 us                                                                | 213 us: 1.02x slower                                                             |
| django_template          | 34.3 ms                                                               | 35.0 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed  | 554 ms                                                                | 567 ms: 1.02x slower                                                             |
| pathlib                  | 15.7 ms                                                               | 16.1 ms: 1.02x slower                                                            |
| regex_effbot             | 3.74 ms                                                               | 3.83 ms: 1.03x slower                                                            |
| pyflate                  | 465 ms                                                                | 477 ms: 1.03x slower                                                             |
| regex_dna                | 221 ms                                                                | 227 ms: 1.03x slower                                                             |
| hexiom                   | 6.09 ms                                                               | 6.26 ms: 1.03x slower                                                            |
| coroutines               | 22.3 ms                                                               | 22.9 ms: 1.03x slower                                                            |
| deltablue                | 3.13 ms                                                               | 3.23 ms: 1.03x slower                                                            |
| pycparser                | 1.13 sec                                                              | 1.17 sec: 1.04x slower                                                           |
| html5lib                 | 63.4 ms                                                               | 65.8 ms: 1.04x slower                                                            |
| comprehensions           | 16.2 us                                                               | 16.9 us: 1.04x slower                                                            |
| logging_silent           | 97.3 ns                                                               | 102 ns: 1.05x slower                                                             |
| regex_v8                 | 25.1 ms                                                               | 26.4 ms: 1.05x slower                                                            |
| async_tree_memoization   | 396 ms                                                                | 425 ms: 1.07x slower                                                             |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                     |

Benchmark hidden because not significant (26): scimark_lu, xml_etree_parse, sqlglot_transpile, sympy_sum, crypto_pyaes, logging_format, sympy_integrate, create_gc_cycles, thrift, logging_simple, bench_mp_pool, pprint_safe_repr, async_tree_none_tg, richards, tornado_http, pylint, coverage, asyncio_websockets, sympy_str, telco, nbody, sympy_expand, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20240730-3.14.0a0-d1a1bca/bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x