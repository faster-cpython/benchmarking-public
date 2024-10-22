# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 240 ms                                                                     | 242 ms: 1.01x slower                                                       |
| docutils       | 1.84 sec                                                                   | 1.85 sec: 1.01x slower                                                     |
| html5lib       | 41.0 ms                                                                    | 42.1 ms: 1.03x slower                                                      |
| tornado_http   | 96.1 ms                                                                    | 95.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines       | 14.1 ms                                                                    | 13.8 ms: 1.03x faster                                                      |
| async_generators | 256 ms                                                                     | 261 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (10): asyncio_tcp, asyncio_tcp_ssl, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.4 ms                                                                    | 14.9 ms: 1.03x faster                                                      |
| regex_dna      | 122 ms                                                                     | 119 ms: 1.02x faster                                                       |
| regex_compile  | 89.4 ms                                                                    | 91.0 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python | 181 us                                                                     | 182 us: 1.01x slower                                                       |
| tomli_loads        | 1.25 sec                                                                   | 1.26 sec: 1.01x slower                                                     |
| xml_etree_parse    | 92.9 ms                                                                    | 95.5 ms: 1.03x slower                                                      |
| Geometric mean     | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (6): json_dumps, xml_etree_generate, json_loads, xml_etree_process, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                                    | 18.4 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 4.96 ms                                                                    | 5.05 ms: 1.02x slower                                                      |
| genshi_xml      | 39.0 ms                                                                    | 40.0 ms: 1.03x slower                                                      |
| django_template | 24.7 ms                                                                    | 25.7 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 121 us                                                                     | 116 us: 1.04x faster                                                       |
| regex_v8                 | 15.4 ms                                                                    | 14.9 ms: 1.03x faster                                                      |
| scimark_lu               | 55.6 ms                                                                    | 54.0 ms: 1.03x faster                                                      |
| deepcopy_memo            | 16.2 us                                                                    | 15.7 us: 1.03x faster                                                      |
| fannkuch                 | 220 ms                                                                     | 214 ms: 1.03x faster                                                       |
| coroutines               | 14.1 ms                                                                    | 13.8 ms: 1.03x faster                                                      |
| spectral_norm            | 46.1 ms                                                                    | 45.0 ms: 1.02x faster                                                      |
| pyflate                  | 257 ms                                                                     | 251 ms: 1.02x faster                                                       |
| regex_dna                | 122 ms                                                                     | 119 ms: 1.02x faster                                                       |
| tornado_http             | 96.1 ms                                                                    | 95.2 ms: 1.01x faster                                                      |
| pathlib                  | 82.1 ms                                                                    | 81.4 ms: 1.01x faster                                                      |
| deltablue                | 2.36 ms                                                                    | 2.34 ms: 1.01x faster                                                      |
| scimark_fft              | 148 ms                                                                     | 147 ms: 1.01x faster                                                       |
| richards                 | 30.6 ms                                                                    | 30.4 ms: 1.01x faster                                                      |
| sqlglot_normalize        | 195 ms                                                                     | 194 ms: 1.00x faster                                                       |
| logging_format           | 6.36 us                                                                    | 6.39 us: 1.00x slower                                                      |
| sympy_expand             | 332 ms                                                                     | 334 ms: 1.01x slower                                                       |
| 2to3                     | 240 ms                                                                     | 242 ms: 1.01x slower                                                       |
| pickle_pure_python       | 181 us                                                                     | 182 us: 1.01x slower                                                       |
| sqlglot_transpile        | 1.08 ms                                                                    | 1.09 ms: 1.01x slower                                                      |
| dulwich_log              | 43.1 ms                                                                    | 43.4 ms: 1.01x slower                                                      |
| scimark_sor              | 59.9 ms                                                                    | 60.4 ms: 1.01x slower                                                      |
| docutils                 | 1.84 sec                                                                   | 1.85 sec: 1.01x slower                                                     |
| sympy_sum                | 97.3 ms                                                                    | 98.4 ms: 1.01x slower                                                      |
| crypto_pyaes             | 39.9 ms                                                                    | 40.3 ms: 1.01x slower                                                      |
| raytrace                 | 188 ms                                                                     | 190 ms: 1.01x slower                                                       |
| logging_silent           | 56.5 ns                                                                    | 57.2 ns: 1.01x slower                                                      |
| python_startup_no_site   | 18.2 ms                                                                    | 18.4 ms: 1.01x slower                                                      |
| go                       | 101 ms                                                                     | 102 ms: 1.01x slower                                                       |
| coverage                 | 47.1 ms                                                                    | 47.7 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult  | 2.07 ms                                                                    | 2.10 ms: 1.01x slower                                                      |
| tomli_loads              | 1.25 sec                                                                   | 1.26 sec: 1.01x slower                                                     |
| nqueens                  | 61.9 ms                                                                    | 62.7 ms: 1.01x slower                                                      |
| sympy_integrate          | 14.7 ms                                                                    | 14.9 ms: 1.01x slower                                                      |
| richards_super           | 34.5 ms                                                                    | 35.0 ms: 1.01x slower                                                      |
| telco                    | 4.54 ms                                                                    | 4.61 ms: 1.01x slower                                                      |
| mako                     | 4.96 ms                                                                    | 5.05 ms: 1.02x slower                                                      |
| regex_compile            | 89.4 ms                                                                    | 91.0 ms: 1.02x slower                                                      |
| async_generators         | 256 ms                                                                     | 261 ms: 1.02x slower                                                       |
| pprint_safe_repr         | 475 ms                                                                     | 484 ms: 1.02x slower                                                       |
| hexiom                   | 4.69 ms                                                                    | 4.79 ms: 1.02x slower                                                      |
| sympy_str                | 188 ms                                                                     | 192 ms: 1.02x slower                                                       |
| chaos                    | 39.0 ms                                                                    | 39.9 ms: 1.02x slower                                                      |
| meteor_contest           | 70.1 ms                                                                    | 71.8 ms: 1.02x slower                                                      |
| html5lib                 | 41.0 ms                                                                    | 42.1 ms: 1.03x slower                                                      |
| genshi_xml               | 39.0 ms                                                                    | 40.0 ms: 1.03x slower                                                      |
| xml_etree_parse          | 92.9 ms                                                                    | 95.5 ms: 1.03x slower                                                      |
| comprehensions           | 10.2 us                                                                    | 10.6 us: 1.03x slower                                                      |
| django_template          | 24.7 ms                                                                    | 25.7 ms: 1.04x slower                                                      |
| deepcopy_reduce          | 1.78 us                                                                    | 1.85 us: 1.04x slower                                                      |
| mdp                      | 1.41 sec                                                                   | 1.47 sec: 1.04x slower                                                     |
| scimark_monte_carlo      | 37.5 ms                                                                    | 39.2 ms: 1.04x slower                                                      |
| deepcopy                 | 183 us                                                                     | 193 us: 1.06x slower                                                       |
| generators               | 20.8 ms                                                                    | 22.5 ms: 1.08x slower                                                      |
| pycparser                | 726 ms                                                                     | 800 ms: 1.10x slower                                                       |
| Geometric mean           | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (33): pylint, asyncio_tcp, asyncio_tcp_ssl, json, json_dumps, regex_effbot, gc_traversal, python_startup, logging_simple, pidigits, bench_mp_pool, xml_etree_generate, bench_thread_pool, json_loads, xml_etree_process, sqlglot_optimize, float, async_tree_io, thrift, xml_etree_iterparse, genshi_text, async_tree_io_tg, sqlglot_parse, create_gc_cycles, nbody, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, unpickle_pure_python, pprint_pformat, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown