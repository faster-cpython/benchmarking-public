# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 226 ms: 1.04x slower                                              |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                            |
| html5lib       | 38.6 ms                                                     | 40.9 ms: 1.06x slower                                             |
| tornado_http   | 92.8 ms                                                     | 84.2 ms: 1.10x faster                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 469 ms: 1.39x faster                                              |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                              |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.45 sec: 1.13x faster                                            |
| async_tree_none            | 223 ms                                                      | 209 ms: 1.07x faster                                              |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                              |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                              |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 398 ms: 1.06x slower                                              |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                              |
| async_tree_io_tg           | 512 ms                                                      | 562 ms: 1.10x slower                                              |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                              |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                             |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                      |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| float          | 48.1 ms                                                     | 55.3 ms: 1.15x slower                                             |
| nbody          | 64.5 ms                                                     | 83.8 ms: 1.30x slower                                             |
| Geometric mean | (ref)                                                       | 1.15x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                             |
| regex_v8       | 14.7 ms                                                     | 15.3 ms: 1.04x slower                                             |
| regex_dna      | 114 ms                                                      | 121 ms: 1.06x slower                                              |
| regex_compile  | 80.1 ms                                                     | 93.1 ms: 1.16x slower                                             |
| Geometric mean | (ref)                                                       | 1.06x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_list          | 2.89 us                                                     | 2.73 us: 1.06x faster                                             |
| pickle               | 7.34 us                                                     | 7.10 us: 1.03x faster                                             |
| pickle_dict          | 18.0 us                                                     | 17.6 us: 1.02x faster                                             |
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                             |
| xml_etree_parse      | 93.2 ms                                                     | 94.3 ms: 1.01x slower                                             |
| unpickle_list        | 2.72 us                                                     | 2.78 us: 1.02x slower                                             |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.2 ms: 1.05x slower                                             |
| unpickle             | 8.63 us                                                     | 9.12 us: 1.06x slower                                             |
| json_dumps           | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                             |
| xml_etree_generate   | 53.3 ms                                                     | 58.6 ms: 1.10x slower                                             |
| xml_etree_process    | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                             |
| pickle_pure_python   | 183 us                                                      | 215 us: 1.17x slower                                              |
| tomli_loads          | 1.36 sec                                                    | 1.61 sec: 1.18x slower                                            |
| unpickle_pure_python | 127 us                                                      | 153 us: 1.21x slower                                              |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                       | 1.00x faster                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.6 ms: 1.09x slower                                             |
| mako            | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                             |
| genshi_text     | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                             |
| django_template | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                             |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 512 us: 16.94x faster                                             |
| asyncio_tcp                | 654 ms                                                      | 469 ms: 1.39x faster                                              |
| deepcopy                   | 223 us                                                      | 191 us: 1.17x faster                                              |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                              |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.45 sec: 1.13x faster                                            |
| tornado_http               | 92.8 ms                                                     | 84.2 ms: 1.10x faster                                             |
| pathlib                    | 81.2 ms                                                     | 75.7 ms: 1.07x faster                                             |
| async_tree_none            | 223 ms                                                      | 209 ms: 1.07x faster                                              |
| pickle_list                | 2.89 us                                                     | 2.73 us: 1.06x faster                                             |
| deepcopy_memo              | 21.8 us                                                     | 20.6 us: 1.06x faster                                             |
| bench_mp_pool              | 69.6 ms                                                     | 66.6 ms: 1.05x faster                                             |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                             |
| pickle                     | 7.34 us                                                     | 7.10 us: 1.03x faster                                             |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                              |
| bench_thread_pool          | 828 us                                                      | 805 us: 1.03x faster                                              |
| pickle_dict                | 18.0 us                                                     | 17.6 us: 1.02x faster                                             |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.02x faster                                             |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                             |
| python_startup             | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                             |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                             |
| xml_etree_parse            | 93.2 ms                                                     | 94.3 ms: 1.01x slower                                             |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| unpickle_list              | 2.72 us                                                     | 2.78 us: 1.02x slower                                             |
| sqlite_synth               | 1.60 us                                                     | 1.64 us: 1.03x slower                                             |
| json                       | 2.98 ms                                                     | 3.09 ms: 1.04x slower                                             |
| coverage                   | 46.7 ms                                                     | 48.5 ms: 1.04x slower                                             |
| 2to3                       | 217 ms                                                      | 226 ms: 1.04x slower                                              |
| regex_v8                   | 14.7 ms                                                     | 15.3 ms: 1.04x slower                                             |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.2 ms: 1.05x slower                                             |
| sympy_sum                  | 86.4 ms                                                     | 90.6 ms: 1.05x slower                                             |
| go                         | 84.6 ms                                                     | 88.9 ms: 1.05x slower                                             |
| unpickle                   | 8.63 us                                                     | 9.12 us: 1.06x slower                                             |
| html5lib                   | 38.6 ms                                                     | 40.9 ms: 1.06x slower                                             |
| regex_dna                  | 114 ms                                                      | 121 ms: 1.06x slower                                              |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 398 ms: 1.06x slower                                              |
| create_gc_cycles           | 829 us                                                      | 882 us: 1.06x slower                                              |
| unpack_sequence            | 40.0 ns                                                     | 42.7 ns: 1.07x slower                                             |
| sympy_expand               | 285 ms                                                      | 305 ms: 1.07x slower                                              |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                              |
| telco                      | 4.85 ms                                                     | 5.20 ms: 1.07x slower                                             |
| dulwich_log                | 40.4 ms                                                     | 43.4 ms: 1.08x slower                                             |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.08x slower                                             |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                            |
| json_dumps                 | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                             |
| genshi_xml                 | 32.8 ms                                                     | 35.6 ms: 1.09x slower                                             |
| mdp                        | 1.38 sec                                                    | 1.51 sec: 1.09x slower                                            |
| meteor_contest             | 72.3 ms                                                     | 78.9 ms: 1.09x slower                                             |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                              |
| generators                 | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                             |
| async_tree_io_tg           | 512 ms                                                      | 562 ms: 1.10x slower                                              |
| mako                       | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                             |
| xml_etree_generate         | 53.3 ms                                                     | 58.6 ms: 1.10x slower                                             |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                              |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                             |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                              |
| sqlglot_optimize           | 33.1 ms                                                     | 36.8 ms: 1.11x slower                                             |
| crypto_pyaes               | 42.8 ms                                                     | 47.9 ms: 1.12x slower                                             |
| pprint_safe_repr           | 493 ms                                                      | 551 ms: 1.12x slower                                              |
| xml_etree_process          | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                             |
| genshi_text                | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                             |
| pprint_pformat             | 991 ms                                                      | 1.13 sec: 1.14x slower                                            |
| float                      | 48.1 ms                                                     | 55.3 ms: 1.15x slower                                             |
| logging_format             | 6.15 us                                                     | 7.08 us: 1.15x slower                                             |
| sqlglot_normalize          | 171 ms                                                      | 197 ms: 1.15x slower                                              |
| regex_compile              | 80.1 ms                                                     | 93.1 ms: 1.16x slower                                             |
| logging_simple             | 5.72 us                                                     | 6.68 us: 1.17x slower                                             |
| comprehensions             | 10.2 us                                                     | 12.0 us: 1.17x slower                                             |
| pickle_pure_python         | 183 us                                                      | 215 us: 1.17x slower                                              |
| pyflate                    | 275 ms                                                      | 324 ms: 1.18x slower                                              |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.18x slower                                             |
| spectral_norm              | 59.2 ms                                                     | 69.9 ms: 1.18x slower                                             |
| tomli_loads                | 1.36 sec                                                    | 1.61 sec: 1.18x slower                                            |
| chaos                      | 37.9 ms                                                     | 44.9 ms: 1.18x slower                                             |
| sqlglot_parse              | 761 us                                                      | 902 us: 1.19x slower                                              |
| nqueens                    | 55.5 ms                                                     | 65.9 ms: 1.19x slower                                             |
| django_template            | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                             |
| unpickle_pure_python       | 127 us                                                      | 153 us: 1.21x slower                                              |
| scimark_lu                 | 54.0 ms                                                     | 65.7 ms: 1.22x slower                                             |
| scimark_fft                | 174 ms                                                      | 212 ms: 1.22x slower                                              |
| logging_silent             | 51.0 ns                                                     | 63.5 ns: 1.25x slower                                             |
| deltablue                  | 1.86 ms                                                     | 2.32 ms: 1.25x slower                                             |
| hexiom                     | 3.69 ms                                                     | 4.62 ms: 1.25x slower                                             |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.93 ms: 1.25x slower                                             |
| richards_super             | 29.3 ms                                                     | 36.9 ms: 1.26x slower                                             |
| fannkuch                   | 245 ms                                                      | 308 ms: 1.26x slower                                              |
| scimark_sor                | 72.0 ms                                                     | 90.7 ms: 1.26x slower                                             |
| raytrace                   | 156 ms                                                      | 197 ms: 1.26x slower                                              |
| richards                   | 26.0 ms                                                     | 33.0 ms: 1.27x slower                                             |
| scimark_monte_carlo        | 40.3 ms                                                     | 51.4 ms: 1.28x slower                                             |
| nbody                      | 64.5 ms                                                     | 83.8 ms: 1.30x slower                                             |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                      |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, python_startup_no_site, pycparser, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown