# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-amd64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 59.61%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| docutils       | 1.75 sec                                                                   | 1.78 sec: 1.02x slower                                                           |
| html5lib       | 38.9 ms                                                                    | 39.6 ms: 1.02x slower                                                            |
| tornado_http   | 83.8 ms                                                                    | 85.2 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 45.0 ms                                                                    | 44.5 ms: 1.01x faster                                                            |
| pidigits       | 149 ms                                                                     | 149 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.59 ms                                                                    | 1.55 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                     |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_generate   | 52.2 ms                                                                    | 51.3 ms: 1.02x faster                                                            |
| xml_etree_parse      | 92.5 ms                                                                    | 91.1 ms: 1.02x faster                                                            |
| unpickle_pure_python | 130 us                                                                     | 128 us: 1.01x faster                                                             |
| xml_etree_process    | 36.7 ms                                                                    | 36.2 ms: 1.01x faster                                                            |
| xml_etree_iterparse  | 60.7 ms                                                                    | 60.2 ms: 1.01x faster                                                            |
| pickle_pure_python   | 174 us                                                                     | 178 us: 1.02x slower                                                             |
| tomli_loads          | 1.23 sec                                                                   | 1.26 sec: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 21.0 ms                                                                    | 21.3 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml     | 46.9 ms                                                                    | 45.2 ms: 1.04x faster                                                            |
| mako           | 5.17 ms                                                                    | 5.10 ms: 1.01x faster                                                            |
| genshi_text    | 17.9 ms                                                                    | 17.8 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pycparser                | 811 ms                                                                     | 740 ms: 1.10x faster                                                             |
| scimark_lu               | 74.6 ms                                                                    | 70.3 ms: 1.06x faster                                                            |
| genshi_xml               | 46.9 ms                                                                    | 45.2 ms: 1.04x faster                                                            |
| json                     | 3.07 ms                                                                    | 2.98 ms: 1.03x faster                                                            |
| regex_effbot             | 1.59 ms                                                                    | 1.55 ms: 1.03x faster                                                            |
| generators               | 23.5 ms                                                                    | 22.9 ms: 1.03x faster                                                            |
| coroutines               | 13.9 ms                                                                    | 13.5 ms: 1.02x faster                                                            |
| pyflate                  | 256 ms                                                                     | 250 ms: 1.02x faster                                                             |
| meteor_contest           | 73.2 ms                                                                    | 71.7 ms: 1.02x faster                                                            |
| typing_runtime_protocols | 115 us                                                                     | 113 us: 1.02x faster                                                             |
| deltablue                | 2.26 ms                                                                    | 2.22 ms: 1.02x faster                                                            |
| scimark_sor              | 86.5 ms                                                                    | 85.0 ms: 1.02x faster                                                            |
| logging_silent           | 56.5 ns                                                                    | 55.5 ns: 1.02x faster                                                            |
| fannkuch                 | 222 ms                                                                     | 219 ms: 1.02x faster                                                             |
| xml_etree_generate       | 52.2 ms                                                                    | 51.3 ms: 1.02x faster                                                            |
| xml_etree_parse          | 92.5 ms                                                                    | 91.1 ms: 1.02x faster                                                            |
| unpickle_pure_python     | 130 us                                                                     | 128 us: 1.01x faster                                                             |
| richards                 | 29.8 ms                                                                    | 29.4 ms: 1.01x faster                                                            |
| xml_etree_process        | 36.7 ms                                                                    | 36.2 ms: 1.01x faster                                                            |
| crypto_pyaes             | 40.2 ms                                                                    | 39.7 ms: 1.01x faster                                                            |
| mako                     | 5.17 ms                                                                    | 5.10 ms: 1.01x faster                                                            |
| float                    | 45.0 ms                                                                    | 44.5 ms: 1.01x faster                                                            |
| richards_super           | 33.6 ms                                                                    | 33.2 ms: 1.01x faster                                                            |
| xml_etree_iterparse      | 60.7 ms                                                                    | 60.2 ms: 1.01x faster                                                            |
| genshi_text              | 17.9 ms                                                                    | 17.8 ms: 1.01x faster                                                            |
| gc_traversal             | 1.56 ms                                                                    | 1.55 ms: 1.01x faster                                                            |
| hexiom                   | 4.61 ms                                                                    | 4.59 ms: 1.00x faster                                                            |
| pathlib                  | 75.5 ms                                                                    | 75.1 ms: 1.00x faster                                                            |
| pidigits                 | 149 ms                                                                     | 149 ms: 1.00x slower                                                             |
| async_generators         | 253 ms                                                                     | 255 ms: 1.01x slower                                                             |
| sympy_expand             | 310 ms                                                                     | 313 ms: 1.01x slower                                                             |
| thrift                   | 513 us                                                                     | 518 us: 1.01x slower                                                             |
| comprehensions           | 10.3 us                                                                    | 10.4 us: 1.01x slower                                                            |
| sqlglot_transpile        | 1.03 ms                                                                    | 1.04 ms: 1.01x slower                                                            |
| sympy_str                | 179 ms                                                                     | 181 ms: 1.01x slower                                                             |
| python_startup           | 21.0 ms                                                                    | 21.3 ms: 1.01x slower                                                            |
| spectral_norm            | 44.5 ms                                                                    | 45.1 ms: 1.01x slower                                                            |
| chaos                    | 38.8 ms                                                                    | 39.4 ms: 1.01x slower                                                            |
| sympy_integrate          | 13.8 ms                                                                    | 14.0 ms: 1.02x slower                                                            |
| tornado_http             | 83.8 ms                                                                    | 85.2 ms: 1.02x slower                                                            |
| sympy_sum                | 92.6 ms                                                                    | 94.2 ms: 1.02x slower                                                            |
| sqlglot_optimize         | 35.5 ms                                                                    | 36.1 ms: 1.02x slower                                                            |
| docutils                 | 1.75 sec                                                                   | 1.78 sec: 1.02x slower                                                           |
| sqlglot_parse            | 800 us                                                                     | 815 us: 1.02x slower                                                             |
| html5lib                 | 38.9 ms                                                                    | 39.6 ms: 1.02x slower                                                            |
| raytrace                 | 176 ms                                                                     | 180 ms: 1.02x slower                                                             |
| pickle_pure_python       | 174 us                                                                     | 178 us: 1.02x slower                                                             |
| sqlglot_normalize        | 188 ms                                                                     | 192 ms: 1.02x slower                                                             |
| mdp                      | 1.41 sec                                                                   | 1.44 sec: 1.03x slower                                                           |
| deepcopy_reduce          | 1.76 us                                                                    | 1.80 us: 1.03x slower                                                            |
| tomli_loads              | 1.23 sec                                                                   | 1.26 sec: 1.03x slower                                                           |
| deepcopy                 | 177 us                                                                     | 182 us: 1.03x slower                                                             |
| pprint_safe_repr         | 464 ms                                                                     | 483 ms: 1.04x slower                                                             |
| pprint_pformat           | 950 ms                                                                     | 989 ms: 1.04x slower                                                             |
| deepcopy_memo            | 15.5 us                                                                    | 16.1 us: 1.04x slower                                                            |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                                     |

Benchmark hidden because not significant (32): regex_v8, regex_dna, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, nbody, django_template, python_startup_no_site, regex_compile, go, scimark_monte_carlo, scimark_fft, coverage, nqueens, create_gc_cycles, json_dumps, logging_simple, bench_mp_pool, json_loads, pylint, logging_format, asyncio_tcp_ssl, scimark_sparse_mat_mult, async_tree_none_tg, async_tree_none, telco, 2to3, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_tcp

# HPT report

- Reliability score: 59.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown