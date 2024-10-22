# Results vs. 3.13.0

- fork: mdboom
- ref: mdboom_08_17
- machine: windows-amd64
- commit hash: 7ab5aad
- commit date: 2024-08-28
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 233 ms: 1.07x slower                                               |
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                             |
| html5lib       | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                       | 1.07x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 539 ms: 1.21x faster                                               |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                               |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 394 ms: 1.05x slower                                               |
| async_tree_io_tg           | 512 ms                                                      | 548 ms: 1.07x slower                                               |
| async_tree_io              | 521 ms                                                      | 581 ms: 1.12x slower                                               |
| async_generators           | 223 ms                                                      | 253 ms: 1.14x slower                                               |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                              |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| float          | 48.1 ms                                                     | 56.1 ms: 1.17x slower                                              |
| nbody          | 64.5 ms                                                     | 85.1 ms: 1.32x slower                                              |
| Geometric mean | (ref)                                                       | 1.16x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                              |
| regex_v8       | 14.7 ms                                                     | 15.0 ms: 1.02x slower                                              |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                               |
| regex_compile  | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                              |
| Geometric mean | (ref)                                                       | 1.04x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 96.0 ms: 1.03x slower                                              |
| json_loads           | 14.3 us                                                     | 14.8 us: 1.03x slower                                              |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.1 ms: 1.04x slower                                              |
| json_dumps           | 5.76 ms                                                     | 6.08 ms: 1.06x slower                                              |
| xml_etree_generate   | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                              |
| xml_etree_process    | 36.5 ms                                                     | 40.2 ms: 1.10x slower                                              |
| pickle_pure_python   | 183 us                                                      | 210 us: 1.14x slower                                               |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                             |
| unpickle_pure_python | 127 us                                                      | 148 us: 1.17x slower                                               |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.98 ms: 1.12x slower                                              |
| genshi_xml      | 32.8 ms                                                     | 37.1 ms: 1.13x slower                                              |
| django_template | 21.8 ms                                                     | 25.0 ms: 1.15x slower                                              |
| genshi_text     | 14.9 ms                                                     | 17.5 ms: 1.18x slower                                              |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 520 us: 16.68x faster                                              |
| asyncio_tcp                | 654 ms                                                      | 539 ms: 1.21x faster                                               |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                               |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                               |
| deepcopy_memo              | 21.8 us                                                     | 20.3 us: 1.07x faster                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                              |
| pathlib                    | 81.2 ms                                                     | 77.9 ms: 1.04x faster                                              |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.04x faster                                               |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                              |
| bench_mp_pool              | 69.6 ms                                                     | 68.4 ms: 1.02x faster                                              |
| python_startup_no_site     | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                              |
| gc_traversal               | 1.55 ms                                                     | 1.58 ms: 1.02x slower                                              |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| regex_v8                   | 14.7 ms                                                     | 15.0 ms: 1.02x slower                                              |
| mdp                        | 1.38 sec                                                    | 1.42 sec: 1.02x slower                                             |
| telco                      | 4.85 ms                                                     | 4.99 ms: 1.03x slower                                              |
| xml_etree_parse            | 93.2 ms                                                     | 96.0 ms: 1.03x slower                                              |
| json_loads                 | 14.3 us                                                     | 14.8 us: 1.03x slower                                              |
| json                       | 2.98 ms                                                     | 3.09 ms: 1.04x slower                                              |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                               |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.1 ms: 1.04x slower                                              |
| sympy_sum                  | 86.4 ms                                                     | 90.8 ms: 1.05x slower                                              |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 394 ms: 1.05x slower                                               |
| json_dumps                 | 5.76 ms                                                     | 6.08 ms: 1.06x slower                                              |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                              |
| dulwich_log                | 40.4 ms                                                     | 43.0 ms: 1.07x slower                                              |
| async_tree_io_tg           | 512 ms                                                      | 548 ms: 1.07x slower                                               |
| 2to3                       | 217 ms                                                      | 233 ms: 1.07x slower                                               |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                               |
| coverage                   | 46.7 ms                                                     | 50.1 ms: 1.07x slower                                              |
| pylint                     | 211 ms                                                      | 227 ms: 1.08x slower                                               |
| meteor_contest             | 72.3 ms                                                     | 77.8 ms: 1.08x slower                                              |
| sympy_expand               | 285 ms                                                      | 308 ms: 1.08x slower                                               |
| xml_etree_generate         | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                              |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                              |
| html5lib                   | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                              |
| sqlglot_optimize           | 33.1 ms                                                     | 36.0 ms: 1.09x slower                                              |
| create_gc_cycles           | 829 us                                                      | 908 us: 1.10x slower                                               |
| xml_etree_process          | 36.5 ms                                                     | 40.2 ms: 1.10x slower                                              |
| logging_format             | 6.15 us                                                     | 6.78 us: 1.10x slower                                              |
| logging_simple             | 5.72 us                                                     | 6.32 us: 1.10x slower                                              |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                             |
| async_tree_io              | 521 ms                                                      | 581 ms: 1.12x slower                                               |
| mako                       | 6.24 ms                                                     | 6.98 ms: 1.12x slower                                              |
| crypto_pyaes               | 42.8 ms                                                     | 48.1 ms: 1.12x slower                                              |
| pprint_safe_repr           | 493 ms                                                      | 555 ms: 1.13x slower                                               |
| regex_compile              | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                              |
| sqlglot_normalize          | 171 ms                                                      | 193 ms: 1.13x slower                                               |
| genshi_xml                 | 32.8 ms                                                     | 37.1 ms: 1.13x slower                                              |
| async_generators           | 223 ms                                                      | 253 ms: 1.14x slower                                               |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.14x slower                                               |
| pickle_pure_python         | 183 us                                                      | 210 us: 1.14x slower                                               |
| pycparser                  | 758 ms                                                      | 871 ms: 1.15x slower                                               |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                              |
| django_template            | 21.8 ms                                                     | 25.0 ms: 1.15x slower                                              |
| pprint_pformat             | 991 ms                                                      | 1.14 sec: 1.15x slower                                             |
| go                         | 84.6 ms                                                     | 97.6 ms: 1.15x slower                                              |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.16x slower                                              |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                             |
| chaos                      | 37.9 ms                                                     | 44.0 ms: 1.16x slower                                              |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                              |
| float                      | 48.1 ms                                                     | 56.1 ms: 1.17x slower                                              |
| nqueens                    | 55.5 ms                                                     | 64.7 ms: 1.17x slower                                              |
| sqlglot_parse              | 761 us                                                      | 889 us: 1.17x slower                                               |
| unpickle_pure_python       | 127 us                                                      | 148 us: 1.17x slower                                               |
| scimark_lu                 | 54.0 ms                                                     | 63.3 ms: 1.17x slower                                              |
| genshi_text                | 14.9 ms                                                     | 17.5 ms: 1.18x slower                                              |
| pyflate                    | 275 ms                                                      | 325 ms: 1.18x slower                                               |
| hexiom                     | 3.69 ms                                                     | 4.36 ms: 1.18x slower                                              |
| scimark_fft                | 174 ms                                                      | 207 ms: 1.19x slower                                               |
| raytrace                   | 156 ms                                                      | 187 ms: 1.20x slower                                               |
| deltablue                  | 1.86 ms                                                     | 2.24 ms: 1.20x slower                                              |
| spectral_norm              | 59.2 ms                                                     | 71.3 ms: 1.21x slower                                              |
| fannkuch                   | 245 ms                                                      | 297 ms: 1.21x slower                                               |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.86 ms: 1.22x slower                                              |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.5 ms: 1.23x slower                                              |
| logging_silent             | 51.0 ns                                                     | 62.9 ns: 1.23x slower                                              |
| richards                   | 26.0 ms                                                     | 33.3 ms: 1.28x slower                                              |
| richards_super             | 29.3 ms                                                     | 37.7 ms: 1.29x slower                                              |
| scimark_sor                | 72.0 ms                                                     | 93.0 ms: 1.29x slower                                              |
| nbody                      | 64.5 ms                                                     | 85.1 ms: 1.32x slower                                              |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                       |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, bench_thread_pool, python_startup, async_tree_cpu_io_mixed, tornado_http, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown