# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-amd64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.04x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 251 ms: 1.16x slower                                                         |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                       |
| html5lib       | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                        |
| tornado_http   | 92.8 ms                                                     | 101 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                         |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.52 sec: 1.08x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 211 ms: 1.02x slower                                                         |
| async_tree_memoization     | 271 ms                                                      | 283 ms: 1.04x slower                                                         |
| async_tree_io              | 521 ms                                                      | 557 ms: 1.07x slower                                                         |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 406 ms: 1.08x slower                                                         |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                        |
| async_generators           | 223 ms                                                      | 269 ms: 1.21x slower                                                         |
| async_tree_io_tg           | 512 ms                                                      | 637 ms: 1.24x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 51.8 ms: 1.24x faster                                                        |
| float          | 48.1 ms                                                     | 46.7 ms: 1.03x faster                                                        |
| pidigits       | 148 ms                                                      | 148 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 92.5 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                 |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list          | 2.89 us                                                     | 2.74 us: 1.05x faster                                                        |
| xml_etree_generate   | 53.3 ms                                                     | 51.0 ms: 1.05x faster                                                        |
| tomli_loads          | 1.36 sec                                                    | 1.32 sec: 1.03x faster                                                       |
| pickle_dict          | 18.0 us                                                     | 17.9 us: 1.01x faster                                                        |
| pickle               | 7.34 us                                                     | 7.38 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.5 ms: 1.02x slower                                                        |
| xml_etree_parse      | 93.2 ms                                                     | 95.3 ms: 1.02x slower                                                        |
| unpickle_list        | 2.72 us                                                     | 2.86 us: 1.05x slower                                                        |
| unpickle             | 8.63 us                                                     | 9.08 us: 1.05x slower                                                        |
| json_dumps           | 5.76 ms                                                     | 6.24 ms: 1.08x slower                                                        |
| pickle_pure_python   | 183 us                                                      | 202 us: 1.10x slower                                                         |
| unpickle_pure_python | 127 us                                                      | 147 us: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                        |
| python_startup         | 22.2 ms                                                     | 24.3 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.02 ms: 1.24x faster                                                        |
| django_template | 21.8 ms                                                     | 27.0 ms: 1.24x slower                                                        |
| genshi_text     | 14.9 ms                                                     | 19.5 ms: 1.31x slower                                                        |
| genshi_xml      | 32.8 ms                                                     | 46.9 ms: 1.43x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.17x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 526 us: 16.49x faster                                                        |
| deepcopy_memo              | 21.8 us                                                     | 17.1 us: 1.28x faster                                                        |
| nbody                      | 64.5 ms                                                     | 51.8 ms: 1.24x faster                                                        |
| mako                       | 6.24 ms                                                     | 5.02 ms: 1.24x faster                                                        |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                         |
| scimark_sor                | 72.0 ms                                                     | 62.8 ms: 1.15x faster                                                        |
| spectral_norm              | 59.2 ms                                                     | 53.2 ms: 1.11x faster                                                        |
| scimark_fft                | 174 ms                                                      | 157 ms: 1.11x faster                                                         |
| telco                      | 4.85 ms                                                     | 4.42 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 493 ms                                                      | 449 ms: 1.10x faster                                                         |
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                         |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.52 sec: 1.08x faster                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 39.9 ms: 1.07x faster                                                        |
| pprint_pformat             | 991 ms                                                      | 924 ms: 1.07x faster                                                         |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.8 ms: 1.07x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                        |
| pickle_list                | 2.89 us                                                     | 2.74 us: 1.05x faster                                                        |
| xml_etree_generate         | 53.3 ms                                                     | 51.0 ms: 1.05x faster                                                        |
| fannkuch                   | 245 ms                                                      | 234 ms: 1.04x faster                                                         |
| tomli_loads                | 1.36 sec                                                    | 1.32 sec: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.26 ms: 1.03x faster                                                        |
| float                      | 48.1 ms                                                     | 46.7 ms: 1.03x faster                                                        |
| pickle_dict                | 18.0 us                                                     | 17.9 us: 1.01x faster                                                        |
| sqlite_synth               | 1.60 us                                                     | 1.59 us: 1.01x faster                                                        |
| pidigits                   | 148 ms                                                      | 148 ms: 1.01x faster                                                         |
| pickle                     | 7.34 us                                                     | 7.38 us: 1.01x slower                                                        |
| coverage                   | 46.7 ms                                                     | 47.1 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.5 ms: 1.02x slower                                                        |
| scimark_lu                 | 54.0 ms                                                     | 55.0 ms: 1.02x slower                                                        |
| xml_etree_parse            | 93.2 ms                                                     | 95.3 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 206 ms                                                      | 211 ms: 1.02x slower                                                         |
| dulwich_log                | 40.4 ms                                                     | 41.5 ms: 1.03x slower                                                        |
| html5lib                   | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                        |
| python_startup_no_site     | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                        |
| meteor_contest             | 72.3 ms                                                     | 75.2 ms: 1.04x slower                                                        |
| async_tree_memoization     | 271 ms                                                      | 283 ms: 1.04x slower                                                         |
| unpickle_list              | 2.72 us                                                     | 2.86 us: 1.05x slower                                                        |
| pyflate                    | 275 ms                                                      | 289 ms: 1.05x slower                                                         |
| unpickle                   | 8.63 us                                                     | 9.08 us: 1.05x slower                                                        |
| async_tree_io              | 521 ms                                                      | 557 ms: 1.07x slower                                                         |
| logging_simple             | 5.72 us                                                     | 6.18 us: 1.08x slower                                                        |
| logging_format             | 6.15 us                                                     | 6.66 us: 1.08x slower                                                        |
| json_dumps                 | 5.76 ms                                                     | 6.24 ms: 1.08x slower                                                        |
| tornado_http               | 92.8 ms                                                     | 101 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 406 ms: 1.08x slower                                                         |
| python_startup             | 22.2 ms                                                     | 24.3 ms: 1.10x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.10x slower                                                        |
| pickle_pure_python         | 183 us                                                      | 202 us: 1.10x slower                                                         |
| mdp                        | 1.38 sec                                                    | 1.55 sec: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                        |
| logging_silent             | 51.0 ns                                                     | 57.4 ns: 1.13x slower                                                        |
| go                         | 84.6 ms                                                     | 95.4 ms: 1.13x slower                                                        |
| comprehensions             | 10.2 us                                                     | 11.6 us: 1.13x slower                                                        |
| nqueens                    | 55.5 ms                                                     | 63.5 ms: 1.14x slower                                                        |
| regex_compile              | 80.1 ms                                                     | 92.5 ms: 1.15x slower                                                        |
| typing_runtime_protocols   | 100 us                                                      | 116 us: 1.16x slower                                                         |
| 2to3                       | 217 ms                                                      | 251 ms: 1.16x slower                                                         |
| sympy_expand               | 285 ms                                                      | 331 ms: 1.16x slower                                                         |
| unpickle_pure_python       | 127 us                                                      | 147 us: 1.16x slower                                                         |
| generators                 | 19.5 ms                                                     | 22.9 ms: 1.18x slower                                                        |
| sympy_str                  | 166 ms                                                      | 196 ms: 1.18x slower                                                         |
| sympy_sum                  | 86.4 ms                                                     | 102 ms: 1.18x slower                                                         |
| sqlglot_parse              | 761 us                                                      | 915 us: 1.20x slower                                                         |
| async_generators           | 223 ms                                                      | 269 ms: 1.21x slower                                                         |
| sqlglot_normalize          | 171 ms                                                      | 209 ms: 1.22x slower                                                         |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                       |
| django_template            | 21.8 ms                                                     | 27.0 ms: 1.24x slower                                                        |
| async_tree_io_tg           | 512 ms                                                      | 637 ms: 1.24x slower                                                         |
| gc_traversal               | 1.55 ms                                                     | 1.96 ms: 1.26x slower                                                        |
| deltablue                  | 1.86 ms                                                     | 2.37 ms: 1.27x slower                                                        |
| sqlglot_transpile          | 952 us                                                      | 1.21 ms: 1.28x slower                                                        |
| bench_mp_pool              | 69.6 ms                                                     | 89.3 ms: 1.28x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 15.9 ms: 1.29x slower                                                        |
| sqlglot_optimize           | 33.1 ms                                                     | 43.2 ms: 1.31x slower                                                        |
| genshi_text                | 14.9 ms                                                     | 19.5 ms: 1.31x slower                                                        |
| richards                   | 26.0 ms                                                     | 34.5 ms: 1.32x slower                                                        |
| richards_super             | 29.3 ms                                                     | 39.1 ms: 1.33x slower                                                        |
| pylint                     | 211 ms                                                      | 283 ms: 1.34x slower                                                         |
| raytrace                   | 156 ms                                                      | 214 ms: 1.37x slower                                                         |
| hexiom                     | 3.69 ms                                                     | 5.25 ms: 1.42x slower                                                        |
| genshi_xml                 | 32.8 ms                                                     | 46.9 ms: 1.43x slower                                                        |
| unpack_sequence            | 40.0 ns                                                     | 60.8 ns: 1.52x slower                                                        |
| create_gc_cycles           | 829 us                                                      | 1.42 ms: 1.71x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                 |

Benchmark hidden because not significant (12): pycparser, async_tree_none, regex_effbot, bench_thread_pool, xml_etree_process, async_tree_cpu_io_mixed, regex_dna, pathlib, json_loads, regex_v8, json, asyncio_tcp
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown