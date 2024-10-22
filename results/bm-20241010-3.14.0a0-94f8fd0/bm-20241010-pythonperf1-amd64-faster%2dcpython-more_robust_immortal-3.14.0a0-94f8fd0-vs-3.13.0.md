# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: windows-amd64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 227 ms: 1.05x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                               |
| html5lib       | 38.6 ms                                                     | 42.2 ms: 1.09x slower                                                                |
| tornado_http   | 92.8 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                                 |
| async_tree_none            | 223 ms                                                      | 212 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 398 ms: 1.03x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 393 ms: 1.05x slower                                                                 |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.73 sec: 1.06x slower                                                               |
| asyncio_tcp                | 654 ms                                                      | 695 ms: 1.06x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 593 ms: 1.14x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 587 ms: 1.15x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                                 |
| float          | 48.1 ms                                                     | 54.8 ms: 1.14x slower                                                                |
| nbody          | 64.5 ms                                                     | 80.7 ms: 1.25x slower                                                                |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                                |
| regex_v8       | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                                |
| regex_compile  | 80.1 ms                                                     | 90.1 ms: 1.12x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 93.9 ms: 1.01x slower                                                                |
| pickle               | 7.34 us                                                     | 7.45 us: 1.01x slower                                                                |
| json_loads           | 14.3 us                                                     | 14.9 us: 1.04x slower                                                                |
| unpickle_list        | 2.72 us                                                     | 2.89 us: 1.06x slower                                                                |
| pickle_dict          | 18.0 us                                                     | 19.2 us: 1.06x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.9 ms: 1.07x slower                                                                |
| unpickle             | 8.63 us                                                     | 9.35 us: 1.08x slower                                                                |
| json_dumps           | 5.76 ms                                                     | 6.34 ms: 1.10x slower                                                                |
| xml_etree_generate   | 53.3 ms                                                     | 58.7 ms: 1.10x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 41.1 ms: 1.13x slower                                                                |
| unpickle_pure_python | 127 us                                                      | 149 us: 1.17x slower                                                                 |
| pickle_pure_python   | 183 us                                                      | 215 us: 1.18x slower                                                                 |
| tomli_loads          | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                                                |
| genshi_xml      | 32.8 ms                                                     | 38.2 ms: 1.16x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                                |
| django_template | 21.8 ms                                                     | 26.7 ms: 1.23x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.17x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 522 us: 16.63x faster                                                                |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                                 |
| deepcopy_memo              | 21.8 us                                                     | 19.9 us: 1.10x faster                                                                |
| async_tree_none            | 223 ms                                                      | 212 ms: 1.05x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.97 us: 1.03x faster                                                                |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.02x faster                                                                |
| pathlib                    | 81.2 ms                                                     | 80.3 ms: 1.01x faster                                                                |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                                 |
| xml_etree_parse            | 93.2 ms                                                     | 93.9 ms: 1.01x slower                                                                |
| pickle                     | 7.34 us                                                     | 7.45 us: 1.01x slower                                                                |
| telco                      | 4.85 ms                                                     | 4.93 ms: 1.02x slower                                                                |
| regex_v8                   | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                                |
| tornado_http               | 92.8 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 398 ms: 1.03x slower                                                                 |
| go                         | 84.6 ms                                                     | 87.4 ms: 1.03x slower                                                                |
| sqlite_synth               | 1.60 us                                                     | 1.65 us: 1.03x slower                                                                |
| json_loads                 | 14.3 us                                                     | 14.9 us: 1.04x slower                                                                |
| sympy_sum                  | 86.4 ms                                                     | 90.2 ms: 1.04x slower                                                                |
| 2to3                       | 217 ms                                                      | 227 ms: 1.05x slower                                                                 |
| coverage                   | 46.7 ms                                                     | 48.9 ms: 1.05x slower                                                                |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 393 ms: 1.05x slower                                                                 |
| meteor_contest             | 72.3 ms                                                     | 76.4 ms: 1.06x slower                                                                |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.73 sec: 1.06x slower                                                               |
| unpickle_list              | 2.72 us                                                     | 2.89 us: 1.06x slower                                                                |
| pickle_dict                | 18.0 us                                                     | 19.2 us: 1.06x slower                                                                |
| scimark_lu                 | 54.0 ms                                                     | 57.4 ms: 1.06x slower                                                                |
| asyncio_tcp                | 654 ms                                                      | 695 ms: 1.06x slower                                                                 |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.9 ms: 1.07x slower                                                                |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.08x slower                                                                 |
| sympy_expand               | 285 ms                                                      | 308 ms: 1.08x slower                                                                 |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                                 |
| unpickle                   | 8.63 us                                                     | 9.35 us: 1.08x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                               |
| html5lib                   | 38.6 ms                                                     | 42.2 ms: 1.09x slower                                                                |
| dulwich_log                | 40.4 ms                                                     | 44.2 ms: 1.09x slower                                                                |
| mako                       | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                                                |
| json_dumps                 | 5.76 ms                                                     | 6.34 ms: 1.10x slower                                                                |
| xml_etree_generate         | 53.3 ms                                                     | 58.7 ms: 1.10x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 493 ms                                                      | 552 ms: 1.12x slower                                                                 |
| logging_format             | 6.15 us                                                     | 6.91 us: 1.12x slower                                                                |
| regex_compile              | 80.1 ms                                                     | 90.1 ms: 1.12x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 41.1 ms: 1.13x slower                                                                |
| crypto_pyaes               | 42.8 ms                                                     | 48.3 ms: 1.13x slower                                                                |
| logging_simple             | 5.72 us                                                     | 6.45 us: 1.13x slower                                                                |
| create_gc_cycles           | 829 us                                                      | 934 us: 1.13x slower                                                                 |
| typing_runtime_protocols   | 100 us                                                      | 113 us: 1.13x slower                                                                 |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| sqlglot_optimize           | 33.1 ms                                                     | 37.6 ms: 1.14x slower                                                                |
| async_tree_io              | 521 ms                                                      | 593 ms: 1.14x slower                                                                 |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.66 ms: 1.14x slower                                                                |
| pprint_pformat             | 991 ms                                                      | 1.13 sec: 1.14x slower                                                               |
| mdp                        | 1.38 sec                                                    | 1.58 sec: 1.14x slower                                                               |
| fannkuch                   | 245 ms                                                      | 279 ms: 1.14x slower                                                                 |
| float                      | 48.1 ms                                                     | 54.8 ms: 1.14x slower                                                                |
| async_tree_io_tg           | 512 ms                                                      | 587 ms: 1.15x slower                                                                 |
| comprehensions             | 10.2 us                                                     | 11.8 us: 1.15x slower                                                                |
| nqueens                    | 55.5 ms                                                     | 64.1 ms: 1.15x slower                                                                |
| chaos                      | 37.9 ms                                                     | 43.8 ms: 1.16x slower                                                                |
| pyflate                    | 275 ms                                                      | 319 ms: 1.16x slower                                                                 |
| scimark_fft                | 174 ms                                                      | 202 ms: 1.16x slower                                                                 |
| genshi_xml                 | 32.8 ms                                                     | 38.2 ms: 1.16x slower                                                                |
| scimark_monte_carlo        | 40.3 ms                                                     | 46.9 ms: 1.17x slower                                                                |
| sqlglot_normalize          | 171 ms                                                      | 200 ms: 1.17x slower                                                                 |
| hexiom                     | 3.69 ms                                                     | 4.32 ms: 1.17x slower                                                                |
| spectral_norm              | 59.2 ms                                                     | 69.3 ms: 1.17x slower                                                                |
| unpickle_pure_python       | 127 us                                                      | 149 us: 1.17x slower                                                                 |
| pickle_pure_python         | 183 us                                                      | 215 us: 1.18x slower                                                                 |
| logging_silent             | 51.0 ns                                                     | 60.1 ns: 1.18x slower                                                                |
| tomli_loads                | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| genshi_text                | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                                |
| sqlglot_parse              | 761 us                                                      | 912 us: 1.20x slower                                                                 |
| sqlglot_transpile          | 952 us                                                      | 1.14 ms: 1.20x slower                                                                |
| scimark_sor                | 72.0 ms                                                     | 88.0 ms: 1.22x slower                                                                |
| deltablue                  | 1.86 ms                                                     | 2.29 ms: 1.23x slower                                                                |
| django_template            | 21.8 ms                                                     | 26.7 ms: 1.23x slower                                                                |
| raytrace                   | 156 ms                                                      | 192 ms: 1.23x slower                                                                 |
| richards                   | 26.0 ms                                                     | 32.5 ms: 1.25x slower                                                                |
| richards_super             | 29.3 ms                                                     | 36.6 ms: 1.25x slower                                                                |
| nbody                      | 64.5 ms                                                     | 80.7 ms: 1.25x slower                                                                |
| json                       | 2.98 ms                                                     | 4.15 ms: 1.39x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (10): python_startup, pycparser, bench_mp_pool, regex_dna, python_startup_no_site, unpack_sequence, async_tree_memoization, async_tree_none_tg, bench_thread_pool, pickle_list
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown