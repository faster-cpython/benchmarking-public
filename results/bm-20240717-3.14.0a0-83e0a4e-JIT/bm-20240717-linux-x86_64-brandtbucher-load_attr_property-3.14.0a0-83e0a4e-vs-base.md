# Results vs. base

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 83e0a4e
- commit date: 2024-07-17
- overall geometric mean: 1.00x slower
- HPT reliability: 84.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 270 ms: 1.00x faster                                                      |
| docutils       | 2.84 sec                                                              | 2.87 sec: 1.01x slower                                                    |
| tornado_http   | 93.1 ms                                                               | 92.5 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                      |
| nbody          | 79.6 ms                                                               | 80.7 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                | 221 ms: 1.01x faster                                                      |
| regex_compile  | 133 ms                                                                | 134 ms: 1.01x slower                                                      |
| regex_effbot   | 3.58 ms                                                               | 3.77 ms: 1.05x slower                                                     |
| regex_v8       | 24.2 ms                                                               | 25.9 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                                | 215 us: 1.01x faster                                                      |
| xml_etree_generate   | 81.4 ms                                                               | 80.9 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 99.4 ms                                                               | 99.1 ms: 1.00x faster                                                     |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| json_loads           | 27.5 us                                                               | 27.7 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, pickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                               | 7.15 ms: 1.00x faster                                                     |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                               | 35.2 ms: 1.01x faster                                                     |
| mako            | 9.75 ms                                                               | 9.71 ms: 1.00x faster                                                     |
| genshi_xml      | 55.4 ms                                                               | 56.2 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_fft              | 317 ms                                                                | 307 ms: 1.03x faster                                                      |
| scimark_sor              | 130 ms                                                                | 127 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult  | 4.48 ms                                                               | 4.37 ms: 1.02x faster                                                     |
| deepcopy_reduce          | 2.75 us                                                               | 2.69 us: 1.02x faster                                                     |
| logging_format           | 6.18 us                                                               | 6.06 us: 1.02x faster                                                     |
| dulwich_log              | 67.2 ms                                                               | 66.1 ms: 1.02x faster                                                     |
| pprint_safe_repr         | 712 ms                                                                | 702 ms: 1.02x faster                                                      |
| raytrace                 | 271 ms                                                                | 267 ms: 1.01x faster                                                      |
| regex_dna                | 225 ms                                                                | 221 ms: 1.01x faster                                                      |
| richards_super           | 48.0 ms                                                               | 47.4 ms: 1.01x faster                                                     |
| unpickle_pure_python     | 218 us                                                                | 215 us: 1.01x faster                                                      |
| logging_silent           | 106 ns                                                                | 105 ns: 1.01x faster                                                      |
| deepcopy                 | 275 us                                                                | 272 us: 1.01x faster                                                      |
| logging_simple           | 5.56 us                                                               | 5.50 us: 1.01x faster                                                     |
| json                     | 5.11 ms                                                               | 5.07 ms: 1.01x faster                                                     |
| scimark_monte_carlo      | 61.2 ms                                                               | 60.6 ms: 1.01x faster                                                     |
| django_template          | 35.5 ms                                                               | 35.2 ms: 1.01x faster                                                     |
| typing_runtime_protocols | 167 us                                                                | 166 us: 1.01x faster                                                      |
| pathlib                  | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                     |
| tornado_http             | 93.1 ms                                                               | 92.5 ms: 1.01x faster                                                     |
| generators               | 29.4 ms                                                               | 29.2 ms: 1.01x faster                                                     |
| asyncio_tcp              | 507 ms                                                                | 504 ms: 1.01x faster                                                      |
| deltablue                | 3.57 ms                                                               | 3.55 ms: 1.01x faster                                                     |
| xml_etree_generate       | 81.4 ms                                                               | 80.9 ms: 1.01x faster                                                     |
| sqlglot_transpile        | 1.59 ms                                                               | 1.58 ms: 1.00x faster                                                     |
| mako                     | 9.75 ms                                                               | 9.71 ms: 1.00x faster                                                     |
| 2to3                     | 271 ms                                                                | 270 ms: 1.00x faster                                                      |
| xml_etree_iterparse      | 99.4 ms                                                               | 99.1 ms: 1.00x faster                                                     |
| python_startup_no_site   | 7.16 ms                                                               | 7.15 ms: 1.00x faster                                                     |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x faster                                                      |
| bench_mp_pool            | 24.0 ms                                                               | 24.0 ms: 1.00x slower                                                     |
| create_gc_cycles         | 1.77 ms                                                               | 1.78 ms: 1.00x slower                                                     |
| hexiom                   | 6.55 ms                                                               | 6.58 ms: 1.00x slower                                                     |
| go                       | 143 ms                                                                | 144 ms: 1.01x slower                                                      |
| regex_compile            | 133 ms                                                                | 134 ms: 1.01x slower                                                      |
| sympy_expand             | 491 ms                                                                | 494 ms: 1.01x slower                                                      |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| sqlglot_optimize         | 55.2 ms                                                               | 55.6 ms: 1.01x slower                                                     |
| json_loads               | 27.5 us                                                               | 27.7 us: 1.01x slower                                                     |
| fannkuch                 | 359 ms                                                                | 363 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 111 ms                                                                | 112 ms: 1.01x slower                                                      |
| docutils                 | 2.84 sec                                                              | 2.87 sec: 1.01x slower                                                    |
| bpe_tokeniser            | 4.76 sec                                                              | 4.82 sec: 1.01x slower                                                    |
| coverage                 | 93.7 ms                                                               | 94.9 ms: 1.01x slower                                                     |
| coroutines               | 22.4 ms                                                               | 22.7 ms: 1.01x slower                                                     |
| genshi_xml               | 55.4 ms                                                               | 56.2 ms: 1.01x slower                                                     |
| nbody                    | 79.6 ms                                                               | 80.7 ms: 1.01x slower                                                     |
| sympy_integrate          | 21.8 ms                                                               | 22.2 ms: 1.02x slower                                                     |
| deepcopy_memo            | 28.2 us                                                               | 28.7 us: 1.02x slower                                                     |
| comprehensions           | 16.4 us                                                               | 16.7 us: 1.02x slower                                                     |
| spectral_norm            | 102 ms                                                                | 104 ms: 1.02x slower                                                      |
| meteor_contest           | 105 ms                                                                | 107 ms: 1.02x slower                                                      |
| pyflate                  | 432 ms                                                                | 442 ms: 1.02x slower                                                      |
| mdp                      | 2.53 sec                                                              | 2.60 sec: 1.03x slower                                                    |
| pycparser                | 1.13 sec                                                              | 1.17 sec: 1.04x slower                                                    |
| regex_effbot             | 3.58 ms                                                               | 3.77 ms: 1.05x slower                                                     |
| gc_traversal             | 3.65 ms                                                               | 3.88 ms: 1.06x slower                                                     |
| regex_v8                 | 24.2 ms                                                               | 25.9 ms: 1.07x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (32): async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization, chaos, async_tree_cpu_io_mixed, async_tree_io_tg, nqueens, async_tree_memoization_tg, xml_etree_parse, genshi_text, scimark_lu, async_tree_cpu_io_mixed_tg, xml_etree_process, asyncio_websockets, dask, sqlglot_parse, crypto_pyaes, bench_thread_pool, richards, html5lib, pickle_pure_python, asyncio_tcp_ssl, pylint, sympy_sum, sympy_str, async_generators, telco, thrift, float, tomli_loads, pprint_pformat

# HPT report

- Reliability score: 84.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x