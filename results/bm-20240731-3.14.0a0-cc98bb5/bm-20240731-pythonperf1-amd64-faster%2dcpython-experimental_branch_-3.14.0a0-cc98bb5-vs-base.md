# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.00x faster
- HPT reliability: 88.75%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                                     | 230 ms: 1.01x faster                                                                 |
| html5lib       | 43.1 ms                                                                    | 41.5 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 390 ms                                                                     | 386 ms: 1.01x faster                                                                 |
| coroutines                 | 13.7 ms                                                                    | 14.0 ms: 1.02x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, async_tree_memoization, async_generators, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 59.7 ms                                                                    | 55.9 ms: 1.07x faster                                                                |
| nbody          | 86.7 ms                                                                    | 85.4 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 17.4 ms                                                                    | 15.5 ms: 1.12x faster                                                                |
| regex_compile  | 93.3 ms                                                                    | 91.8 ms: 1.02x faster                                                                |
| regex_dna      | 119 ms                                                                     | 123 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.61 sec                                                                   | 1.54 sec: 1.05x faster                                                               |
| xml_etree_process    | 42.1 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| xml_etree_parse      | 95.0 ms                                                                    | 93.1 ms: 1.02x faster                                                                |
| xml_etree_generate   | 59.4 ms                                                                    | 58.4 ms: 1.02x faster                                                                |
| json_dumps           | 6.27 ms                                                                    | 6.22 ms: 1.01x faster                                                                |
| pickle_pure_python   | 215 us                                                                     | 214 us: 1.00x faster                                                                 |
| unpickle_pure_python | 152 us                                                                     | 153 us: 1.00x slower                                                                 |
| json_loads           | 14.1 us                                                                    | 14.3 us: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.3 ms                                                                    | 17.7 ms: 1.03x faster                                                                |
| python_startup         | 21.8 ms                                                                    | 21.5 ms: 1.01x faster                                                                |
| Geometric mean         | (ref)                                                                      | 1.02x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 38.1 ms                                                                    | 36.6 ms: 1.04x faster                                                                |
| genshi_text     | 17.9 ms                                                                    | 17.4 ms: 1.03x faster                                                                |
| django_template | 25.0 ms                                                                    | 24.8 ms: 1.01x faster                                                                |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8                   | 17.4 ms                                                                    | 15.5 ms: 1.12x faster                                                                |
| pycparser                  | 833 ms                                                                     | 755 ms: 1.10x faster                                                                 |
| float                      | 59.7 ms                                                                    | 55.9 ms: 1.07x faster                                                                |
| tomli_loads                | 1.61 sec                                                                   | 1.54 sec: 1.05x faster                                                               |
| genshi_xml                 | 38.1 ms                                                                    | 36.6 ms: 1.04x faster                                                                |
| html5lib                   | 43.1 ms                                                                    | 41.5 ms: 1.04x faster                                                                |
| genshi_text                | 17.9 ms                                                                    | 17.4 ms: 1.03x faster                                                                |
| python_startup_no_site     | 18.3 ms                                                                    | 17.7 ms: 1.03x faster                                                                |
| richards                   | 32.4 ms                                                                    | 31.5 ms: 1.03x faster                                                                |
| raytrace                   | 197 ms                                                                     | 192 ms: 1.03x faster                                                                 |
| xml_etree_process          | 42.1 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| scimark_fft                | 213 ms                                                                     | 208 ms: 1.02x faster                                                                 |
| mdp                        | 1.48 sec                                                                   | 1.44 sec: 1.02x faster                                                               |
| dulwich_log                | 44.1 ms                                                                    | 43.1 ms: 1.02x faster                                                                |
| richards_super             | 36.4 ms                                                                    | 35.7 ms: 1.02x faster                                                                |
| xml_etree_parse            | 95.0 ms                                                                    | 93.1 ms: 1.02x faster                                                                |
| xml_etree_generate         | 59.4 ms                                                                    | 58.4 ms: 1.02x faster                                                                |
| deepcopy                   | 192 us                                                                     | 189 us: 1.02x faster                                                                 |
| regex_compile              | 93.3 ms                                                                    | 91.8 ms: 1.02x faster                                                                |
| nbody                      | 86.7 ms                                                                    | 85.4 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult    | 2.91 ms                                                                    | 2.87 ms: 1.01x faster                                                                |
| python_startup             | 21.8 ms                                                                    | 21.5 ms: 1.01x faster                                                                |
| pprint_safe_repr           | 571 ms                                                                     | 564 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 390 ms                                                                     | 386 ms: 1.01x faster                                                                 |
| 2to3                       | 233 ms                                                                     | 230 ms: 1.01x faster                                                                 |
| deltablue                  | 2.28 ms                                                                    | 2.26 ms: 1.01x faster                                                                |
| pprint_pformat             | 1.16 sec                                                                   | 1.15 sec: 1.01x faster                                                               |
| sqlglot_optimize           | 36.7 ms                                                                    | 36.3 ms: 1.01x faster                                                                |
| json_dumps                 | 6.27 ms                                                                    | 6.22 ms: 1.01x faster                                                                |
| django_template            | 25.0 ms                                                                    | 24.8 ms: 1.01x faster                                                                |
| sympy_expand               | 311 ms                                                                     | 309 ms: 1.01x faster                                                                 |
| bench_mp_pool              | 69.7 ms                                                                    | 69.3 ms: 1.01x faster                                                                |
| pathlib                    | 81.0 ms                                                                    | 80.6 ms: 1.01x faster                                                                |
| pickle_pure_python         | 215 us                                                                     | 214 us: 1.00x faster                                                                 |
| meteor_contest             | 77.3 ms                                                                    | 77.5 ms: 1.00x slower                                                                |
| sqlglot_normalize          | 195 ms                                                                     | 196 ms: 1.00x slower                                                                 |
| sympy_integrate            | 13.3 ms                                                                    | 13.4 ms: 1.00x slower                                                                |
| unpickle_pure_python       | 152 us                                                                     | 153 us: 1.00x slower                                                                 |
| sympy_str                  | 179 ms                                                                     | 180 ms: 1.01x slower                                                                 |
| spectral_norm              | 71.3 ms                                                                    | 71.8 ms: 1.01x slower                                                                |
| sympy_sum                  | 90.5 ms                                                                    | 91.4 ms: 1.01x slower                                                                |
| scimark_lu                 | 64.9 ms                                                                    | 65.8 ms: 1.01x slower                                                                |
| crypto_pyaes               | 51.5 ms                                                                    | 52.2 ms: 1.01x slower                                                                |
| logging_silent             | 62.8 ns                                                                    | 63.6 ns: 1.01x slower                                                                |
| telco                      | 4.98 ms                                                                    | 5.05 ms: 1.01x slower                                                                |
| json_loads                 | 14.1 us                                                                    | 14.3 us: 1.01x slower                                                                |
| chaos                      | 44.3 ms                                                                    | 45.0 ms: 1.02x slower                                                                |
| coroutines                 | 13.7 ms                                                                    | 14.0 ms: 1.02x slower                                                                |
| logging_format             | 6.85 us                                                                    | 6.98 us: 1.02x slower                                                                |
| generators                 | 21.0 ms                                                                    | 21.5 ms: 1.02x slower                                                                |
| comprehensions             | 12.1 us                                                                    | 12.4 us: 1.02x slower                                                                |
| pyflate                    | 320 ms                                                                     | 328 ms: 1.03x slower                                                                 |
| hexiom                     | 4.49 ms                                                                    | 4.62 ms: 1.03x slower                                                                |
| coverage                   | 47.2 ms                                                                    | 48.7 ms: 1.03x slower                                                                |
| regex_dna                  | 119 ms                                                                     | 123 ms: 1.03x slower                                                                 |
| fannkuch                   | 292 ms                                                                     | 302 ms: 1.03x slower                                                                 |
| scimark_monte_carlo        | 50.6 ms                                                                    | 52.7 ms: 1.04x slower                                                                |
| scimark_sor                | 89.7 ms                                                                    | 94.3 ms: 1.05x slower                                                                |
| nqueens                    | 61.6 ms                                                                    | 65.7 ms: 1.07x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (29): asyncio_tcp_ssl, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, tornado_http, asyncio_tcp, xml_etree_iterparse, logging_simple, sqlglot_parse, regex_effbot, docutils, mako, pidigits, async_tree_memoization, deepcopy_reduce, deepcopy_memo, gc_traversal, go, async_generators, sqlglot_transpile, typing_runtime_protocols, thrift, async_tree_io, bench_thread_pool, pylint, create_gc_cycles, json

# HPT report

- Reliability score: 88.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown