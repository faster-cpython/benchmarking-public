# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 90.81%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.75 sec                                                                   | 1.75 sec: 1.00x slower                                                               |
| html5lib       | 43.1 ms                                                                    | 42.3 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators | 242 ms                                                                     | 244 ms: 1.01x slower                                                                 |
| coroutines       | 13.7 ms                                                                    | 14.3 ms: 1.04x slower                                                                |
| asyncio_tcp_ssl  | 1.69 sec                                                                   | 1.85 sec: 1.09x slower                                                               |
| Geometric mean   | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 59.7 ms                                                                    | 56.6 ms: 1.05x faster                                                                |
| nbody          | 86.7 ms                                                                    | 92.0 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 17.4 ms                                                                    | 14.8 ms: 1.18x faster                                                                |
| regex_effbot   | 1.60 ms                                                                    | 1.59 ms: 1.01x faster                                                                |
| regex_dna      | 119 ms                                                                     | 120 ms: 1.01x slower                                                                 |
| regex_compile  | 93.3 ms                                                                    | 95.0 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_process    | 42.1 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| xml_etree_generate   | 59.4 ms                                                                    | 58.1 ms: 1.02x faster                                                                |
| pickle_pure_python   | 215 us                                                                     | 217 us: 1.01x slower                                                                 |
| json_loads           | 14.1 us                                                                    | 14.5 us: 1.02x slower                                                                |
| unpickle_pure_python | 152 us                                                                     | 157 us: 1.03x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (4): tomli_loads, xml_etree_parse, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.3 ms                                                                    | 17.4 ms: 1.05x faster                                                                |
| Geometric mean         | (ref)                                                                      | 1.03x faster                                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 38.1 ms                                                                    | 36.8 ms: 1.04x faster                                                                |
| django_template | 25.0 ms                                                                    | 24.7 ms: 1.01x faster                                                                |
| mako            | 7.08 ms                                                                    | 7.25 ms: 1.02x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8                 | 17.4 ms                                                                    | 14.8 ms: 1.18x faster                                                                |
| pycparser                | 833 ms                                                                     | 752 ms: 1.11x faster                                                                 |
| float                    | 59.7 ms                                                                    | 56.6 ms: 1.05x faster                                                                |
| python_startup_no_site   | 18.3 ms                                                                    | 17.4 ms: 1.05x faster                                                                |
| genshi_xml               | 38.1 ms                                                                    | 36.8 ms: 1.04x faster                                                                |
| dulwich_log              | 44.1 ms                                                                    | 42.7 ms: 1.03x faster                                                                |
| xml_etree_process        | 42.1 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| xml_etree_generate       | 59.4 ms                                                                    | 58.1 ms: 1.02x faster                                                                |
| html5lib                 | 43.1 ms                                                                    | 42.3 ms: 1.02x faster                                                                |
| typing_runtime_protocols | 114 us                                                                     | 112 us: 1.02x faster                                                                 |
| scimark_sparse_mat_mult  | 2.91 ms                                                                    | 2.88 ms: 1.01x faster                                                                |
| sqlglot_optimize         | 36.7 ms                                                                    | 36.3 ms: 1.01x faster                                                                |
| mdp                      | 1.48 sec                                                                   | 1.46 sec: 1.01x faster                                                               |
| telco                    | 4.98 ms                                                                    | 4.93 ms: 1.01x faster                                                                |
| django_template          | 25.0 ms                                                                    | 24.7 ms: 1.01x faster                                                                |
| sqlglot_normalize        | 195 ms                                                                     | 193 ms: 1.01x faster                                                                 |
| thrift                   | 529 us                                                                     | 525 us: 1.01x faster                                                                 |
| regex_effbot             | 1.60 ms                                                                    | 1.59 ms: 1.01x faster                                                                |
| bench_mp_pool            | 69.7 ms                                                                    | 69.1 ms: 1.01x faster                                                                |
| logging_simple           | 6.44 us                                                                    | 6.39 us: 1.01x faster                                                                |
| raytrace                 | 197 ms                                                                     | 196 ms: 1.01x faster                                                                 |
| pathlib                  | 81.0 ms                                                                    | 80.5 ms: 1.01x faster                                                                |
| scimark_fft              | 213 ms                                                                     | 212 ms: 1.00x faster                                                                 |
| pprint_safe_repr         | 571 ms                                                                     | 569 ms: 1.00x faster                                                                 |
| pprint_pformat           | 1.16 sec                                                                   | 1.16 sec: 1.00x faster                                                               |
| coverage                 | 47.2 ms                                                                    | 47.4 ms: 1.00x slower                                                                |
| docutils                 | 1.75 sec                                                                   | 1.75 sec: 1.00x slower                                                               |
| logging_format           | 6.85 us                                                                    | 6.89 us: 1.00x slower                                                                |
| crypto_pyaes             | 51.5 ms                                                                    | 51.8 ms: 1.01x slower                                                                |
| regex_dna                | 119 ms                                                                     | 120 ms: 1.01x slower                                                                 |
| pickle_pure_python       | 215 us                                                                     | 217 us: 1.01x slower                                                                 |
| async_generators         | 242 ms                                                                     | 244 ms: 1.01x slower                                                                 |
| sqlglot_parse            | 899 us                                                                     | 906 us: 1.01x slower                                                                 |
| scimark_lu               | 64.9 ms                                                                    | 65.5 ms: 1.01x slower                                                                |
| deltablue                | 2.28 ms                                                                    | 2.31 ms: 1.01x slower                                                                |
| sqlglot_transpile        | 1.12 ms                                                                    | 1.13 ms: 1.01x slower                                                                |
| sympy_str                | 179 ms                                                                     | 181 ms: 1.01x slower                                                                 |
| deepcopy_memo            | 20.9 us                                                                    | 21.1 us: 1.01x slower                                                                |
| richards                 | 32.4 ms                                                                    | 32.8 ms: 1.01x slower                                                                |
| scimark_monte_carlo      | 50.6 ms                                                                    | 51.2 ms: 1.01x slower                                                                |
| chaos                    | 44.3 ms                                                                    | 44.9 ms: 1.02x slower                                                                |
| sympy_integrate          | 13.3 ms                                                                    | 13.5 ms: 1.02x slower                                                                |
| richards_super           | 36.4 ms                                                                    | 37.0 ms: 1.02x slower                                                                |
| regex_compile            | 93.3 ms                                                                    | 95.0 ms: 1.02x slower                                                                |
| sympy_sum                | 90.5 ms                                                                    | 92.1 ms: 1.02x slower                                                                |
| meteor_contest           | 77.3 ms                                                                    | 79.0 ms: 1.02x slower                                                                |
| json_loads               | 14.1 us                                                                    | 14.5 us: 1.02x slower                                                                |
| mako                     | 7.08 ms                                                                    | 7.25 ms: 1.02x slower                                                                |
| logging_silent           | 62.8 ns                                                                    | 64.4 ns: 1.03x slower                                                                |
| hexiom                   | 4.49 ms                                                                    | 4.61 ms: 1.03x slower                                                                |
| pyflate                  | 320 ms                                                                     | 330 ms: 1.03x slower                                                                 |
| fannkuch                 | 292 ms                                                                     | 301 ms: 1.03x slower                                                                 |
| unpickle_pure_python     | 152 us                                                                     | 157 us: 1.03x slower                                                                 |
| spectral_norm            | 71.3 ms                                                                    | 74.1 ms: 1.04x slower                                                                |
| coroutines               | 13.7 ms                                                                    | 14.3 ms: 1.04x slower                                                                |
| generators               | 21.0 ms                                                                    | 22.0 ms: 1.04x slower                                                                |
| nqueens                  | 61.6 ms                                                                    | 64.9 ms: 1.05x slower                                                                |
| nbody                    | 86.7 ms                                                                    | 92.0 ms: 1.06x slower                                                                |
| scimark_sor              | 89.7 ms                                                                    | 96.5 ms: 1.08x slower                                                                |
| asyncio_tcp_ssl          | 1.69 sec                                                                   | 1.85 sec: 1.09x slower                                                               |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (28): async_tree_io_tg, async_tree_memoization_tg, async_tree_io, create_gc_cycles, python_startup, async_tree_none, async_tree_none_tg, tomli_loads, comprehensions, genshi_text, xml_etree_parse, deepcopy, async_tree_cpu_io_mixed, gc_traversal, async_tree_cpu_io_mixed_tg, go, async_tree_memoization, sympy_expand, xml_etree_iterparse, pidigits, deepcopy_reduce, asyncio_tcp, tornado_http, 2to3, bench_thread_pool, pylint, json, json_dumps

# HPT report

- Reliability score: 90.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown