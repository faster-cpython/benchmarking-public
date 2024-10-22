# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6f4aaba
- commit date: 2024-07-15
- overall geometric mean: 1.01x slower
- HPT reliability: 96.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 272 ms: 1.00x slower                                                        |
| docutils       | 2.84 sec                                                              | 2.88 sec: 1.01x slower                                                      |
| html5lib       | 64.0 ms                                                               | 63.2 ms: 1.01x faster                                                       |
| tornado_http   | 93.1 ms                                                               | 93.5 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.01x slower                                                        |
| nbody          | 79.6 ms                                                               | 81.2 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                | 134 ms: 1.01x slower                                                        |
| regex_dna      | 225 ms                                                                | 229 ms: 1.02x slower                                                        |
| regex_v8       | 24.2 ms                                                               | 25.4 ms: 1.05x slower                                                       |
| regex_effbot   | 3.58 ms                                                               | 3.81 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                       |
| xml_etree_process    | 57.4 ms                                                               | 56.9 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 99.4 ms                                                               | 98.9 ms: 1.00x faster                                                       |
| json_loads           | 27.5 us                                                               | 27.9 us: 1.01x slower                                                       |
| unpickle_pure_python | 218 us                                                                | 226 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                               | 7.13 ms: 1.00x faster                                                       |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.75 ms                                                               | 9.74 ms: 1.00x faster                                                       |
| django_template | 35.5 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| genshi_xml      | 55.4 ms                                                               | 57.4 ms: 1.04x slower                                                       |
| genshi_text     | 24.8 ms                                                               | 25.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| bpe_tokeniser            | 4.76 sec                                                              | 4.60 sec: 1.03x faster                                                      |
| pprint_safe_repr         | 712 ms                                                                | 694 ms: 1.03x faster                                                        |
| scimark_fft              | 317 ms                                                                | 310 ms: 1.02x faster                                                        |
| gc_traversal             | 3.65 ms                                                               | 3.58 ms: 1.02x faster                                                       |
| create_gc_cycles         | 1.77 ms                                                               | 1.74 ms: 1.02x faster                                                       |
| richards_super           | 48.0 ms                                                               | 47.3 ms: 1.02x faster                                                       |
| async_generators         | 462 ms                                                                | 455 ms: 1.02x faster                                                        |
| html5lib                 | 64.0 ms                                                               | 63.2 ms: 1.01x faster                                                       |
| tomli_loads              | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| crypto_pyaes             | 67.9 ms                                                               | 67.0 ms: 1.01x faster                                                       |
| spectral_norm            | 102 ms                                                                | 101 ms: 1.01x faster                                                        |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                       |
| xml_etree_process        | 57.4 ms                                                               | 56.9 ms: 1.01x faster                                                       |
| raytrace                 | 271 ms                                                                | 269 ms: 1.01x faster                                                        |
| coroutines               | 22.4 ms                                                               | 22.2 ms: 1.01x faster                                                       |
| logging_simple           | 5.56 us                                                               | 5.53 us: 1.01x faster                                                       |
| xml_etree_iterparse      | 99.4 ms                                                               | 98.9 ms: 1.00x faster                                                       |
| python_startup_no_site   | 7.16 ms                                                               | 7.13 ms: 1.00x faster                                                       |
| mako                     | 9.75 ms                                                               | 9.74 ms: 1.00x faster                                                       |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| bench_thread_pool        | 832 us                                                                | 834 us: 1.00x slower                                                        |
| tornado_http             | 93.1 ms                                                               | 93.5 ms: 1.00x slower                                                       |
| 2to3                     | 271 ms                                                                | 272 ms: 1.00x slower                                                        |
| asyncio_tcp              | 507 ms                                                                | 509 ms: 1.00x slower                                                        |
| dulwich_log              | 67.2 ms                                                               | 67.5 ms: 1.01x slower                                                       |
| pidigits                 | 185 ms                                                                | 186 ms: 1.01x slower                                                        |
| hexiom                   | 6.55 ms                                                               | 6.59 ms: 1.01x slower                                                       |
| scimark_sor              | 130 ms                                                                | 131 ms: 1.01x slower                                                        |
| regex_compile            | 133 ms                                                                | 134 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.59 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| coverage                 | 93.7 ms                                                               | 94.5 ms: 1.01x slower                                                       |
| django_template          | 35.5 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| comprehensions           | 16.4 us                                                               | 16.5 us: 1.01x slower                                                       |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                        |
| sqlglot_parse            | 1.27 ms                                                               | 1.28 ms: 1.01x slower                                                       |
| thrift                   | 799 us                                                                | 808 us: 1.01x slower                                                        |
| sqlglot_normalize        | 111 ms                                                                | 113 ms: 1.01x slower                                                        |
| docutils                 | 2.84 sec                                                              | 2.88 sec: 1.01x slower                                                      |
| sqlglot_optimize         | 55.2 ms                                                               | 56.0 ms: 1.01x slower                                                       |
| json_loads               | 27.5 us                                                               | 27.9 us: 1.01x slower                                                       |
| generators               | 29.4 ms                                                               | 29.9 ms: 1.02x slower                                                       |
| json                     | 5.11 ms                                                               | 5.21 ms: 1.02x slower                                                       |
| sympy_str                | 292 ms                                                                | 298 ms: 1.02x slower                                                        |
| fannkuch                 | 359 ms                                                                | 367 ms: 1.02x slower                                                        |
| go                       | 143 ms                                                                | 146 ms: 1.02x slower                                                        |
| sympy_integrate          | 21.8 ms                                                               | 22.3 ms: 1.02x slower                                                       |
| nbody                    | 79.6 ms                                                               | 81.2 ms: 1.02x slower                                                       |
| sympy_sum                | 165 ms                                                                | 169 ms: 1.02x slower                                                        |
| regex_dna                | 225 ms                                                                | 229 ms: 1.02x slower                                                        |
| deepcopy_memo            | 28.2 us                                                               | 28.8 us: 1.02x slower                                                       |
| deltablue                | 3.57 ms                                                               | 3.65 ms: 1.02x slower                                                       |
| sympy_expand             | 491 ms                                                                | 503 ms: 1.02x slower                                                        |
| scimark_lu               | 124 ms                                                                | 127 ms: 1.03x slower                                                        |
| typing_runtime_protocols | 167 us                                                                | 172 us: 1.03x slower                                                        |
| genshi_xml               | 55.4 ms                                                               | 57.4 ms: 1.04x slower                                                       |
| unpickle_pure_python     | 218 us                                                                | 226 us: 1.04x slower                                                        |
| genshi_text              | 24.8 ms                                                               | 25.8 ms: 1.04x slower                                                       |
| pycparser                | 1.13 sec                                                              | 1.18 sec: 1.05x slower                                                      |
| regex_v8                 | 24.2 ms                                                               | 25.4 ms: 1.05x slower                                                       |
| regex_effbot             | 3.58 ms                                                               | 3.81 ms: 1.06x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (30): async_tree_io, scimark_sparse_mat_mult, chaos, async_tree_memoization, async_tree_memoization_tg, xml_etree_parse, xml_etree_generate, telco, async_tree_none, logging_format, deepcopy, float, pathlib, deepcopy_reduce, async_tree_io_tg, pickle_pure_python, mdp, bench_mp_pool, pyflate, richards, async_tree_none_tg, asyncio_websockets, scimark_monte_carlo, nqueens, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, pylint, dask, pprint_pformat, logging_silent

# HPT report

- Reliability score: 96.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x