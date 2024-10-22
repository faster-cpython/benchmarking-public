# Results vs. 3.13.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-amd64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 227 ms: 1.04x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                               |
| html5lib       | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                                                |
| tornado_http   | 92.8 ms                                                     | 91.6 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 533 ms: 1.23x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.17x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 193 ms: 1.07x faster                                                                 |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                                 |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 387 ms: 1.03x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 533 ms: 1.04x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 547 ms: 1.05x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                                |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.79 sec: 1.09x slower                                                               |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.01x slower                                                                 |
| float          | 48.1 ms                                                     | 56.3 ms: 1.17x slower                                                                |
| nbody          | 64.5 ms                                                     | 83.8 ms: 1.30x slower                                                                |
| Geometric mean | (ref)                                                       | 1.16x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                                |
| regex_v8       | 14.7 ms                                                     | 14.6 ms: 1.01x faster                                                                |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                                 |
| regex_compile  | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.0 us: 1.03x faster                                                                |
| xml_etree_parse      | 93.2 ms                                                     | 91.9 ms: 1.01x faster                                                                |
| json_dumps           | 5.76 ms                                                     | 6.00 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                                                |
| xml_etree_generate   | 53.3 ms                                                     | 58.1 ms: 1.09x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 40.6 ms: 1.11x slower                                                                |
| pickle_pure_python   | 183 us                                                      | 209 us: 1.14x slower                                                                 |
| tomli_loads          | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| unpickle_pure_python | 127 us                                                      | 150 us: 1.19x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 23.7 ms: 1.09x slower                                                                |
| genshi_xml      | 32.8 ms                                                     | 36.3 ms: 1.11x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 16.7 ms: 1.12x slower                                                                |
| mako            | 6.24 ms                                                     | 7.48 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 530 us: 16.38x faster                                                                |
| asyncio_tcp                | 654 ms                                                      | 533 ms: 1.23x faster                                                                 |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.17x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 193 ms: 1.07x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                                |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                                 |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.04x faster                                                                 |
| bench_mp_pool              | 69.6 ms                                                     | 67.3 ms: 1.03x faster                                                                |
| bench_thread_pool          | 828 us                                                      | 806 us: 1.03x faster                                                                 |
| json_loads                 | 14.3 us                                                     | 14.0 us: 1.03x faster                                                                |
| python_startup             | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                                |
| json                       | 2.98 ms                                                     | 2.93 ms: 1.02x faster                                                                |
| xml_etree_parse            | 93.2 ms                                                     | 91.9 ms: 1.01x faster                                                                |
| tornado_http               | 92.8 ms                                                     | 91.6 ms: 1.01x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                                |
| pathlib                    | 81.2 ms                                                     | 80.5 ms: 1.01x faster                                                                |
| regex_v8                   | 14.7 ms                                                     | 14.6 ms: 1.01x faster                                                                |
| deepcopy_memo              | 21.8 us                                                     | 21.7 us: 1.01x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.87 ms: 1.00x slower                                                                |
| coverage                   | 46.7 ms                                                     | 47.4 ms: 1.01x slower                                                                |
| pidigits                   | 148 ms                                                      | 151 ms: 1.01x slower                                                                 |
| mdp                        | 1.38 sec                                                    | 1.40 sec: 1.01x slower                                                               |
| sympy_sum                  | 86.4 ms                                                     | 89.3 ms: 1.03x slower                                                                |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 387 ms: 1.03x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 533 ms: 1.04x slower                                                                 |
| json_dumps                 | 5.76 ms                                                     | 6.00 ms: 1.04x slower                                                                |
| sympy_expand               | 285 ms                                                      | 298 ms: 1.04x slower                                                                 |
| 2to3                       | 217 ms                                                      | 227 ms: 1.04x slower                                                                 |
| meteor_contest             | 72.3 ms                                                     | 75.6 ms: 1.05x slower                                                                |
| sqlglot_optimize           | 33.1 ms                                                     | 34.6 ms: 1.05x slower                                                                |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                                 |
| sympy_str                  | 166 ms                                                      | 174 ms: 1.05x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 547 ms: 1.05x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 13.0 ms: 1.06x slower                                                                |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                                                |
| sqlglot_normalize          | 171 ms                                                      | 184 ms: 1.07x slower                                                                 |
| html5lib                   | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                               |
| typing_runtime_protocols   | 100 us                                                      | 108 us: 1.07x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                                |
| logging_simple             | 5.72 us                                                     | 6.20 us: 1.08x slower                                                                |
| logging_format             | 6.15 us                                                     | 6.68 us: 1.09x slower                                                                |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                                |
| xml_etree_generate         | 53.3 ms                                                     | 58.1 ms: 1.09x slower                                                                |
| create_gc_cycles           | 829 us                                                      | 903 us: 1.09x slower                                                                 |
| django_template            | 21.8 ms                                                     | 23.7 ms: 1.09x slower                                                                |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.79 sec: 1.09x slower                                                               |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                                 |
| genshi_xml                 | 32.8 ms                                                     | 36.3 ms: 1.11x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 40.6 ms: 1.11x slower                                                                |
| genshi_text                | 14.9 ms                                                     | 16.7 ms: 1.12x slower                                                                |
| regex_compile              | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                                |
| go                         | 84.6 ms                                                     | 95.5 ms: 1.13x slower                                                                |
| comprehensions             | 10.2 us                                                     | 11.6 us: 1.14x slower                                                                |
| nqueens                    | 55.5 ms                                                     | 63.2 ms: 1.14x slower                                                                |
| pickle_pure_python         | 183 us                                                      | 209 us: 1.14x slower                                                                 |
| pprint_safe_repr           | 493 ms                                                      | 563 ms: 1.14x slower                                                                 |
| pyflate                    | 275 ms                                                      | 316 ms: 1.15x slower                                                                 |
| raytrace                   | 156 ms                                                      | 179 ms: 1.15x slower                                                                 |
| tomli_loads                | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.15x slower                                                                |
| pprint_pformat             | 991 ms                                                      | 1.15 sec: 1.16x slower                                                               |
| float                      | 48.1 ms                                                     | 56.3 ms: 1.17x slower                                                                |
| crypto_pyaes               | 42.8 ms                                                     | 50.2 ms: 1.17x slower                                                                |
| sqlglot_parse              | 761 us                                                      | 893 us: 1.17x slower                                                                 |
| chaos                      | 37.9 ms                                                     | 44.5 ms: 1.17x slower                                                                |
| deltablue                  | 1.86 ms                                                     | 2.21 ms: 1.19x slower                                                                |
| unpickle_pure_python       | 127 us                                                      | 150 us: 1.19x slower                                                                 |
| richards_super             | 29.3 ms                                                     | 35.1 ms: 1.20x slower                                                                |
| mako                       | 6.24 ms                                                     | 7.48 ms: 1.20x slower                                                                |
| richards                   | 26.0 ms                                                     | 31.4 ms: 1.21x slower                                                                |
| hexiom                     | 3.69 ms                                                     | 4.46 ms: 1.21x slower                                                                |
| scimark_lu                 | 54.0 ms                                                     | 65.9 ms: 1.22x slower                                                                |
| fannkuch                   | 245 ms                                                      | 300 ms: 1.23x slower                                                                 |
| logging_silent             | 51.0 ns                                                     | 62.6 ns: 1.23x slower                                                                |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.90 ms: 1.24x slower                                                                |
| spectral_norm              | 59.2 ms                                                     | 73.5 ms: 1.24x slower                                                                |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.1 ms: 1.24x slower                                                                |
| scimark_fft                | 174 ms                                                      | 219 ms: 1.26x slower                                                                 |
| scimark_sor                | 72.0 ms                                                     | 90.9 ms: 1.26x slower                                                                |
| nbody                      | 64.5 ms                                                     | 83.8 ms: 1.30x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, python_startup_no_site, gc_traversal, pycparser, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown