# Results vs. 3.13.0b2

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-amd64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.6 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 549 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 56.4 ms: 1.13x slower                                                      |
| nbody          | 67.6 ms                                                         | 85.8 ms: 1.27x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 93.3 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.1 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.6 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.8 ms: 1.11x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.31 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.2 ms: 1.16x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 217 us: 1.23x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 152 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.40 ms: 1.16x slower                                                      |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 39.5 ms: 1.25x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.21x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 541 us: 14.99x faster                                                      |
| deepcopy                   | 220 us                                                          | 196 us: 1.12x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 549 ms: 1.10x faster                                                       |
| json                       | 3.19 ms                                                         | 3.03 ms: 1.05x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 21.3 us: 1.04x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 2.03 us: 1.02x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 902 us: 1.02x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| regex_dna                  | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 93.1 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                       |
| bench_thread_pool          | 768 us                                                          | 804 us: 1.05x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.6 ms: 1.05x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 80.6 ms: 1.06x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 69.4 ms: 1.07x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.06 ms: 1.08x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.2 ms: 1.08x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| sympy_sum                  | 84.4 ms                                                         | 92.0 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.4 ms: 1.10x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.37 us: 1.10x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 58.8 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                          | 248 ms: 1.11x slower                                                       |
| logging_format             | 6.22 us                                                         | 6.92 us: 1.11x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 77.9 ms: 1.11x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| pylint                     | 205 ms                                                          | 229 ms: 1.12x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 63.4 ms: 1.12x slower                                                      |
| 2to3                       | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 6.31 ms: 1.12x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.8 ms: 1.13x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 71.8 ms: 1.13x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.9 ms: 1.13x slower                                                      |
| float                      | 49.7 ms                                                         | 56.4 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 197 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.85 ms: 1.14x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 51.9 ms: 1.14x slower                                                      |
| sympy_str                  | 159 ms                                                          | 182 ms: 1.14x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 93.6 ms: 1.14x slower                                                      |
| sympy_expand               | 271 ms                                                          | 310 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 116 us: 1.15x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 544 ms: 1.16x slower                                                       |
| xml_etree_process          | 36.4 ms                                                         | 42.2 ms: 1.16x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.40 ms: 1.16x slower                                                      |
| pyflate                    | 279 ms                                                          | 325 ms: 1.17x slower                                                       |
| chaos                      | 38.4 ms                                                         | 45.0 ms: 1.17x slower                                                      |
| coverage                   | 42.1 ms                                                         | 49.4 ms: 1.17x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 66.4 ms: 1.17x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.12 ms: 1.18x slower                                                      |
| django_template            | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 93.3 ms: 1.20x slower                                                      |
| comprehensions             | 10.4 us                                                         | 12.4 us: 1.20x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| pycparser                  | 754 ms                                                          | 912 ms: 1.21x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.17 sec: 1.21x slower                                                     |
| pprint_safe_repr           | 474 ms                                                          | 574 ms: 1.21x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 64.4 ns: 1.22x slower                                                      |
| go                         | 82.1 ms                                                         | 99.8 ms: 1.22x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 913 us: 1.22x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 92.2 ms: 1.22x slower                                                      |
| fannkuch                   | 243 ms                                                          | 298 ms: 1.23x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.31 ms: 1.23x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 217 us: 1.23x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.61 ms: 1.24x slower                                                      |
| richards                   | 26.7 ms                                                         | 33.1 ms: 1.24x slower                                                      |
| scimark_fft                | 171 ms                                                          | 212 ms: 1.24x slower                                                       |
| richards_super             | 30.2 ms                                                         | 37.5 ms: 1.24x slower                                                      |
| raytrace                   | 162 ms                                                          | 202 ms: 1.25x slower                                                       |
| genshi_xml                 | 31.6 ms                                                         | 39.5 ms: 1.25x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 152 us: 1.25x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                      |
| nbody                      | 67.6 ms                                                         | 85.8 ms: 1.27x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 52.6 ms: 1.34x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, pidigits, regex_effbot, gc_traversal, async_tree_none, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown