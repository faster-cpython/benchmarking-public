# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x faster
- HPT reliability: 85.98%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 232 ms                                                                     | 236 ms: 1.02x slower                                                       |
| docutils       | 1.79 sec                                                                   | 1.79 sec: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators | 249 ms                                                                     | 252 ms: 1.01x slower                                                       |
| coroutines       | 13.9 ms                                                                    | 14.1 ms: 1.01x slower                                                      |
| Geometric mean   | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 91.2 ms                                                                    | 85.4 ms: 1.07x faster                                                      |
| float          | 55.3 ms                                                                    | 57.0 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 125 ms                                                                     | 115 ms: 1.09x faster                                                       |
| regex_effbot   | 1.63 ms                                                                    | 1.57 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                               |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|---------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads         | 1.66 sec                                                                   | 1.62 sec: 1.02x faster                                                     |
| pickle_pure_python  | 226 us                                                                     | 221 us: 1.02x faster                                                       |
| xml_etree_parse     | 95.6 ms                                                                    | 94.8 ms: 1.01x faster                                                      |
| xml_etree_process   | 42.5 ms                                                                    | 42.1 ms: 1.01x faster                                                      |
| xml_etree_generate  | 59.1 ms                                                                    | 58.7 ms: 1.01x faster                                                      |
| xml_etree_iterparse | 66.2 ms                                                                    | 66.6 ms: 1.01x slower                                                      |
| json_loads          | 14.1 us                                                                    | 14.3 us: 1.01x slower                                                      |
| Geometric mean      | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.0 ms                                                                    | 22.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 18.0 ms                                                                    | 17.8 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (3): mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pycparser                | 928 ms                                                                     | 811 ms: 1.14x faster                                                       |
| regex_dna                | 125 ms                                                                     | 115 ms: 1.09x faster                                                       |
| nbody                    | 91.2 ms                                                                    | 85.4 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.78 ms                                                                    | 2.62 ms: 1.06x faster                                                      |
| regex_effbot             | 1.63 ms                                                                    | 1.57 ms: 1.04x faster                                                      |
| scimark_monte_carlo      | 52.5 ms                                                                    | 50.4 ms: 1.04x faster                                                      |
| spectral_norm            | 77.3 ms                                                                    | 74.7 ms: 1.03x faster                                                      |
| deepcopy_reduce          | 2.02 us                                                                    | 1.96 us: 1.03x faster                                                      |
| deepcopy_memo            | 21.3 us                                                                    | 20.7 us: 1.03x faster                                                      |
| deepcopy                 | 193 us                                                                     | 189 us: 1.03x faster                                                       |
| tomli_loads              | 1.66 sec                                                                   | 1.62 sec: 1.02x faster                                                     |
| pickle_pure_python       | 226 us                                                                     | 221 us: 1.02x faster                                                       |
| chaos                    | 45.8 ms                                                                    | 44.9 ms: 1.02x faster                                                      |
| nqueens                  | 66.8 ms                                                                    | 65.5 ms: 1.02x faster                                                      |
| json                     | 3.07 ms                                                                    | 3.01 ms: 1.02x faster                                                      |
| scimark_fft              | 205 ms                                                                     | 202 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 117 us                                                                     | 116 us: 1.01x faster                                                       |
| sqlglot_parse            | 915 us                                                                     | 903 us: 1.01x faster                                                       |
| sqlglot_transpile        | 1.14 ms                                                                    | 1.13 ms: 1.01x faster                                                      |
| meteor_contest           | 78.0 ms                                                                    | 77.2 ms: 1.01x faster                                                      |
| sympy_str                | 184 ms                                                                     | 182 ms: 1.01x faster                                                       |
| logging_silent           | 66.1 ns                                                                    | 65.5 ns: 1.01x faster                                                      |
| genshi_text              | 18.0 ms                                                                    | 17.8 ms: 1.01x faster                                                      |
| xml_etree_parse          | 95.6 ms                                                                    | 94.8 ms: 1.01x faster                                                      |
| xml_etree_process        | 42.5 ms                                                                    | 42.1 ms: 1.01x faster                                                      |
| coverage                 | 47.6 ms                                                                    | 47.2 ms: 1.01x faster                                                      |
| xml_etree_generate       | 59.1 ms                                                                    | 58.7 ms: 1.01x faster                                                      |
| fannkuch                 | 298 ms                                                                     | 296 ms: 1.01x faster                                                       |
| bench_mp_pool            | 69.9 ms                                                                    | 69.4 ms: 1.01x faster                                                      |
| scimark_lu               | 65.1 ms                                                                    | 64.8 ms: 1.00x faster                                                      |
| hexiom                   | 4.72 ms                                                                    | 4.70 ms: 1.00x faster                                                      |
| scimark_sor              | 96.2 ms                                                                    | 95.8 ms: 1.00x faster                                                      |
| docutils                 | 1.79 sec                                                                   | 1.79 sec: 1.00x slower                                                     |
| sqlglot_normalize        | 202 ms                                                                     | 203 ms: 1.00x slower                                                       |
| pathlib                  | 81.0 ms                                                                    | 81.5 ms: 1.01x slower                                                      |
| logging_simple           | 6.48 us                                                                    | 6.52 us: 1.01x slower                                                      |
| sympy_expand             | 312 ms                                                                     | 314 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 66.2 ms                                                                    | 66.6 ms: 1.01x slower                                                      |
| pprint_pformat           | 1.18 sec                                                                   | 1.18 sec: 1.01x slower                                                     |
| json_loads               | 14.1 us                                                                    | 14.3 us: 1.01x slower                                                      |
| deltablue                | 2.35 ms                                                                    | 2.37 ms: 1.01x slower                                                      |
| logging_format           | 6.94 us                                                                    | 7.01 us: 1.01x slower                                                      |
| go                       | 101 ms                                                                     | 101 ms: 1.01x slower                                                       |
| async_generators         | 249 ms                                                                     | 252 ms: 1.01x slower                                                       |
| python_startup           | 22.0 ms                                                                    | 22.2 ms: 1.01x slower                                                      |
| raytrace                 | 204 ms                                                                     | 206 ms: 1.01x slower                                                       |
| richards                 | 34.2 ms                                                                    | 34.7 ms: 1.01x slower                                                      |
| pprint_safe_repr         | 573 ms                                                                     | 581 ms: 1.01x slower                                                       |
| coroutines               | 13.9 ms                                                                    | 14.1 ms: 1.01x slower                                                      |
| richards_super           | 38.5 ms                                                                    | 39.3 ms: 1.02x slower                                                      |
| 2to3                     | 232 ms                                                                     | 236 ms: 1.02x slower                                                       |
| float                    | 55.3 ms                                                                    | 57.0 ms: 1.03x slower                                                      |
| telco                    | 4.97 ms                                                                    | 5.13 ms: 1.03x slower                                                      |
| generators               | 20.9 ms                                                                    | 21.8 ms: 1.04x slower                                                      |
| Geometric mean           | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (34): asyncio_tcp_ssl, asyncio_tcp, async_tree_none, async_tree_memoization_tg, python_startup_no_site, mako, html5lib, async_tree_memoization, async_tree_cpu_io_mixed, pylint, comprehensions, thrift, sympy_integrate, django_template, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, pyflate, create_gc_cycles, pidigits, sympy_sum, tornado_http, json_dumps, crypto_pyaes, mdp, regex_compile, async_tree_none_tg, dulwich_log, unpickle_pure_python, gc_traversal, regex_v8, sqlglot_optimize, bench_thread_pool, genshi_xml

# HPT report

- Reliability score: 85.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown