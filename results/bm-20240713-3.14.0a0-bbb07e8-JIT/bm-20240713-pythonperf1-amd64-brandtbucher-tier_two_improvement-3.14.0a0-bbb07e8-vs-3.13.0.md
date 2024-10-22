# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-amd64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.03x faster
- HPT reliability: 73.67%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 233 ms: 1.07x slower                                                             |
| docutils       | 1.57 sec                                                    | 1.78 sec: 1.13x slower                                                           |
| html5lib       | 38.6 ms                                                     | 39.6 ms: 1.03x slower                                                            |
| tornado_http   | 92.8 ms                                                     | 85.2 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 469 ms: 1.39x faster                                                             |
| async_tree_memoization_tg  | 288 ms                                                      | 241 ms: 1.20x faster                                                             |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.42 sec: 1.16x faster                                                           |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                             |
| async_tree_memoization     | 271 ms                                                      | 249 ms: 1.09x faster                                                             |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                             |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 385 ms: 1.03x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                            |
| async_generators           | 223 ms                                                      | 255 ms: 1.14x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                     |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 53.0 ms: 1.22x faster                                                            |
| float          | 48.1 ms                                                     | 44.5 ms: 1.08x faster                                                            |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                            |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                             |
| regex_compile  | 80.1 ms                                                     | 88.9 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                           |
| xml_etree_generate   | 53.3 ms                                                     | 51.3 ms: 1.04x faster                                                            |
| xml_etree_iterparse  | 62.3 ms                                                     | 60.2 ms: 1.03x faster                                                            |
| pickle_pure_python   | 183 us                                                      | 178 us: 1.03x faster                                                             |
| xml_etree_parse      | 93.2 ms                                                     | 91.1 ms: 1.02x faster                                                            |
| xml_etree_process    | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                            |
| json_loads           | 14.3 us                                                     | 14.3 us: 1.00x faster                                                            |
| json_dumps           | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                                            |
| unpickle_pure_python | 127 us                                                      | 128 us: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                            |
| python_startup_no_site | 17.8 ms                                                     | 17.5 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.10 ms: 1.22x faster                                                            |
| django_template | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                                            |
| genshi_text     | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                            |
| genshi_xml      | 32.8 ms                                                     | 45.2 ms: 1.38x slower                                                            |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 518 us: 16.75x faster                                                            |
| asyncio_tcp                | 654 ms                                                      | 469 ms: 1.39x faster                                                             |
| deepcopy_memo              | 21.8 us                                                     | 16.1 us: 1.35x faster                                                            |
| spectral_norm              | 59.2 ms                                                     | 45.1 ms: 1.31x faster                                                            |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                             |
| mako                       | 6.24 ms                                                     | 5.10 ms: 1.22x faster                                                            |
| nbody                      | 64.5 ms                                                     | 53.0 ms: 1.22x faster                                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 241 ms: 1.20x faster                                                             |
| scimark_fft                | 174 ms                                                      | 150 ms: 1.16x faster                                                             |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.42 sec: 1.16x faster                                                           |
| fannkuch                   | 245 ms                                                      | 219 ms: 1.12x faster                                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                            |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                             |
| pyflate                    | 275 ms                                                      | 250 ms: 1.10x faster                                                             |
| async_tree_memoization     | 271 ms                                                      | 249 ms: 1.09x faster                                                             |
| tornado_http               | 92.8 ms                                                     | 85.2 ms: 1.09x faster                                                            |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                             |
| float                      | 48.1 ms                                                     | 44.5 ms: 1.08x faster                                                            |
| pathlib                    | 81.2 ms                                                     | 75.1 ms: 1.08x faster                                                            |
| crypto_pyaes               | 42.8 ms                                                     | 39.7 ms: 1.08x faster                                                            |
| tomli_loads                | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                           |
| telco                      | 4.85 ms                                                     | 4.50 ms: 1.08x faster                                                            |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.5 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.19 ms: 1.07x faster                                                            |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                            |
| python_startup             | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                            |
| xml_etree_generate         | 53.3 ms                                                     | 51.3 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 62.3 ms                                                     | 60.2 ms: 1.03x faster                                                            |
| bench_thread_pool          | 828 us                                                      | 801 us: 1.03x faster                                                             |
| pickle_pure_python         | 183 us                                                      | 178 us: 1.03x faster                                                             |
| xml_etree_parse            | 93.2 ms                                                     | 91.1 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 493 ms                                                      | 483 ms: 1.02x faster                                                             |
| python_startup_no_site     | 17.8 ms                                                     | 17.5 ms: 1.02x faster                                                            |
| logging_simple             | 5.72 us                                                     | 5.64 us: 1.02x faster                                                            |
| logging_format             | 6.15 us                                                     | 6.09 us: 1.01x faster                                                            |
| xml_etree_process          | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                            |
| meteor_contest             | 72.3 ms                                                     | 71.7 ms: 1.01x faster                                                            |
| coverage                   | 46.7 ms                                                     | 46.5 ms: 1.01x faster                                                            |
| json_loads                 | 14.3 us                                                     | 14.3 us: 1.00x faster                                                            |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                             |
| json_dumps                 | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 127 us                                                      | 128 us: 1.01x slower                                                             |
| comprehensions             | 10.2 us                                                     | 10.4 us: 1.01x slower                                                            |
| html5lib                   | 38.6 ms                                                     | 39.6 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 385 ms: 1.03x slower                                                             |
| chaos                      | 37.9 ms                                                     | 39.4 ms: 1.04x slower                                                            |
| mdp                        | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                                           |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                             |
| sqlglot_parse              | 761 us                                                      | 815 us: 1.07x slower                                                             |
| 2to3                       | 217 ms                                                      | 233 ms: 1.07x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                            |
| create_gc_cycles           | 829 us                                                      | 899 us: 1.09x slower                                                             |
| logging_silent             | 51.0 ns                                                     | 55.5 ns: 1.09x slower                                                            |
| sympy_str                  | 166 ms                                                      | 181 ms: 1.09x slower                                                             |
| sympy_sum                  | 86.4 ms                                                     | 94.2 ms: 1.09x slower                                                            |
| nqueens                    | 55.5 ms                                                     | 60.6 ms: 1.09x slower                                                            |
| pylint                     | 211 ms                                                      | 230 ms: 1.09x slower                                                             |
| sqlglot_optimize           | 33.1 ms                                                     | 36.1 ms: 1.09x slower                                                            |
| sqlglot_transpile          | 952 us                                                      | 1.04 ms: 1.09x slower                                                            |
| go                         | 84.6 ms                                                     | 92.8 ms: 1.10x slower                                                            |
| sympy_expand               | 285 ms                                                      | 313 ms: 1.10x slower                                                             |
| regex_compile              | 80.1 ms                                                     | 88.9 ms: 1.11x slower                                                            |
| typing_runtime_protocols   | 100 us                                                      | 113 us: 1.12x slower                                                             |
| sqlglot_normalize          | 171 ms                                                      | 192 ms: 1.12x slower                                                             |
| richards                   | 26.0 ms                                                     | 29.4 ms: 1.13x slower                                                            |
| docutils                   | 1.57 sec                                                    | 1.78 sec: 1.13x slower                                                           |
| richards_super             | 29.3 ms                                                     | 33.2 ms: 1.13x slower                                                            |
| async_generators           | 223 ms                                                      | 255 ms: 1.14x slower                                                             |
| sympy_integrate            | 12.3 ms                                                     | 14.0 ms: 1.14x slower                                                            |
| raytrace                   | 156 ms                                                      | 180 ms: 1.15x slower                                                             |
| generators                 | 19.5 ms                                                     | 22.9 ms: 1.17x slower                                                            |
| scimark_sor                | 72.0 ms                                                     | 85.0 ms: 1.18x slower                                                            |
| django_template            | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                                            |
| deltablue                  | 1.86 ms                                                     | 2.22 ms: 1.19x slower                                                            |
| genshi_text                | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                            |
| hexiom                     | 3.69 ms                                                     | 4.59 ms: 1.24x slower                                                            |
| scimark_lu                 | 54.0 ms                                                     | 70.3 ms: 1.30x slower                                                            |
| genshi_xml                 | 32.8 ms                                                     | 45.2 ms: 1.38x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                     |

Benchmark hidden because not significant (9): pycparser, async_tree_cpu_io_mixed, bench_mp_pool, pprint_pformat, json, gc_traversal, async_tree_io, async_tree_io_tg, regex_v8
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 73.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown