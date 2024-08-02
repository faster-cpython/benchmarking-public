# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: f133a86
- commit date: 2024-07-14
- overall geometric mean: 1.00x faster
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 269 ms: 1.01x faster                                                  |
| docutils       | 2.88 sec                                                              | 2.86 sec: 1.01x faster                                                |
| html5lib       | 65.4 ms                                                               | 65.6 ms: 1.00x slower                                                 |
| tornado_http   | 93.8 ms                                                               | 93.2 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 79.5 ms                                                               | 77.1 ms: 1.03x faster                                                 |
| float          | 70.4 ms                                                               | 69.6 ms: 1.01x faster                                                 |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                               | 23.7 ms: 1.08x faster                                                 |
| regex_effbot   | 3.84 ms                                                               | 3.67 ms: 1.05x faster                                                 |
| regex_dna      | 227 ms                                                                | 219 ms: 1.04x faster                                                  |
| regex_compile  | 135 ms                                                                | 134 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                |
| xml_etree_iterparse | 99.0 ms                                                               | 99.9 ms: 1.01x slower                                                 |
| json_dumps          | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                 |
| xml_etree_process   | 57.5 ms                                                               | 58.8 ms: 1.02x slower                                                 |
| xml_etree_generate  | 81.1 ms                                                               | 84.2 ms: 1.04x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                 |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                               | 24.1 ms: 1.04x faster                                                 |
| django_template | 36.1 ms                                                               | 35.1 ms: 1.03x faster                                                 |
| genshi_xml      | 56.9 ms                                                               | 56.1 ms: 1.02x faster                                                 |
| mako            | 9.77 ms                                                               | 9.85 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8                 | 25.5 ms                                                               | 23.7 ms: 1.08x faster                                                 |
| pycparser                | 1.19 sec                                                              | 1.12 sec: 1.06x faster                                                |
| regex_effbot             | 3.84 ms                                                               | 3.67 ms: 1.05x faster                                                 |
| genshi_text              | 25.1 ms                                                               | 24.1 ms: 1.04x faster                                                 |
| mdp                      | 2.71 sec                                                              | 2.61 sec: 1.04x faster                                                |
| regex_dna                | 227 ms                                                                | 219 ms: 1.04x faster                                                  |
| nbody                    | 79.5 ms                                                               | 77.1 ms: 1.03x faster                                                 |
| logging_simple           | 5.61 us                                                               | 5.45 us: 1.03x faster                                                 |
| django_template          | 36.1 ms                                                               | 35.1 ms: 1.03x faster                                                 |
| sqlglot_normalize        | 113 ms                                                                | 111 ms: 1.02x faster                                                  |
| sqlglot_optimize         | 55.7 ms                                                               | 54.6 ms: 1.02x faster                                                 |
| go                       | 146 ms                                                                | 143 ms: 1.02x faster                                                  |
| logging_format           | 6.16 us                                                               | 6.04 us: 1.02x faster                                                 |
| richards_super           | 47.7 ms                                                               | 46.8 ms: 1.02x faster                                                 |
| deepcopy_reduce          | 2.76 us                                                               | 2.70 us: 1.02x faster                                                 |
| typing_runtime_protocols | 171 us                                                                | 168 us: 1.02x faster                                                  |
| richards                 | 41.5 ms                                                               | 40.8 ms: 1.02x faster                                                 |
| scimark_sor              | 131 ms                                                                | 129 ms: 1.02x faster                                                  |
| sympy_sum                | 167 ms                                                                | 165 ms: 1.02x faster                                                  |
| logging_silent           | 108 ns                                                                | 106 ns: 1.02x faster                                                  |
| genshi_xml               | 56.9 ms                                                               | 56.1 ms: 1.02x faster                                                 |
| sqlglot_parse            | 1.28 ms                                                               | 1.26 ms: 1.02x faster                                                 |
| sqlglot_transpile        | 1.60 ms                                                               | 1.58 ms: 1.01x faster                                                 |
| hexiom                   | 6.56 ms                                                               | 6.47 ms: 1.01x faster                                                 |
| 2to3                     | 272 ms                                                                | 269 ms: 1.01x faster                                                  |
| float                    | 70.4 ms                                                               | 69.6 ms: 1.01x faster                                                 |
| regex_compile            | 135 ms                                                                | 134 ms: 1.01x faster                                                  |
| deltablue                | 3.58 ms                                                               | 3.54 ms: 1.01x faster                                                 |
| sympy_integrate          | 21.9 ms                                                               | 21.7 ms: 1.01x faster                                                 |
| dulwich_log              | 68.0 ms                                                               | 67.4 ms: 1.01x faster                                                 |
| sympy_str                | 293 ms                                                                | 291 ms: 1.01x faster                                                  |
| docutils                 | 2.88 sec                                                              | 2.86 sec: 1.01x faster                                                |
| tomli_loads              | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                |
| chaos                    | 57.8 ms                                                               | 57.4 ms: 1.01x faster                                                 |
| scimark_monte_carlo      | 60.8 ms                                                               | 60.3 ms: 1.01x faster                                                 |
| meteor_contest           | 108 ms                                                                | 107 ms: 1.01x faster                                                  |
| tornado_http             | 93.8 ms                                                               | 93.2 ms: 1.01x faster                                                 |
| asyncio_tcp              | 504 ms                                                                | 502 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x slower                                                  |
| python_startup_no_site   | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                 |
| bench_thread_pool        | 833 us                                                                | 836 us: 1.00x slower                                                  |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                 |
| html5lib                 | 65.4 ms                                                               | 65.6 ms: 1.00x slower                                                 |
| create_gc_cycles         | 1.77 ms                                                               | 1.77 ms: 1.00x slower                                                 |
| pathlib                  | 15.9 ms                                                               | 16.0 ms: 1.00x slower                                                 |
| mako                     | 9.77 ms                                                               | 9.85 ms: 1.01x slower                                                 |
| xml_etree_iterparse      | 99.0 ms                                                               | 99.9 ms: 1.01x slower                                                 |
| thrift                   | 799 us                                                                | 811 us: 1.02x slower                                                  |
| async_generators         | 455 ms                                                                | 463 ms: 1.02x slower                                                  |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                 |
| coroutines               | 23.5 ms                                                               | 24.0 ms: 1.02x slower                                                 |
| telco                    | 7.92 ms                                                               | 8.09 ms: 1.02x slower                                                 |
| xml_etree_process        | 57.5 ms                                                               | 58.8 ms: 1.02x slower                                                 |
| gc_traversal             | 3.64 ms                                                               | 3.78 ms: 1.04x slower                                                 |
| xml_etree_generate       | 81.1 ms                                                               | 84.2 ms: 1.04x slower                                                 |
| spectral_norm            | 101 ms                                                                | 107 ms: 1.05x slower                                                  |
| scimark_fft              | 305 ms                                                                | 322 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 4.70 ms: 1.07x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (32): deepcopy, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, pylint, async_tree_none, deepcopy_memo, pickle_pure_python, nqueens, dask, async_tree_none_tg, async_tree_io_tg, unpickle_pure_python, pyflate, sympy_expand, raytrace, crypto_pyaes, async_tree_memoization, json_loads, coverage, bench_mp_pool, json, xml_etree_parse, generators, asyncio_websockets, comprehensions, pprint_pformat, bpe_tokeniser, scimark_lu, async_tree_io, fannkuch, async_tree_cpu_io_mixed, pprint_safe_repr

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x