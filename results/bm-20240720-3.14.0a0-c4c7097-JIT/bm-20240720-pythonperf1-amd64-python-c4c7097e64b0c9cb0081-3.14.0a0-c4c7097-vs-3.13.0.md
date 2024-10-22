# Results vs. 3.13.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.03x faster
- HPT reliability: 90.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 235 ms: 1.08x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.79 sec: 1.13x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.0 ms: 1.04x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 518 ms: 1.26x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 244 ms: 1.18x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.42 sec: 1.15x faster                                                     |
| async_tree_none            | 223 ms                                                      | 199 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 251 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 528 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.07x slower                                                      |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 50.1 ms: 1.29x faster                                                      |
| float          | 48.1 ms                                                     | 44.2 ms: 1.09x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 122 ms: 1.07x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 87.6 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.23 sec: 1.10x faster                                                     |
| pickle_pure_python   | 183 us                                                      | 176 us: 1.04x faster                                                       |
| xml_etree_generate   | 53.3 ms                                                     | 51.2 ms: 1.04x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.3 ms: 1.01x faster                                                      |
| unpickle_pure_python | 127 us                                                      | 128 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (4): json_dumps, xml_etree_iterparse, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.2 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.26 ms: 1.19x faster                                                      |
| django_template | 21.8 ms                                                     | 25.3 ms: 1.16x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.3 ms: 1.23x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 45.6 ms: 1.39x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 505 us: 17.19x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 15.6 us: 1.40x faster                                                      |
| nbody                      | 64.5 ms                                                     | 50.1 ms: 1.29x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 46.1 ms: 1.28x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 518 ms: 1.26x faster                                                       |
| deepcopy                   | 223 us                                                      | 179 us: 1.25x faster                                                       |
| mako                       | 6.24 ms                                                     | 5.26 ms: 1.19x faster                                                      |
| scimark_fft                | 174 ms                                                      | 147 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 244 ms: 1.18x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.42 sec: 1.15x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.78 us: 1.13x faster                                                      |
| pyflate                    | 275 ms                                                      | 245 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.08 ms: 1.12x faster                                                      |
| async_tree_none            | 223 ms                                                      | 199 ms: 1.12x faster                                                       |
| fannkuch                   | 245 ms                                                      | 220 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.23 sec: 1.10x faster                                                     |
| telco                      | 4.85 ms                                                     | 4.45 ms: 1.09x faster                                                      |
| float                      | 48.1 ms                                                     | 44.2 ms: 1.09x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 251 ms: 1.08x faster                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 39.8 ms: 1.08x faster                                                      |
| pprint_safe_repr           | 493 ms                                                      | 461 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.9 ms: 1.06x faster                                                      |
| pprint_pformat             | 991 ms                                                      | 944 ms: 1.05x faster                                                       |
| pickle_pure_python         | 183 us                                                      | 176 us: 1.04x faster                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 51.2 ms: 1.04x faster                                                      |
| meteor_contest             | 72.3 ms                                                     | 70.2 ms: 1.03x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 807 us: 1.03x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.3 ms: 1.01x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.6 ms: 1.01x faster                                                      |
| logging_simple             | 5.72 us                                                     | 5.69 us: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.56 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 128 us: 1.01x slower                                                       |
| coverage                   | 46.7 ms                                                     | 47.2 ms: 1.01x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 71.1 ms: 1.02x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.2 ms: 1.03x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 528 ms: 1.03x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.2 ms: 1.03x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.0 ms: 1.04x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.46 sec: 1.05x slower                                                     |
| sqlglot_parse              | 761 us                                                      | 808 us: 1.06x slower                                                       |
| regex_dna                  | 114 ms                                                      | 122 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 35.5 ms: 1.07x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 59.7 ms: 1.08x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 55.0 ns: 1.08x slower                                                      |
| 2to3                       | 217 ms                                                      | 235 ms: 1.08x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.1 ms: 1.09x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.03 ms: 1.09x slower                                                      |
| sympy_str                  | 166 ms                                                      | 181 ms: 1.09x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 94.4 ms: 1.09x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 906 us: 1.09x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 87.6 ms: 1.09x slower                                                      |
| go                         | 84.6 ms                                                     | 93.3 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 189 ms: 1.10x slower                                                       |
| pylint                     | 211 ms                                                      | 232 ms: 1.10x slower                                                       |
| richards_super             | 29.3 ms                                                     | 32.4 ms: 1.10x slower                                                      |
| richards                   | 26.0 ms                                                     | 28.8 ms: 1.10x slower                                                      |
| sympy_expand               | 285 ms                                                      | 316 ms: 1.11x slower                                                       |
| raytrace                   | 156 ms                                                      | 174 ms: 1.12x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 113 us: 1.12x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.79 sec: 1.13x slower                                                     |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 14.1 ms: 1.15x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.3 ms: 1.16x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.22 ms: 1.19x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 86.1 ms: 1.20x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 18.3 ms: 1.23x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.60 ms: 1.25x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 67.7 ms: 1.25x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 45.6 ms: 1.39x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (11): pycparser, async_tree_cpu_io_mixed, comprehensions, regex_effbot, json_dumps, xml_etree_iterparse, json_loads, async_tree_io, logging_format, xml_etree_parse, json
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 90.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown