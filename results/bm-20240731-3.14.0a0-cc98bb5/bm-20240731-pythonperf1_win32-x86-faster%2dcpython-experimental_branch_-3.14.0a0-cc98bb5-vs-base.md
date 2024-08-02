# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                         | 262 ms: 1.04x slower                                                                     |
| docutils       | 1.91 sec                                                                       | 1.94 sec: 1.01x slower                                                                   |
| html5lib       | 47.8 ms                                                                        | 49.1 ms: 1.03x slower                                                                    |
| tornado_http   | 104 ms                                                                         | 106 ms: 1.02x slower                                                                     |
| Geometric mean | (ref)                                                                          | 1.03x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| coroutines                 | 17.3 ms                                                                        | 17.4 ms: 1.01x slower                                                                    |
| async_tree_io_tg           | 511 ms                                                                         | 523 ms: 1.02x slower                                                                     |
| async_tree_io              | 549 ms                                                                         | 564 ms: 1.03x slower                                                                     |
| async_tree_memoization_tg  | 246 ms                                                                         | 253 ms: 1.03x slower                                                                     |
| async_tree_memoization     | 276 ms                                                                         | 285 ms: 1.03x slower                                                                     |
| async_tree_none            | 224 ms                                                                         | 232 ms: 1.03x slower                                                                     |
| async_tree_none_tg         | 195 ms                                                                         | 202 ms: 1.04x slower                                                                     |
| async_tree_cpu_io_mixed    | 467 ms                                                                         | 486 ms: 1.04x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 454 ms                                                                         | 474 ms: 1.04x slower                                                                     |
| async_generators           | 280 ms                                                                         | 294 ms: 1.05x slower                                                                     |
| Geometric mean             | (ref)                                                                          | 1.03x slower                                                                             |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                                         | 201 ms: 1.01x slower                                                                     |
| float          | 58.2 ms                                                                        | 60.0 ms: 1.03x slower                                                                    |
| nbody          | 88.5 ms                                                                        | 99.2 ms: 1.12x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.05x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                         | 119 ms: 1.02x faster                                                                     |
| regex_compile  | 103 ms                                                                         | 109 ms: 1.05x slower                                                                     |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                                        | 7.35 ms: 1.03x faster                                                                    |
| xml_etree_parse      | 107 ms                                                                         | 104 ms: 1.02x faster                                                                     |
| xml_etree_iterparse  | 69.2 ms                                                                        | 67.9 ms: 1.02x faster                                                                    |
| tomli_loads          | 1.82 sec                                                                       | 1.79 sec: 1.02x faster                                                                   |
| xml_etree_generate   | 66.8 ms                                                                        | 66.2 ms: 1.01x faster                                                                    |
| json_loads           | 20.0 us                                                                        | 20.4 us: 1.02x slower                                                                    |
| unpickle_pure_python | 169 us                                                                         | 173 us: 1.02x slower                                                                     |
| xml_etree_process    | 47.3 ms                                                                        | 48.6 ms: 1.03x slower                                                                    |
| pickle_pure_python   | 244 us                                                                         | 257 us: 1.06x slower                                                                     |
| Geometric mean       | (ref)                                                                          | 1.00x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 23.7 ms                                                                        | 24.3 ms: 1.03x slower                                                                    |
| python_startup_no_site | 19.7 ms                                                                        | 20.4 ms: 1.04x slower                                                                    |
| Geometric mean         | (ref)                                                                          | 1.03x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| django_template | 34.7 ms                                                                        | 33.9 ms: 1.02x faster                                                                    |
| mako            | 8.01 ms                                                                        | 8.24 ms: 1.03x slower                                                                    |
| genshi_text     | 21.6 ms                                                                        | 22.3 ms: 1.03x slower                                                                    |
| genshi_xml      | 46.4 ms                                                                        | 48.4 ms: 1.04x slower                                                                    |
| Geometric mean  | (ref)                                                                          | 1.02x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps                 | 7.53 ms                                                                        | 7.35 ms: 1.03x faster                                                                    |
| xml_etree_parse            | 107 ms                                                                         | 104 ms: 1.02x faster                                                                     |
| django_template            | 34.7 ms                                                                        | 33.9 ms: 1.02x faster                                                                    |
| regex_dna                  | 122 ms                                                                         | 119 ms: 1.02x faster                                                                     |
| xml_etree_iterparse        | 69.2 ms                                                                        | 67.9 ms: 1.02x faster                                                                    |
| tomli_loads                | 1.82 sec                                                                       | 1.79 sec: 1.02x faster                                                                   |
| create_gc_cycles           | 758 us                                                                         | 749 us: 1.01x faster                                                                     |
| xml_etree_generate         | 66.8 ms                                                                        | 66.2 ms: 1.01x faster                                                                    |
| sqlglot_normalize          | 230 ms                                                                         | 231 ms: 1.01x slower                                                                     |
| scimark_sparse_mat_mult    | 3.14 ms                                                                        | 3.16 ms: 1.01x slower                                                                    |
| coroutines                 | 17.3 ms                                                                        | 17.4 ms: 1.01x slower                                                                    |
| logging_silent             | 74.2 ns                                                                        | 74.9 ns: 1.01x slower                                                                    |
| pathlib                    | 88.6 ms                                                                        | 89.6 ms: 1.01x slower                                                                    |
| docutils                   | 1.91 sec                                                                       | 1.94 sec: 1.01x slower                                                                   |
| logging_format             | 8.87 us                                                                        | 8.98 us: 1.01x slower                                                                    |
| pidigits                   | 199 ms                                                                         | 201 ms: 1.01x slower                                                                     |
| telco                      | 6.15 ms                                                                        | 6.24 ms: 1.01x slower                                                                    |
| sqlglot_optimize           | 44.0 ms                                                                        | 44.6 ms: 1.01x slower                                                                    |
| logging_simple             | 8.12 us                                                                        | 8.26 us: 1.02x slower                                                                    |
| tornado_http               | 104 ms                                                                         | 106 ms: 1.02x slower                                                                     |
| json_loads                 | 20.0 us                                                                        | 20.4 us: 1.02x slower                                                                    |
| deepcopy_reduce            | 2.55 us                                                                        | 2.60 us: 1.02x slower                                                                    |
| async_tree_io_tg           | 511 ms                                                                         | 523 ms: 1.02x slower                                                                     |
| unpickle_pure_python       | 169 us                                                                         | 173 us: 1.02x slower                                                                     |
| mdp                        | 1.67 sec                                                                       | 1.71 sec: 1.03x slower                                                                   |
| python_startup             | 23.7 ms                                                                        | 24.3 ms: 1.03x slower                                                                    |
| async_tree_io              | 549 ms                                                                         | 564 ms: 1.03x slower                                                                     |
| html5lib                   | 47.8 ms                                                                        | 49.1 ms: 1.03x slower                                                                    |
| xml_etree_process          | 47.3 ms                                                                        | 48.6 ms: 1.03x slower                                                                    |
| mako                       | 8.01 ms                                                                        | 8.24 ms: 1.03x slower                                                                    |
| async_tree_memoization_tg  | 246 ms                                                                         | 253 ms: 1.03x slower                                                                     |
| float                      | 58.2 ms                                                                        | 60.0 ms: 1.03x slower                                                                    |
| sympy_sum                  | 109 ms                                                                         | 112 ms: 1.03x slower                                                                     |
| pprint_pformat             | 1.34 sec                                                                       | 1.39 sec: 1.03x slower                                                                   |
| async_tree_memoization     | 276 ms                                                                         | 285 ms: 1.03x slower                                                                     |
| sqlglot_parse              | 1.06 ms                                                                        | 1.09 ms: 1.03x slower                                                                    |
| raytrace                   | 218 ms                                                                         | 226 ms: 1.03x slower                                                                     |
| async_tree_none            | 224 ms                                                                         | 232 ms: 1.03x slower                                                                     |
| genshi_text                | 21.6 ms                                                                        | 22.3 ms: 1.03x slower                                                                    |
| pprint_safe_repr           | 657 ms                                                                         | 680 ms: 1.03x slower                                                                     |
| spectral_norm              | 76.5 ms                                                                        | 79.2 ms: 1.03x slower                                                                    |
| dulwich_log                | 49.4 ms                                                                        | 51.1 ms: 1.03x slower                                                                    |
| sympy_integrate            | 15.4 ms                                                                        | 15.9 ms: 1.04x slower                                                                    |
| python_startup_no_site     | 19.7 ms                                                                        | 20.4 ms: 1.04x slower                                                                    |
| async_tree_none_tg         | 195 ms                                                                         | 202 ms: 1.04x slower                                                                     |
| sqlglot_transpile          | 1.30 ms                                                                        | 1.35 ms: 1.04x slower                                                                    |
| scimark_sor                | 94.8 ms                                                                        | 98.5 ms: 1.04x slower                                                                    |
| async_tree_cpu_io_mixed    | 467 ms                                                                         | 486 ms: 1.04x slower                                                                     |
| 2to3                       | 251 ms                                                                         | 262 ms: 1.04x slower                                                                     |
| genshi_xml                 | 46.4 ms                                                                        | 48.4 ms: 1.04x slower                                                                    |
| async_tree_cpu_io_mixed_tg | 454 ms                                                                         | 474 ms: 1.04x slower                                                                     |
| thrift                     | 733 us                                                                         | 769 us: 1.05x slower                                                                     |
| sympy_expand               | 385 ms                                                                         | 404 ms: 1.05x slower                                                                     |
| async_generators           | 280 ms                                                                         | 294 ms: 1.05x slower                                                                     |
| sympy_str                  | 217 ms                                                                         | 229 ms: 1.05x slower                                                                     |
| regex_compile              | 103 ms                                                                         | 109 ms: 1.05x slower                                                                     |
| pickle_pure_python         | 244 us                                                                         | 257 us: 1.06x slower                                                                     |
| crypto_pyaes               | 55.9 ms                                                                        | 59.1 ms: 1.06x slower                                                                    |
| hexiom                     | 4.99 ms                                                                        | 5.31 ms: 1.06x slower                                                                    |
| deltablue                  | 2.57 ms                                                                        | 2.74 ms: 1.06x slower                                                                    |
| fannkuch                   | 310 ms                                                                         | 330 ms: 1.07x slower                                                                     |
| chaos                      | 50.5 ms                                                                        | 54.0 ms: 1.07x slower                                                                    |
| pycparser                  | 836 ms                                                                         | 893 ms: 1.07x slower                                                                     |
| nqueens                    | 73.9 ms                                                                        | 79.1 ms: 1.07x slower                                                                    |
| generators                 | 25.7 ms                                                                        | 27.6 ms: 1.07x slower                                                                    |
| pyflate                    | 331 ms                                                                         | 355 ms: 1.07x slower                                                                     |
| deepcopy                   | 241 us                                                                         | 259 us: 1.07x slower                                                                     |
| go                         | 111 ms                                                                         | 119 ms: 1.08x slower                                                                     |
| comprehensions             | 13.1 us                                                                        | 14.3 us: 1.09x slower                                                                    |
| richards                   | 35.8 ms                                                                        | 39.1 ms: 1.09x slower                                                                    |
| scimark_fft                | 217 ms                                                                         | 237 ms: 1.09x slower                                                                     |
| richards_super             | 40.2 ms                                                                        | 44.2 ms: 1.10x slower                                                                    |
| meteor_contest             | 76.7 ms                                                                        | 84.3 ms: 1.10x slower                                                                    |
| scimark_monte_carlo        | 50.6 ms                                                                        | 55.6 ms: 1.10x slower                                                                    |
| deepcopy_memo              | 21.1 us                                                                        | 23.3 us: 1.11x slower                                                                    |
| nbody                      | 88.5 ms                                                                        | 99.2 ms: 1.12x slower                                                                    |
| typing_runtime_protocols   | 137 us                                                                         | 158 us: 1.15x slower                                                                     |
| Geometric mean             | (ref)                                                                          | 1.03x slower                                                                             |

Benchmark hidden because not significant (11): asyncio_tcp, regex_v8, scimark_lu, asyncio_tcp_ssl, coverage, bench_mp_pool, gc_traversal, bench_thread_pool, json, regex_effbot, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown