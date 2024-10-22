# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-amd64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 222 ms: 1.02x slower                                                   |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                 |
| html5lib       | 38.6 ms                                                     | 40.3 ms: 1.04x slower                                                  |
| tornado_http   | 92.8 ms                                                     | 84.1 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                       | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 472 ms: 1.38x faster                                                   |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                   |
| async_tree_none            | 223 ms                                                      | 205 ms: 1.09x faster                                                   |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.52 sec: 1.08x faster                                                 |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.06x slower                                                   |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                   |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                   |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                           |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.01x slower                                                   |
| float          | 48.1 ms                                                     | 56.6 ms: 1.18x slower                                                  |
| nbody          | 64.5 ms                                                     | 81.8 ms: 1.27x slower                                                  |
| Geometric mean | (ref)                                                       | 1.15x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                  |
| regex_v8       | 14.7 ms                                                     | 15.1 ms: 1.03x slower                                                  |
| regex_dna      | 114 ms                                                      | 121 ms: 1.06x slower                                                   |
| regex_compile  | 80.1 ms                                                     | 91.5 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                       | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.17 us: 1.02x faster                                                  |
| json_loads           | 14.3 us                                                     | 14.6 us: 1.02x slower                                                  |
| pickle_dict          | 18.0 us                                                     | 18.7 us: 1.04x slower                                                  |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.1 ms: 1.04x slower                                                  |
| unpickle             | 8.63 us                                                     | 9.28 us: 1.07x slower                                                  |
| json_dumps           | 5.76 ms                                                     | 6.23 ms: 1.08x slower                                                  |
| xml_etree_generate   | 53.3 ms                                                     | 58.6 ms: 1.10x slower                                                  |
| xml_etree_process    | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                  |
| pickle_pure_python   | 183 us                                                      | 212 us: 1.16x slower                                                   |
| tomli_loads          | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                 |
| unpickle_pure_python | 127 us                                                      | 153 us: 1.20x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                           |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.4 ms: 1.04x faster                                                  |
| python_startup_no_site | 17.8 ms                                                     | 17.5 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.89 ms: 1.10x slower                                                  |
| genshi_xml      | 32.8 ms                                                     | 37.4 ms: 1.14x slower                                                  |
| django_template | 21.8 ms                                                     | 24.9 ms: 1.14x slower                                                  |
| genshi_text     | 14.9 ms                                                     | 17.3 ms: 1.16x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 544 us: 15.94x faster                                                  |
| asyncio_tcp                | 654 ms                                                      | 472 ms: 1.38x faster                                                   |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                   |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                   |
| pathlib                    | 81.2 ms                                                     | 73.5 ms: 1.10x faster                                                  |
| tornado_http               | 92.8 ms                                                     | 84.1 ms: 1.10x faster                                                  |
| async_tree_none            | 223 ms                                                      | 205 ms: 1.09x faster                                                   |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.52 sec: 1.08x faster                                                 |
| deepcopy_memo              | 21.8 us                                                     | 20.6 us: 1.06x faster                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                  |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                   |
| bench_mp_pool              | 69.6 ms                                                     | 66.6 ms: 1.05x faster                                                  |
| python_startup             | 22.2 ms                                                     | 21.4 ms: 1.04x faster                                                  |
| bench_thread_pool          | 828 us                                                      | 805 us: 1.03x faster                                                   |
| pickle                     | 7.34 us                                                     | 7.17 us: 1.02x faster                                                  |
| gc_traversal               | 1.55 ms                                                     | 1.52 ms: 1.02x faster                                                  |
| python_startup_no_site     | 17.8 ms                                                     | 17.5 ms: 1.02x faster                                                  |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                  |
| coverage                   | 46.7 ms                                                     | 46.9 ms: 1.00x slower                                                  |
| pidigits                   | 148 ms                                                      | 151 ms: 1.01x slower                                                   |
| sqlite_synth               | 1.60 us                                                     | 1.62 us: 1.02x slower                                                  |
| json_loads                 | 14.3 us                                                     | 14.6 us: 1.02x slower                                                  |
| 2to3                       | 217 ms                                                      | 222 ms: 1.02x slower                                                   |
| regex_v8                   | 14.7 ms                                                     | 15.1 ms: 1.03x slower                                                  |
| go                         | 84.6 ms                                                     | 87.3 ms: 1.03x slower                                                  |
| unpack_sequence            | 40.0 ns                                                     | 41.3 ns: 1.03x slower                                                  |
| pickle_dict                | 18.0 us                                                     | 18.7 us: 1.04x slower                                                  |
| html5lib                   | 38.6 ms                                                     | 40.3 ms: 1.04x slower                                                  |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.1 ms: 1.04x slower                                                  |
| sympy_sum                  | 86.4 ms                                                     | 91.2 ms: 1.05x slower                                                  |
| dulwich_log                | 40.4 ms                                                     | 42.6 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.06x slower                                                   |
| json                       | 2.98 ms                                                     | 3.15 ms: 1.06x slower                                                  |
| create_gc_cycles           | 829 us                                                      | 878 us: 1.06x slower                                                   |
| regex_dna                  | 114 ms                                                      | 121 ms: 1.06x slower                                                   |
| telco                      | 4.85 ms                                                     | 5.16 ms: 1.06x slower                                                  |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                   |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                   |
| unpickle                   | 8.63 us                                                     | 9.28 us: 1.07x slower                                                  |
| meteor_contest             | 72.3 ms                                                     | 77.9 ms: 1.08x slower                                                  |
| sympy_expand               | 285 ms                                                      | 307 ms: 1.08x slower                                                   |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.08x slower                                                  |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                 |
| generators                 | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                  |
| json_dumps                 | 5.76 ms                                                     | 6.23 ms: 1.08x slower                                                  |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.08x slower                                                 |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                   |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                   |
| xml_etree_generate         | 53.3 ms                                                     | 58.6 ms: 1.10x slower                                                  |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                   |
| mako                       | 6.24 ms                                                     | 6.89 ms: 1.10x slower                                                  |
| sqlglot_optimize           | 33.1 ms                                                     | 36.5 ms: 1.10x slower                                                  |
| pprint_safe_repr           | 493 ms                                                      | 546 ms: 1.11x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                  |
| logging_simple             | 5.72 us                                                     | 6.39 us: 1.12x slower                                                  |
| xml_etree_process          | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                  |
| pprint_pformat             | 991 ms                                                      | 1.11 sec: 1.12x slower                                                 |
| logging_format             | 6.15 us                                                     | 6.88 us: 1.12x slower                                                  |
| crypto_pyaes               | 42.8 ms                                                     | 48.1 ms: 1.12x slower                                                  |
| sqlglot_normalize          | 171 ms                                                      | 193 ms: 1.12x slower                                                   |
| comprehensions             | 10.2 us                                                     | 11.7 us: 1.14x slower                                                  |
| genshi_xml                 | 32.8 ms                                                     | 37.4 ms: 1.14x slower                                                  |
| regex_compile              | 80.1 ms                                                     | 91.5 ms: 1.14x slower                                                  |
| django_template            | 21.8 ms                                                     | 24.9 ms: 1.14x slower                                                  |
| nqueens                    | 55.5 ms                                                     | 63.7 ms: 1.15x slower                                                  |
| chaos                      | 37.9 ms                                                     | 43.7 ms: 1.15x slower                                                  |
| pyflate                    | 275 ms                                                      | 319 ms: 1.16x slower                                                   |
| pickle_pure_python         | 183 us                                                      | 212 us: 1.16x slower                                                   |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.72 ms: 1.16x slower                                                  |
| genshi_text                | 14.9 ms                                                     | 17.3 ms: 1.16x slower                                                  |
| scimark_fft                | 174 ms                                                      | 203 ms: 1.16x slower                                                   |
| spectral_norm              | 59.2 ms                                                     | 69.0 ms: 1.17x slower                                                  |
| tomli_loads                | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                 |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.18x slower                                                  |
| scimark_lu                 | 54.0 ms                                                     | 63.6 ms: 1.18x slower                                                  |
| float                      | 48.1 ms                                                     | 56.6 ms: 1.18x slower                                                  |
| sqlglot_parse              | 761 us                                                      | 900 us: 1.18x slower                                                   |
| hexiom                     | 3.69 ms                                                     | 4.39 ms: 1.19x slower                                                  |
| fannkuch                   | 245 ms                                                      | 292 ms: 1.19x slower                                                   |
| raytrace                   | 156 ms                                                      | 188 ms: 1.20x slower                                                   |
| unpickle_pure_python       | 127 us                                                      | 153 us: 1.20x slower                                                   |
| deltablue                  | 1.86 ms                                                     | 2.26 ms: 1.21x slower                                                  |
| logging_silent             | 51.0 ns                                                     | 62.6 ns: 1.23x slower                                                  |
| scimark_sor                | 72.0 ms                                                     | 88.8 ms: 1.23x slower                                                  |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.9 ms: 1.24x slower                                                  |
| richards_super             | 29.3 ms                                                     | 36.4 ms: 1.24x slower                                                  |
| richards                   | 26.0 ms                                                     | 32.4 ms: 1.24x slower                                                  |
| nbody                      | 64.5 ms                                                     | 81.8 ms: 1.27x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                           |

Benchmark hidden because not significant (7): async_tree_none_tg, unpickle_list, xml_etree_parse, async_tree_cpu_io_mixed, pickle_list, pycparser, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown