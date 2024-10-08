# Results vs. base

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: 5206d7b
- commit date: 2024-07-17
- overall geometric mean: 1.00x slower
- HPT reliability: 98.37%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 273 ms: 1.01x slower                                                        |
| docutils       | 2.84 sec                                                              | 2.86 sec: 1.01x slower                                                      |
| html5lib       | 64.0 ms                                                               | 65.0 ms: 1.02x slower                                                       |
| tornado_http   | 93.1 ms                                                               | 94.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io  | 862 ms                                                                | 840 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.6 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                               | 24.4 ms: 1.01x slower                                                       |
| regex_dna      | 225 ms                                                                | 229 ms: 1.02x slower                                                        |
| regex_compile  | 133 ms                                                                | 136 ms: 1.02x slower                                                        |
| regex_effbot   | 3.58 ms                                                               | 3.75 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate  | 81.4 ms                                                               | 81.8 ms: 1.01x slower                                                       |
| xml_etree_iterparse | 99.4 ms                                                               | 100 ms: 1.01x slower                                                        |
| xml_etree_process   | 57.4 ms                                                               | 58.2 ms: 1.01x slower                                                       |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (6): xml_etree_parse, json_dumps, unpickle_pure_python, json_loads, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                               | 7.17 ms: 1.00x slower                                                       |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.75 ms                                                               | 9.81 ms: 1.01x slower                                                       |
| genshi_text     | 24.8 ms                                                               | 25.1 ms: 1.01x slower                                                       |
| django_template | 35.5 ms                                                               | 36.1 ms: 1.02x slower                                                       |
| genshi_xml      | 55.4 ms                                                               | 57.7 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240715-linux-x86_64-python-8b209fd4f8a9bf960388-3.14.0a0-8b209fd | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.48 ms                                                               | 4.31 ms: 1.04x faster                                                       |
| deepcopy_reduce          | 2.75 us                                                               | 2.68 us: 1.03x faster                                                       |
| async_tree_io            | 862 ms                                                                | 840 ms: 1.03x faster                                                        |
| logging_format           | 6.18 us                                                               | 6.04 us: 1.02x faster                                                       |
| scimark_fft              | 317 ms                                                                | 312 ms: 1.02x faster                                                        |
| logging_simple           | 5.56 us                                                               | 5.48 us: 1.02x faster                                                       |
| deepcopy                 | 275 us                                                                | 271 us: 1.01x faster                                                        |
| async_generators         | 462 ms                                                                | 456 ms: 1.01x faster                                                        |
| scimark_monte_carlo      | 61.2 ms                                                               | 60.6 ms: 1.01x faster                                                       |
| scimark_sor              | 130 ms                                                                | 129 ms: 1.01x faster                                                        |
| asyncio_tcp              | 507 ms                                                                | 503 ms: 1.01x faster                                                        |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                      |
| float                    | 70.6 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| python_startup_no_site   | 7.16 ms                                                               | 7.17 ms: 1.00x slower                                                       |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| bpe_tokeniser            | 4.76 sec                                                              | 4.77 sec: 1.00x slower                                                      |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.00x slower                                                        |
| bench_thread_pool        | 832 us                                                                | 835 us: 1.00x slower                                                        |
| raytrace                 | 271 ms                                                                | 273 ms: 1.01x slower                                                        |
| xml_etree_generate       | 81.4 ms                                                               | 81.8 ms: 1.01x slower                                                       |
| gc_traversal             | 3.65 ms                                                               | 3.67 ms: 1.01x slower                                                       |
| 2to3                     | 271 ms                                                                | 273 ms: 1.01x slower                                                        |
| mako                     | 9.75 ms                                                               | 9.81 ms: 1.01x slower                                                       |
| mdp                      | 2.53 sec                                                              | 2.55 sec: 1.01x slower                                                      |
| telco                    | 8.00 ms                                                               | 8.06 ms: 1.01x slower                                                       |
| docutils                 | 2.84 sec                                                              | 2.86 sec: 1.01x slower                                                      |
| pyflate                  | 432 ms                                                                | 435 ms: 1.01x slower                                                        |
| regex_v8                 | 24.2 ms                                                               | 24.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 99.4 ms                                                               | 100 ms: 1.01x slower                                                        |
| pycparser                | 1.13 sec                                                              | 1.14 sec: 1.01x slower                                                      |
| sqlglot_transpile        | 1.59 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| generators               | 29.4 ms                                                               | 29.7 ms: 1.01x slower                                                       |
| sympy_str                | 292 ms                                                                | 295 ms: 1.01x slower                                                        |
| tornado_http             | 93.1 ms                                                               | 94.2 ms: 1.01x slower                                                       |
| pathlib                  | 16.0 ms                                                               | 16.2 ms: 1.01x slower                                                       |
| sympy_sum                | 165 ms                                                                | 167 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 55.2 ms                                                               | 55.8 ms: 1.01x slower                                                       |
| genshi_text              | 24.8 ms                                                               | 25.1 ms: 1.01x slower                                                       |
| comprehensions           | 16.4 us                                                               | 16.6 us: 1.01x slower                                                       |
| richards_super           | 48.0 ms                                                               | 48.7 ms: 1.01x slower                                                       |
| dulwich_log              | 67.2 ms                                                               | 68.1 ms: 1.01x slower                                                       |
| sympy_expand             | 491 ms                                                                | 498 ms: 1.01x slower                                                        |
| spectral_norm            | 102 ms                                                                | 104 ms: 1.01x slower                                                        |
| xml_etree_process        | 57.4 ms                                                               | 58.2 ms: 1.01x slower                                                       |
| hexiom                   | 6.55 ms                                                               | 6.65 ms: 1.01x slower                                                       |
| html5lib                 | 64.0 ms                                                               | 65.0 ms: 1.02x slower                                                       |
| sqlglot_parse            | 1.27 ms                                                               | 1.29 ms: 1.02x slower                                                       |
| django_template          | 35.5 ms                                                               | 36.1 ms: 1.02x slower                                                       |
| sqlglot_normalize        | 111 ms                                                                | 113 ms: 1.02x slower                                                        |
| regex_dna                | 225 ms                                                                | 229 ms: 1.02x slower                                                        |
| deepcopy_memo            | 28.2 us                                                               | 28.8 us: 1.02x slower                                                       |
| regex_compile            | 133 ms                                                                | 136 ms: 1.02x slower                                                        |
| sympy_integrate          | 21.8 ms                                                               | 22.3 ms: 1.02x slower                                                       |
| coroutines               | 22.4 ms                                                               | 22.9 ms: 1.02x slower                                                       |
| deltablue                | 3.57 ms                                                               | 3.66 ms: 1.02x slower                                                       |
| richards                 | 41.1 ms                                                               | 42.2 ms: 1.03x slower                                                       |
| go                       | 143 ms                                                                | 147 ms: 1.03x slower                                                        |
| typing_runtime_protocols | 167 us                                                                | 173 us: 1.03x slower                                                        |
| genshi_xml               | 55.4 ms                                                               | 57.7 ms: 1.04x slower                                                       |
| regex_effbot             | 3.58 ms                                                               | 3.75 ms: 1.05x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (29): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, logging_silent, scimark_lu, pprint_pformat, pprint_safe_repr, nqueens, coverage, asyncio_websockets, chaos, json_dumps, unpickle_pure_python, thrift, json_loads, bench_mp_pool, dask, fannkuch, tomli_loads, crypto_pyaes, json, nbody, pickle_pure_python, pylint

# HPT report

- Reliability score: 98.37% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x