# Results vs. base

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 84bca09
- commit date: 2024-07-17
- overall geometric mean: 1.01x slower
- HPT reliability: 66.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 275 ms: 1.01x slower                                                 |
| docutils       | 2.84 sec                                                              | 2.88 sec: 1.01x slower                                               |
| html5lib       | 64.0 ms                                                               | 63.3 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 70.6 ms                                                               | 70.2 ms: 1.01x faster                                                |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                | 134 ms: 1.01x slower                                                 |
| regex_dna      | 225 ms                                                                | 226 ms: 1.01x slower                                                 |
| regex_v8       | 24.2 ms                                                               | 25.7 ms: 1.06x slower                                                |
| regex_effbot   | 3.58 ms                                                               | 3.82 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate  | 81.4 ms                                                               | 79.6 ms: 1.02x faster                                                |
| xml_etree_parse     | 148 ms                                                                | 146 ms: 1.02x faster                                                 |
| pickle_pure_python  | 297 us                                                                | 293 us: 1.01x faster                                                 |
| xml_etree_process   | 57.4 ms                                                               | 56.8 ms: 1.01x faster                                                |
| json_dumps          | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                |
| xml_etree_iterparse | 99.4 ms                                                               | 98.6 ms: 1.01x faster                                                |
| json_loads          | 27.5 us                                                               | 27.6 us: 1.00x slower                                                |
| tomli_loads         | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                               |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                               | 7.14 ms: 1.00x faster                                                |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 24.8 ms                                                               | 23.9 ms: 1.04x faster                                                |
| genshi_xml     | 55.4 ms                                                               | 53.4 ms: 1.04x faster                                                |
| mako           | 9.75 ms                                                               | 9.82 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text              | 24.8 ms                                                               | 23.9 ms: 1.04x faster                                                |
| genshi_xml               | 55.4 ms                                                               | 53.4 ms: 1.04x faster                                                |
| scimark_sparse_mat_mult  | 4.48 ms                                                               | 4.35 ms: 1.03x faster                                                |
| async_generators         | 462 ms                                                                | 450 ms: 1.03x faster                                                 |
| scimark_fft              | 317 ms                                                                | 309 ms: 1.03x faster                                                 |
| xml_etree_generate       | 81.4 ms                                                               | 79.6 ms: 1.02x faster                                                |
| chaos                    | 58.7 ms                                                               | 57.5 ms: 1.02x faster                                                |
| richards_super           | 48.0 ms                                                               | 47.2 ms: 1.02x faster                                                |
| spectral_norm            | 102 ms                                                                | 101 ms: 1.02x faster                                                 |
| scimark_lu               | 124 ms                                                                | 122 ms: 1.02x faster                                                 |
| xml_etree_parse          | 148 ms                                                                | 146 ms: 1.02x faster                                                 |
| pickle_pure_python       | 297 us                                                                | 293 us: 1.01x faster                                                 |
| logging_simple           | 5.56 us                                                               | 5.49 us: 1.01x faster                                                |
| html5lib                 | 64.0 ms                                                               | 63.3 ms: 1.01x faster                                                |
| comprehensions           | 16.4 us                                                               | 16.2 us: 1.01x faster                                                |
| scimark_sor              | 130 ms                                                                | 129 ms: 1.01x faster                                                 |
| xml_etree_process        | 57.4 ms                                                               | 56.8 ms: 1.01x faster                                                |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                |
| pathlib                  | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                |
| logging_format           | 6.18 us                                                               | 6.12 us: 1.01x faster                                                |
| thrift                   | 799 us                                                                | 793 us: 1.01x faster                                                 |
| xml_etree_iterparse      | 99.4 ms                                                               | 98.6 ms: 1.01x faster                                                |
| asyncio_tcp              | 507 ms                                                                | 504 ms: 1.01x faster                                                 |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                |
| float                    | 70.6 ms                                                               | 70.2 ms: 1.01x faster                                                |
| bench_thread_pool        | 832 us                                                                | 828 us: 1.00x faster                                                 |
| python_startup_no_site   | 7.16 ms                                                               | 7.14 ms: 1.00x faster                                                |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x faster                                                 |
| gc_traversal             | 3.65 ms                                                               | 3.66 ms: 1.00x slower                                                |
| json_loads               | 27.5 us                                                               | 27.6 us: 1.00x slower                                                |
| sqlglot_optimize         | 55.2 ms                                                               | 55.4 ms: 1.01x slower                                                |
| regex_compile            | 133 ms                                                                | 134 ms: 1.01x slower                                                 |
| mako                     | 9.75 ms                                                               | 9.82 ms: 1.01x slower                                                |
| regex_dna                | 225 ms                                                                | 226 ms: 1.01x slower                                                 |
| json                     | 5.11 ms                                                               | 5.17 ms: 1.01x slower                                                |
| sympy_str                | 292 ms                                                                | 295 ms: 1.01x slower                                                 |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                 |
| bpe_tokeniser            | 4.76 sec                                                              | 4.81 sec: 1.01x slower                                               |
| sympy_expand             | 491 ms                                                                | 496 ms: 1.01x slower                                                 |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                               |
| docutils                 | 2.84 sec                                                              | 2.88 sec: 1.01x slower                                               |
| typing_runtime_protocols | 167 us                                                                | 170 us: 1.01x slower                                                 |
| pprint_pformat           | 1.45 sec                                                              | 1.47 sec: 1.01x slower                                               |
| 2to3                     | 271 ms                                                                | 275 ms: 1.01x slower                                                 |
| logging_silent           | 106 ns                                                                | 108 ns: 1.01x slower                                                 |
| go                       | 143 ms                                                                | 145 ms: 1.02x slower                                                 |
| dulwich_log              | 67.2 ms                                                               | 68.3 ms: 1.02x slower                                                |
| sqlglot_parse            | 1.27 ms                                                               | 1.29 ms: 1.02x slower                                                |
| sqlglot_transpile        | 1.59 ms                                                               | 1.62 ms: 1.02x slower                                                |
| deepcopy_memo            | 28.2 us                                                               | 28.7 us: 1.02x slower                                                |
| sqlglot_normalize        | 111 ms                                                                | 113 ms: 1.02x slower                                                 |
| hexiom                   | 6.55 ms                                                               | 6.68 ms: 1.02x slower                                                |
| sympy_integrate          | 21.8 ms                                                               | 22.3 ms: 1.02x slower                                                |
| deltablue                | 3.57 ms                                                               | 3.65 ms: 1.02x slower                                                |
| coroutines               | 22.4 ms                                                               | 23.1 ms: 1.03x slower                                                |
| pycparser                | 1.13 sec                                                              | 1.18 sec: 1.05x slower                                               |
| regex_v8                 | 24.2 ms                                                               | 25.7 ms: 1.06x slower                                                |
| regex_effbot             | 3.58 ms                                                               | 3.82 ms: 1.07x slower                                                |
| mdp                      | 2.53 sec                                                              | 2.73 sec: 1.08x slower                                               |
| generators               | 29.4 ms                                                               | 45.4 ms: 1.54x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (30): async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, nqueens, async_tree_none_tg, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, unpickle_pure_python, dask, nbody, coverage, asyncio_tcp_ssl, bench_mp_pool, crypto_pyaes, sympy_sum, tornado_http, raytrace, fannkuch, asyncio_websockets, deepcopy, django_template, telco, richards, pyflate, deepcopy_reduce, pprint_safe_repr, pylint

# HPT report

- Reliability score: 66.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x