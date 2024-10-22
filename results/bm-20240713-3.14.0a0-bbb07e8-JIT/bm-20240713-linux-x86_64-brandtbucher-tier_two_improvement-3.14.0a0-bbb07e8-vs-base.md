# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.88 sec                                                              | 2.87 sec: 1.01x faster                                                      |
| html5lib       | 65.4 ms                                                               | 66.0 ms: 1.01x slower                                                       |
| tornado_http   | 93.8 ms                                                               | 93.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 69.3 ms: 1.02x faster                                                       |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                               | 24.4 ms: 1.05x faster                                                       |
| regex_effbot   | 3.84 ms                                                               | 3.73 ms: 1.03x faster                                                       |
| regex_compile  | 135 ms                                                                | 135 ms: 1.00x faster                                                        |
| regex_dna      | 227 ms                                                                | 229 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process  | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                       |
| xml_etree_generate | 81.1 ms                                                               | 80.6 ms: 1.01x faster                                                       |
| json_dumps         | 10.3 ms                                                               | 10.4 ms: 1.00x slower                                                       |
| json_loads         | 27.5 us                                                               | 27.9 us: 1.01x slower                                                       |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_parse, tomli_loads, unpickle_pure_python, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.09 ms: 1.00x faster                                                       |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 36.1 ms                                                               | 34.9 ms: 1.03x faster                                                       |
| genshi_text     | 25.1 ms                                                               | 24.6 ms: 1.02x faster                                                       |
| genshi_xml      | 56.9 ms                                                               | 56.3 ms: 1.01x faster                                                       |
| mako            | 9.77 ms                                                               | 9.86 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pycparser                | 1.19 sec                                                              | 1.13 sec: 1.05x faster                                                      |
| bpe_tokeniser            | 4.82 sec                                                              | 4.59 sec: 1.05x faster                                                      |
| pyflate                  | 446 ms                                                                | 426 ms: 1.05x faster                                                        |
| regex_v8                 | 25.5 ms                                                               | 24.4 ms: 1.05x faster                                                       |
| django_template          | 36.1 ms                                                               | 34.9 ms: 1.03x faster                                                       |
| regex_effbot             | 3.84 ms                                                               | 3.73 ms: 1.03x faster                                                       |
| gc_traversal             | 3.64 ms                                                               | 3.55 ms: 1.03x faster                                                       |
| meteor_contest           | 108 ms                                                                | 105 ms: 1.02x faster                                                        |
| sqlglot_normalize        | 113 ms                                                                | 111 ms: 1.02x faster                                                        |
| logging_simple           | 5.61 us                                                               | 5.49 us: 1.02x faster                                                       |
| nqueens                  | 86.2 ms                                                               | 84.3 ms: 1.02x faster                                                       |
| scimark_lu               | 126 ms                                                                | 123 ms: 1.02x faster                                                        |
| genshi_text              | 25.1 ms                                                               | 24.6 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 171 us                                                                | 168 us: 1.02x faster                                                        |
| logging_silent           | 108 ns                                                                | 106 ns: 1.02x faster                                                        |
| float                    | 70.4 ms                                                               | 69.3 ms: 1.02x faster                                                       |
| go                       | 146 ms                                                                | 144 ms: 1.02x faster                                                        |
| logging_format           | 6.16 us                                                               | 6.07 us: 1.01x faster                                                       |
| async_generators         | 455 ms                                                                | 449 ms: 1.01x faster                                                        |
| raytrace                 | 271 ms                                                                | 268 ms: 1.01x faster                                                        |
| dulwich_log              | 68.0 ms                                                               | 67.2 ms: 1.01x faster                                                       |
| deltablue                | 3.58 ms                                                               | 3.54 ms: 1.01x faster                                                       |
| genshi_xml               | 56.9 ms                                                               | 56.3 ms: 1.01x faster                                                       |
| create_gc_cycles         | 1.77 ms                                                               | 1.75 ms: 1.01x faster                                                       |
| scimark_sor              | 131 ms                                                                | 130 ms: 1.01x faster                                                        |
| comprehensions           | 16.7 us                                                               | 16.6 us: 1.01x faster                                                       |
| xml_etree_process        | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                       |
| tornado_http             | 93.8 ms                                                               | 93.0 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 55.7 ms                                                               | 55.3 ms: 1.01x faster                                                       |
| xml_etree_generate       | 81.1 ms                                                               | 80.6 ms: 1.01x faster                                                       |
| docutils                 | 2.88 sec                                                              | 2.87 sec: 1.01x faster                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                      |
| regex_compile            | 135 ms                                                                | 135 ms: 1.00x faster                                                        |
| asyncio_tcp              | 504 ms                                                                | 502 ms: 1.00x faster                                                        |
| asyncio_websockets       | 558 ms                                                                | 555 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.11 ms                                                               | 7.09 ms: 1.00x faster                                                       |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x slower                                                        |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.00x slower                                                       |
| sqlglot_transpile        | 1.60 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| pathlib                  | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                       |
| crypto_pyaes             | 67.0 ms                                                               | 67.5 ms: 1.01x slower                                                       |
| coverage                 | 92.7 ms                                                               | 93.4 ms: 1.01x slower                                                       |
| sympy_expand             | 493 ms                                                                | 497 ms: 1.01x slower                                                        |
| regex_dna                | 227 ms                                                                | 229 ms: 1.01x slower                                                        |
| sympy_integrate          | 21.9 ms                                                               | 22.1 ms: 1.01x slower                                                       |
| mako                     | 9.77 ms                                                               | 9.86 ms: 1.01x slower                                                       |
| html5lib                 | 65.4 ms                                                               | 66.0 ms: 1.01x slower                                                       |
| mdp                      | 2.71 sec                                                              | 2.74 sec: 1.01x slower                                                      |
| spectral_norm            | 101 ms                                                                | 103 ms: 1.01x slower                                                        |
| json_loads               | 27.5 us                                                               | 27.9 us: 1.01x slower                                                       |
| deepcopy                 | 274 us                                                                | 278 us: 1.01x slower                                                        |
| telco                    | 7.92 ms                                                               | 8.04 ms: 1.02x slower                                                       |
| deepcopy_memo            | 28.4 us                                                               | 28.9 us: 1.02x slower                                                       |
| generators               | 29.8 ms                                                               | 30.4 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 4.50 ms: 1.03x slower                                                       |
| scimark_fft              | 305 ms                                                                | 315 ms: 1.03x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (34): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, richards, xml_etree_parse, pylint, nbody, async_tree_io, pprint_pformat, richards_super, coroutines, fannkuch, tomli_loads, bench_mp_pool, unpickle_pure_python, json, sqlglot_parse, bench_thread_pool, xml_etree_iterparse, sympy_sum, thrift, 2to3, sympy_str, hexiom, scimark_monte_carlo, dask, pprint_safe_repr, chaos, pickle_pure_python, deepcopy_reduce

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x