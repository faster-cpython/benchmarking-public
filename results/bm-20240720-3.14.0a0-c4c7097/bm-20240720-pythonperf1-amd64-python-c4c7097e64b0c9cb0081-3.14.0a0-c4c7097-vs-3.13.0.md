# Results vs. 3.13.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 223 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 91.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 524 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| async_tree_none            | 223 ms                                                      | 216 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 541 ms: 1.06x slower                                                       |
| async_tree_io              | 521 ms                                                      | 556 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 55.4 ms: 1.15x slower                                                      |
| nbody          | 64.5 ms                                                     | 77.3 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 86.8 ms: 1.08x slower                                                      |
| regex_dna      | 114 ms                                                      | 126 ms: 1.10x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 16.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 5.76 ms                                                     | 5.92 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.7 ms: 1.04x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 56.5 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.3 ms: 1.07x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 199 us: 1.09x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.51 sec: 1.11x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 141 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.4 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 23.0 ms: 1.06x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.0 ms: 1.08x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                      |
| mako            | 6.24 ms                                                     | 7.11 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 514 us: 16.88x faster                                                      |
| deepcopy                   | 223 us                                                      | 175 us: 1.28x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 524 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 19.6 us: 1.12x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.4 ms: 1.04x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 67.1 ms: 1.04x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 799 us: 1.04x faster                                                       |
| async_tree_none            | 223 ms                                                      | 216 ms: 1.03x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 91.3 ms: 1.02x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 80.3 ms: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.81 ms: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| meteor_contest             | 72.3 ms                                                     | 73.3 ms: 1.01x slower                                                      |
| json                       | 2.98 ms                                                     | 3.06 ms: 1.03x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.92 ms: 1.03x slower                                                      |
| 2to3                       | 217 ms                                                      | 223 ms: 1.03x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 89.0 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 34.2 ms: 1.03x slower                                                      |
| sympy_str                  | 166 ms                                                      | 172 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.7 ms: 1.04x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.2 ms: 1.04x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                      |
| sympy_expand               | 285 ms                                                      | 298 ms: 1.04x slower                                                       |
| logging_simple             | 5.72 us                                                     | 5.99 us: 1.05x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 105 us: 1.05x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 180 ms: 1.05x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.48 us: 1.05x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 541 ms: 1.06x slower                                                       |
| django_template            | 21.8 ms                                                     | 23.0 ms: 1.06x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.47 sec: 1.06x slower                                                     |
| xml_etree_generate         | 53.3 ms                                                     | 56.5 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 524 ms: 1.06x slower                                                       |
| async_tree_io              | 521 ms                                                      | 556 ms: 1.07x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 39.3 ms: 1.07x slower                                                      |
| go                         | 84.6 ms                                                     | 91.0 ms: 1.08x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.0 ms: 1.08x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.07 sec: 1.08x slower                                                     |
| comprehensions             | 10.2 us                                                     | 11.1 us: 1.08x slower                                                      |
| raytrace                   | 156 ms                                                      | 169 ms: 1.08x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 86.8 ms: 1.08x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 60.2 ms: 1.08x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.1 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 199 us: 1.09x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 903 us: 1.09x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.05 ms: 1.10x slower                                                      |
| regex_dna                  | 114 ms                                                      | 126 ms: 1.10x slower                                                       |
| pyflate                    | 275 ms                                                      | 304 ms: 1.10x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.51 sec: 1.11x slower                                                     |
| unpickle_pure_python       | 127 us                                                      | 141 us: 1.11x slower                                                       |
| richards                   | 26.0 ms                                                     | 28.9 ms: 1.11x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.07 ms: 1.11x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 847 us: 1.11x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.12 ms: 1.12x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 60.3 ms: 1.12x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 16.4 ms: 1.12x slower                                                      |
| richards_super             | 29.3 ms                                                     | 33.0 ms: 1.12x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 57.9 ns: 1.14x slower                                                      |
| scimark_fft                | 174 ms                                                      | 198 ms: 1.14x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.11 ms: 1.14x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 48.9 ms: 1.14x slower                                                      |
| fannkuch                   | 245 ms                                                      | 280 ms: 1.14x slower                                                       |
| float                      | 48.1 ms                                                     | 55.4 ms: 1.15x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.72 ms: 1.16x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 69.5 ms: 1.17x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 47.9 ms: 1.19x slower                                                      |
| nbody                      | 64.5 ms                                                     | 77.3 ms: 1.20x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 86.8 ms: 1.21x slower                                                      |
| coverage                   | 46.7 ms                                                     | 79.8 ms: 1.71x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (9): python_startup_no_site, pylint, xml_etree_parse, json_loads, gc_traversal, asyncio_tcp_ssl, regex_effbot, async_tree_cpu_io_mixed, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown