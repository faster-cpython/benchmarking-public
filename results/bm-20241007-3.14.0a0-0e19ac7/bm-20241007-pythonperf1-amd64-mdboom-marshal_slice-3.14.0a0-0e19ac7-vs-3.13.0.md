# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: windows-amd64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 226 ms: 1.04x slower                                                |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                              |
| html5lib       | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 532 ms: 1.23x faster                                                |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                |
| async_tree_memoization     | 271 ms                                                      | 262 ms: 1.04x faster                                                |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                |
| async_tree_io_tg           | 512 ms                                                      | 566 ms: 1.10x slower                                                |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                               |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                        |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.01x slower                                                |
| float          | 48.1 ms                                                     | 56.0 ms: 1.16x slower                                               |
| nbody          | 64.5 ms                                                     | 81.0 ms: 1.26x slower                                               |
| Geometric mean | (ref)                                                       | 1.14x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                               |
| regex_compile  | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                       | 1.02x slower                                                        |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.12 us: 1.03x faster                                               |
| json_loads           | 14.3 us                                                     | 14.1 us: 1.02x faster                                               |
| unpickle_list        | 2.72 us                                                     | 2.74 us: 1.01x slower                                               |
| pickle_dict          | 18.0 us                                                     | 18.4 us: 1.02x slower                                               |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.4 ms: 1.03x slower                                               |
| unpickle             | 8.63 us                                                     | 9.30 us: 1.08x slower                                               |
| xml_etree_generate   | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                               |
| json_dumps           | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                               |
| xml_etree_process    | 36.5 ms                                                     | 40.7 ms: 1.11x slower                                               |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                              |
| pickle_pure_python   | 183 us                                                      | 215 us: 1.17x slower                                                |
| unpickle_pure_python | 127 us                                                      | 150 us: 1.18x slower                                                |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                        |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.6 ms: 1.09x slower                                               |
| mako            | 6.24 ms                                                     | 6.93 ms: 1.11x slower                                               |
| genshi_text     | 14.9 ms                                                     | 16.8 ms: 1.13x slower                                               |
| django_template | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                               |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 513 us: 16.91x faster                                               |
| asyncio_tcp                | 654 ms                                                      | 532 ms: 1.23x faster                                                |
| deepcopy                   | 223 us                                                      | 185 us: 1.20x faster                                                |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                |
| deepcopy_memo              | 21.8 us                                                     | 20.1 us: 1.08x faster                                               |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                |
| pycparser                  | 758 ms                                                      | 720 ms: 1.05x faster                                                |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                               |
| unpack_sequence            | 40.0 ns                                                     | 38.5 ns: 1.04x faster                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                               |
| async_tree_memoization     | 271 ms                                                      | 262 ms: 1.04x faster                                                |
| pickle                     | 7.34 us                                                     | 7.12 us: 1.03x faster                                               |
| pathlib                    | 81.2 ms                                                     | 78.8 ms: 1.03x faster                                               |
| json_loads                 | 14.3 us                                                     | 14.1 us: 1.02x faster                                               |
| bench_mp_pool              | 69.6 ms                                                     | 68.9 ms: 1.01x faster                                               |
| unpickle_list              | 2.72 us                                                     | 2.74 us: 1.01x slower                                               |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                               |
| pidigits                   | 148 ms                                                      | 151 ms: 1.01x slower                                                |
| pickle_dict                | 18.0 us                                                     | 18.4 us: 1.02x slower                                               |
| mdp                        | 1.38 sec                                                    | 1.41 sec: 1.02x slower                                              |
| sqlite_synth               | 1.60 us                                                     | 1.63 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                |
| go                         | 84.6 ms                                                     | 87.1 ms: 1.03x slower                                               |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.4 ms: 1.03x slower                                               |
| html5lib                   | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                               |
| sympy_sum                  | 86.4 ms                                                     | 90.0 ms: 1.04x slower                                               |
| 2to3                       | 217 ms                                                      | 226 ms: 1.04x slower                                                |
| coverage                   | 46.7 ms                                                     | 49.2 ms: 1.05x slower                                               |
| meteor_contest             | 72.3 ms                                                     | 76.3 ms: 1.06x slower                                               |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.08x slower                                               |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                              |
| unpickle                   | 8.63 us                                                     | 9.30 us: 1.08x slower                                               |
| sympy_expand               | 285 ms                                                      | 307 ms: 1.08x slower                                                |
| dulwich_log                | 40.4 ms                                                     | 43.8 ms: 1.09x slower                                               |
| genshi_xml                 | 32.8 ms                                                     | 35.6 ms: 1.09x slower                                               |
| xml_etree_generate         | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                               |
| json_dumps                 | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                               |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                               |
| typing_runtime_protocols   | 100 us                                                      | 110 us: 1.10x slower                                                |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                               |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                |
| pprint_safe_repr           | 493 ms                                                      | 542 ms: 1.10x slower                                                |
| async_tree_io_tg           | 512 ms                                                      | 566 ms: 1.10x slower                                                |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                |
| logging_simple             | 5.72 us                                                     | 6.33 us: 1.11x slower                                               |
| create_gc_cycles           | 829 us                                                      | 917 us: 1.11x slower                                                |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                               |
| logging_format             | 6.15 us                                                     | 6.82 us: 1.11x slower                                               |
| mako                       | 6.24 ms                                                     | 6.93 ms: 1.11x slower                                               |
| xml_etree_process          | 36.5 ms                                                     | 40.7 ms: 1.11x slower                                               |
| pprint_pformat             | 991 ms                                                      | 1.11 sec: 1.12x slower                                              |
| sqlglot_normalize          | 171 ms                                                      | 192 ms: 1.12x slower                                                |
| regex_compile              | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                               |
| genshi_text                | 14.9 ms                                                     | 16.8 ms: 1.13x slower                                               |
| django_template            | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                               |
| chaos                      | 37.9 ms                                                     | 43.5 ms: 1.15x slower                                               |
| comprehensions             | 10.2 us                                                     | 11.8 us: 1.15x slower                                               |
| crypto_pyaes               | 42.8 ms                                                     | 49.3 ms: 1.15x slower                                               |
| sqlglot_parse              | 761 us                                                      | 880 us: 1.16x slower                                                |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.16x slower                                               |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                              |
| pyflate                    | 275 ms                                                      | 319 ms: 1.16x slower                                                |
| spectral_norm              | 59.2 ms                                                     | 68.8 ms: 1.16x slower                                               |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.72 ms: 1.16x slower                                               |
| float                      | 48.1 ms                                                     | 56.0 ms: 1.16x slower                                               |
| nqueens                    | 55.5 ms                                                     | 64.6 ms: 1.16x slower                                               |
| pickle_pure_python         | 183 us                                                      | 215 us: 1.17x slower                                                |
| fannkuch                   | 245 ms                                                      | 288 ms: 1.18x slower                                                |
| scimark_fft                | 174 ms                                                      | 205 ms: 1.18x slower                                                |
| unpickle_pure_python       | 127 us                                                      | 150 us: 1.18x slower                                                |
| hexiom                     | 3.69 ms                                                     | 4.37 ms: 1.18x slower                                               |
| scimark_monte_carlo        | 40.3 ms                                                     | 48.4 ms: 1.20x slower                                               |
| scimark_lu                 | 54.0 ms                                                     | 65.8 ms: 1.22x slower                                               |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.22x slower                                               |
| richards_super             | 29.3 ms                                                     | 36.2 ms: 1.24x slower                                               |
| richards                   | 26.0 ms                                                     | 32.2 ms: 1.24x slower                                               |
| logging_silent             | 51.0 ns                                                     | 63.1 ns: 1.24x slower                                               |
| scimark_sor                | 72.0 ms                                                     | 90.4 ms: 1.26x slower                                               |
| nbody                      | 64.5 ms                                                     | 81.0 ms: 1.26x slower                                               |
| raytrace                   | 156 ms                                                      | 198 ms: 1.27x slower                                                |
| json                       | 2.98 ms                                                     | 4.27 ms: 1.43x slower                                               |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                        |

Benchmark hidden because not significant (13): asyncio_tcp_ssl, async_tree_none_tg, bench_thread_pool, python_startup, telco, regex_v8, regex_dna, python_startup_no_site, tornado_http, pickle_list, async_tree_cpu_io_mixed, xml_etree_parse, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown