# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: windows-amd64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 226 ms: 1.04x slower                                              |
| chameleon      | 4.72 ms                                                     | 5.10 ms: 1.08x slower                                             |
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                            |
| Geometric mean | (ref)                                                       | 1.04x slower                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 272 ms: 1.06x faster                                              |
| asyncio_tcp               | 654 ms                                                      | 631 ms: 1.04x faster                                              |
| async_tree_none           | 223 ms                                                      | 228 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed   | 387 ms                                                      | 396 ms: 1.02x slower                                              |
| async_generators          | 223 ms                                                      | 231 ms: 1.04x slower                                              |
| async_tree_none_tg        | 206 ms                                                      | 213 ms: 1.04x slower                                              |
| coroutines                | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                             |
| async_tree_io             | 521 ms                                                      | 603 ms: 1.16x slower                                              |
| async_tree_io_tg          | 512 ms                                                      | 627 ms: 1.22x slower                                              |
| Geometric mean            | (ref)                                                       | 1.04x slower                                                      |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| float          | 48.1 ms                                                     | 50.1 ms: 1.04x slower                                             |
| nbody          | 64.5 ms                                                     | 76.8 ms: 1.19x slower                                             |
| Geometric mean | (ref)                                                       | 1.08x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 83.9 ms: 1.05x slower                                             |
| regex_dna      | 114 ms                                                      | 123 ms: 1.08x slower                                              |
| regex_v8       | 14.7 ms                                                     | 16.4 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                       | 1.06x slower                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 91.5 ms: 1.02x faster                                             |
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                             |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.0 ms: 1.01x slower                                             |
| json_dumps           | 5.76 ms                                                     | 5.90 ms: 1.02x slower                                             |
| xml_etree_generate   | 53.3 ms                                                     | 55.4 ms: 1.04x slower                                             |
| tomli_loads          | 1.36 sec                                                    | 1.42 sec: 1.04x slower                                            |
| xml_etree_process    | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                             |
| pickle_pure_python   | 183 us                                                      | 194 us: 1.06x slower                                              |
| unpickle_pure_python | 127 us                                                      | 138 us: 1.09x slower                                              |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.5 ms: 1.01x slower                                             |
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                             |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 14.9 ms                                                     | 15.3 ms: 1.03x slower                                             |
| django_template | 21.8 ms                                                     | 22.7 ms: 1.04x slower                                             |
| mako            | 6.24 ms                                                     | 6.66 ms: 1.07x slower                                             |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 272 ms: 1.06x faster                                              |
| asyncio_tcp               | 654 ms                                                      | 631 ms: 1.04x faster                                              |
| coverage                  | 46.7 ms                                                     | 45.7 ms: 1.02x faster                                             |
| xml_etree_parse           | 93.2 ms                                                     | 91.5 ms: 1.02x faster                                             |
| telco                     | 4.85 ms                                                     | 4.79 ms: 1.01x faster                                             |
| json_loads                | 14.3 us                                                     | 14.2 us: 1.01x faster                                             |
| xml_etree_iterparse       | 62.3 ms                                                     | 63.0 ms: 1.01x slower                                             |
| python_startup            | 22.2 ms                                                     | 22.5 ms: 1.01x slower                                             |
| sympy_sum                 | 86.4 ms                                                     | 87.6 ms: 1.01x slower                                             |
| pathlib                   | 81.2 ms                                                     | 82.3 ms: 1.01x slower                                             |
| sympy_expand              | 285 ms                                                      | 289 ms: 1.01x slower                                              |
| meteor_contest            | 72.3 ms                                                     | 73.3 ms: 1.01x slower                                             |
| sympy_str                 | 166 ms                                                      | 169 ms: 1.02x slower                                              |
| dulwich_log               | 40.4 ms                                                     | 41.0 ms: 1.02x slower                                             |
| pidigits                  | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| gc_traversal              | 1.55 ms                                                     | 1.58 ms: 1.02x slower                                             |
| thrift                    | 8.68 ms                                                     | 8.84 ms: 1.02x slower                                             |
| logging_simple            | 5.72 us                                                     | 5.85 us: 1.02x slower                                             |
| bench_mp_pool             | 69.6 ms                                                     | 71.1 ms: 1.02x slower                                             |
| async_tree_none           | 223 ms                                                      | 228 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed   | 387 ms                                                      | 396 ms: 1.02x slower                                              |
| logging_format            | 6.15 us                                                     | 6.29 us: 1.02x slower                                             |
| mypy2                     | 429 ms                                                      | 439 ms: 1.02x slower                                              |
| json_dumps                | 5.76 ms                                                     | 5.90 ms: 1.02x slower                                             |
| sqlglot_optimize          | 33.1 ms                                                     | 33.9 ms: 1.03x slower                                             |
| genshi_text               | 14.9 ms                                                     | 15.3 ms: 1.03x slower                                             |
| async_generators          | 223 ms                                                      | 231 ms: 1.04x slower                                              |
| sympy_integrate           | 12.3 ms                                                     | 12.7 ms: 1.04x slower                                             |
| async_tree_none_tg        | 206 ms                                                      | 213 ms: 1.04x slower                                              |
| python_startup_no_site    | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                             |
| coroutines                | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                             |
| json                      | 2.98 ms                                                     | 3.10 ms: 1.04x slower                                             |
| xml_etree_generate        | 53.3 ms                                                     | 55.4 ms: 1.04x slower                                             |
| pprint_safe_repr          | 493 ms                                                      | 512 ms: 1.04x slower                                              |
| tomli_loads               | 1.36 sec                                                    | 1.42 sec: 1.04x slower                                            |
| float                     | 48.1 ms                                                     | 50.1 ms: 1.04x slower                                             |
| 2to3                      | 217 ms                                                      | 226 ms: 1.04x slower                                              |
| mdp                       | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                            |
| django_template           | 21.8 ms                                                     | 22.7 ms: 1.04x slower                                             |
| raytrace                  | 156 ms                                                      | 164 ms: 1.05x slower                                              |
| regex_compile             | 80.1 ms                                                     | 83.9 ms: 1.05x slower                                             |
| deepcopy_reduce           | 2.02 us                                                     | 2.11 us: 1.05x slower                                             |
| go                        | 84.6 ms                                                     | 88.6 ms: 1.05x slower                                             |
| sqlglot_normalize         | 171 ms                                                      | 180 ms: 1.05x slower                                              |
| xml_etree_process         | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                             |
| sqlglot_parse             | 761 us                                                      | 803 us: 1.06x slower                                              |
| typing_runtime_protocols  | 100 us                                                      | 106 us: 1.06x slower                                              |
| generators                | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                             |
| pprint_pformat            | 991 ms                                                      | 1.05 sec: 1.06x slower                                            |
| pickle_pure_python        | 183 us                                                      | 194 us: 1.06x slower                                              |
| sqlglot_transpile         | 952 us                                                      | 1.01 ms: 1.06x slower                                             |
| deepcopy                  | 223 us                                                      | 237 us: 1.06x slower                                              |
| docutils                  | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                            |
| chaos                     | 37.9 ms                                                     | 40.4 ms: 1.07x slower                                             |
| comprehensions            | 10.2 us                                                     | 10.9 us: 1.07x slower                                             |
| mako                      | 6.24 ms                                                     | 6.66 ms: 1.07x slower                                             |
| nqueens                   | 55.5 ms                                                     | 59.8 ms: 1.08x slower                                             |
| regex_dna                 | 114 ms                                                      | 123 ms: 1.08x slower                                              |
| deltablue                 | 1.86 ms                                                     | 2.01 ms: 1.08x slower                                             |
| pyflate                   | 275 ms                                                      | 298 ms: 1.08x slower                                              |
| chameleon                 | 4.72 ms                                                     | 5.10 ms: 1.08x slower                                             |
| spectral_norm             | 59.2 ms                                                     | 64.3 ms: 1.09x slower                                             |
| richards                  | 26.0 ms                                                     | 28.3 ms: 1.09x slower                                             |
| unpickle_pure_python      | 127 us                                                      | 138 us: 1.09x slower                                              |
| richards_super            | 29.3 ms                                                     | 32.1 ms: 1.09x slower                                             |
| scimark_fft               | 174 ms                                                      | 192 ms: 1.10x slower                                              |
| logging_silent            | 51.0 ns                                                     | 56.1 ns: 1.10x slower                                             |
| scimark_monte_carlo       | 40.3 ms                                                     | 44.4 ms: 1.10x slower                                             |
| fannkuch                  | 245 ms                                                      | 271 ms: 1.11x slower                                              |
| hexiom                    | 3.69 ms                                                     | 4.08 ms: 1.11x slower                                             |
| create_gc_cycles          | 829 us                                                      | 917 us: 1.11x slower                                              |
| crypto_pyaes              | 42.8 ms                                                     | 47.4 ms: 1.11x slower                                             |
| regex_v8                  | 14.7 ms                                                     | 16.4 ms: 1.12x slower                                             |
| scimark_lu                | 54.0 ms                                                     | 61.4 ms: 1.14x slower                                             |
| scimark_sor               | 72.0 ms                                                     | 81.9 ms: 1.14x slower                                             |
| deepcopy_memo             | 21.8 us                                                     | 24.9 us: 1.14x slower                                             |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.68 ms: 1.14x slower                                             |
| async_tree_io             | 521 ms                                                      | 603 ms: 1.16x slower                                              |
| nbody                     | 64.5 ms                                                     | 76.8 ms: 1.19x slower                                             |
| async_tree_io_tg          | 512 ms                                                      | 627 ms: 1.22x slower                                              |
| Geometric mean            | (ref)                                                       | 1.05x slower                                                      |

Benchmark hidden because not significant (10): bench_thread_pool, tornado_http, pycparser, regex_effbot, html5lib, genshi_xml, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_memoization, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown