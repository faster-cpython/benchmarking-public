# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 0197884
- commit date: 2024-08-01
- overall geometric mean: 1.00x slower
- HPT reliability: 84.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                                | 284 ms: 1.04x slower                                                      |
| docutils       | 2.91 sec                                                              | 2.99 sec: 1.03x slower                                                    |
| html5lib       | 65.2 ms                                                               | 67.1 ms: 1.03x slower                                                     |
| tornado_http   | 92.3 ms                                                               | 94.3 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization | 426 ms                                                                | 415 ms: 1.03x faster                                                      |
| async_generators       | 466 ms                                                                | 458 ms: 1.02x faster                                                      |
| coroutines             | 22.6 ms                                                               | 22.9 ms: 1.01x slower                                                     |
| asyncio_tcp            | 490 ms                                                                | 505 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 71.6 ms                                                               | 70.4 ms: 1.02x faster                                                     |
| pidigits       | 186 ms                                                                | 187 ms: 1.01x slower                                                      |
| nbody          | 79.8 ms                                                               | 80.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.75 ms                                                               | 3.55 ms: 1.06x faster                                                     |
| regex_v8       | 25.2 ms                                                               | 24.0 ms: 1.05x faster                                                     |
| regex_dna      | 223 ms                                                                | 224 ms: 1.01x slower                                                      |
| regex_compile  | 133 ms                                                                | 145 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 99.8 ms                                                               | 98.3 ms: 1.02x faster                                                     |
| unpickle_pure_python | 215 us                                                                | 214 us: 1.00x faster                                                      |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| json_loads           | 27.9 us                                                               | 28.2 us: 1.01x slower                                                     |
| pickle_pure_python   | 297 us                                                                | 306 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_parse, tomli_loads, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.18 ms: 1.01x slower                                                     |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 24.7 ms                                                               | 23.7 ms: 1.04x faster                                                     |
| genshi_xml     | 54.5 ms                                                               | 53.3 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue                | 3.60 ms                                                               | 3.08 ms: 1.17x faster                                                     |
| deepcopy_memo            | 29.0 us                                                               | 27.3 us: 1.06x faster                                                     |
| regex_effbot             | 3.75 ms                                                               | 3.55 ms: 1.06x faster                                                     |
| regex_v8                 | 25.2 ms                                                               | 24.0 ms: 1.05x faster                                                     |
| logging_silent           | 106 ns                                                                | 101 ns: 1.05x faster                                                      |
| genshi_text              | 24.7 ms                                                               | 23.7 ms: 1.04x faster                                                     |
| deepcopy_reduce          | 2.82 us                                                               | 2.71 us: 1.04x faster                                                     |
| mdp                      | 2.63 sec                                                              | 2.54 sec: 1.03x faster                                                    |
| deepcopy                 | 273 us                                                                | 265 us: 1.03x faster                                                      |
| async_tree_memoization   | 426 ms                                                                | 415 ms: 1.03x faster                                                      |
| genshi_xml               | 54.5 ms                                                               | 53.3 ms: 1.02x faster                                                     |
| async_generators         | 466 ms                                                                | 458 ms: 1.02x faster                                                      |
| float                    | 71.6 ms                                                               | 70.4 ms: 1.02x faster                                                     |
| xml_etree_iterparse      | 99.8 ms                                                               | 98.3 ms: 1.02x faster                                                     |
| crypto_pyaes             | 67.4 ms                                                               | 66.4 ms: 1.01x faster                                                     |
| logging_simple           | 5.57 us                                                               | 5.51 us: 1.01x faster                                                     |
| coverage                 | 91.3 ms                                                               | 90.4 ms: 1.01x faster                                                     |
| thrift                   | 794 us                                                                | 787 us: 1.01x faster                                                      |
| nqueens                  | 86.4 ms                                                               | 85.7 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult  | 4.24 ms                                                               | 4.21 ms: 1.01x faster                                                     |
| scimark_fft              | 311 ms                                                                | 309 ms: 1.01x faster                                                      |
| scimark_sor              | 117 ms                                                                | 116 ms: 1.01x faster                                                      |
| unpickle_pure_python     | 215 us                                                                | 214 us: 1.00x faster                                                      |
| create_gc_cycles         | 1.76 ms                                                               | 1.76 ms: 1.00x slower                                                     |
| regex_dna                | 223 ms                                                                | 224 ms: 1.01x slower                                                      |
| python_startup_no_site   | 7.14 ms                                                               | 7.18 ms: 1.01x slower                                                     |
| pidigits                 | 186 ms                                                                | 187 ms: 1.01x slower                                                      |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| bpe_tokeniser            | 4.51 sec                                                              | 4.55 sec: 1.01x slower                                                    |
| nbody                    | 79.8 ms                                                               | 80.8 ms: 1.01x slower                                                     |
| sympy_expand             | 510 ms                                                                | 517 ms: 1.01x slower                                                      |
| coroutines               | 22.6 ms                                                               | 22.9 ms: 1.01x slower                                                     |
| pprint_safe_repr         | 738 ms                                                                | 748 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 113 ms                                                                | 114 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 168 us                                                                | 171 us: 1.01x slower                                                      |
| json_loads               | 27.9 us                                                               | 28.2 us: 1.01x slower                                                     |
| fannkuch                 | 369 ms                                                                | 375 ms: 1.01x slower                                                      |
| pyflate                  | 433 ms                                                                | 440 ms: 1.02x slower                                                      |
| comprehensions           | 16.2 us                                                               | 16.5 us: 1.02x slower                                                     |
| raytrace                 | 271 ms                                                                | 276 ms: 1.02x slower                                                      |
| gc_traversal             | 3.74 ms                                                               | 3.82 ms: 1.02x slower                                                     |
| sympy_integrate          | 22.6 ms                                                               | 23.1 ms: 1.02x slower                                                     |
| tornado_http             | 92.3 ms                                                               | 94.3 ms: 1.02x slower                                                     |
| scimark_monte_carlo      | 60.9 ms                                                               | 62.6 ms: 1.03x slower                                                     |
| docutils                 | 2.91 sec                                                              | 2.99 sec: 1.03x slower                                                    |
| html5lib                 | 65.2 ms                                                               | 67.1 ms: 1.03x slower                                                     |
| go                       | 146 ms                                                                | 150 ms: 1.03x slower                                                      |
| asyncio_tcp              | 490 ms                                                                | 505 ms: 1.03x slower                                                      |
| meteor_contest           | 105 ms                                                                | 108 ms: 1.03x slower                                                      |
| sqlglot_parse            | 1.30 ms                                                               | 1.34 ms: 1.03x slower                                                     |
| pprint_pformat           | 1.51 sec                                                              | 1.56 sec: 1.03x slower                                                    |
| pickle_pure_python       | 297 us                                                                | 306 us: 1.03x slower                                                      |
| sympy_str                | 300 ms                                                                | 310 ms: 1.03x slower                                                      |
| 2to3                     | 274 ms                                                                | 284 ms: 1.04x slower                                                      |
| sqlglot_transpile        | 1.62 ms                                                               | 1.69 ms: 1.04x slower                                                     |
| sympy_sum                | 170 ms                                                                | 178 ms: 1.05x slower                                                      |
| sqlglot_optimize         | 55.8 ms                                                               | 58.6 ms: 1.05x slower                                                     |
| richards                 | 41.1 ms                                                               | 43.1 ms: 1.05x slower                                                     |
| richards_super           | 46.8 ms                                                               | 49.2 ms: 1.05x slower                                                     |
| regex_compile            | 133 ms                                                                | 145 ms: 1.09x slower                                                      |
| hexiom                   | 6.73 ms                                                               | 7.64 ms: 1.14x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (28): xml_etree_parse, telco, generators, tomli_loads, pycparser, async_tree_memoization_tg, scimark_lu, async_tree_io_tg, mako, logging_format, async_tree_io, xml_etree_process, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, dask, bench_thread_pool, spectral_norm, async_tree_none_tg, async_tree_none, bench_mp_pool, asyncio_tcp_ssl, json, chaos, asyncio_websockets, pathlib, django_template, xml_etree_generate, pylint

# HPT report

- Reliability score: 84.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x