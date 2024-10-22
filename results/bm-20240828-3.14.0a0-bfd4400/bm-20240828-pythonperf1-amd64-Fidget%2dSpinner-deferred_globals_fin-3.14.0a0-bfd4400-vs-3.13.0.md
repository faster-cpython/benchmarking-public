# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-amd64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 231 ms: 1.06x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.74 sec: 1.10x slower                                                               |
| html5lib       | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 540 ms: 1.21x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 392 ms: 1.05x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 546 ms: 1.07x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                                 |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                                                 |
| float          | 48.1 ms                                                     | 56.8 ms: 1.18x slower                                                                |
| nbody          | 64.5 ms                                                     | 83.5 ms: 1.30x slower                                                                |
| Geometric mean | (ref)                                                       | 1.16x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                                |
| regex_compile  | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.0 us: 1.02x faster                                                                |
| xml_etree_parse      | 93.2 ms                                                     | 95.9 ms: 1.03x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.8 ms: 1.06x slower                                                                |
| json_dumps           | 5.76 ms                                                     | 6.16 ms: 1.07x slower                                                                |
| xml_etree_generate   | 53.3 ms                                                     | 57.9 ms: 1.09x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 40.7 ms: 1.11x slower                                                                |
| unpickle_pure_python | 127 us                                                      | 146 us: 1.15x slower                                                                 |
| tomli_loads          | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| pickle_pure_python   | 183 us                                                      | 212 us: 1.16x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.8 ms: 1.09x slower                                                                |
| mako            | 6.24 ms                                                     | 6.97 ms: 1.12x slower                                                                |
| django_template | 21.8 ms                                                     | 24.6 ms: 1.13x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 17.0 ms: 1.14x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 526 us: 16.50x faster                                                                |
| asyncio_tcp                | 654 ms                                                      | 540 ms: 1.21x faster                                                                 |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                                 |
| deepcopy_memo              | 21.8 us                                                     | 20.0 us: 1.09x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                                |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.05x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                                |
| pathlib                    | 81.2 ms                                                     | 78.9 ms: 1.03x faster                                                                |
| bench_mp_pool              | 69.6 ms                                                     | 68.2 ms: 1.02x faster                                                                |
| json_loads                 | 14.3 us                                                     | 14.0 us: 1.02x faster                                                                |
| python_startup             | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                                |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                                |
| coverage                   | 46.7 ms                                                     | 47.4 ms: 1.02x slower                                                                |
| pidigits                   | 148 ms                                                      | 152 ms: 1.02x slower                                                                 |
| xml_etree_parse            | 93.2 ms                                                     | 95.9 ms: 1.03x slower                                                                |
| telco                      | 4.85 ms                                                     | 5.02 ms: 1.03x slower                                                                |
| json                       | 2.98 ms                                                     | 3.10 ms: 1.04x slower                                                                |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 392 ms: 1.05x slower                                                                 |
| sympy_sum                  | 86.4 ms                                                     | 91.2 ms: 1.05x slower                                                                |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.8 ms: 1.06x slower                                                                |
| 2to3                       | 217 ms                                                      | 231 ms: 1.06x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 546 ms: 1.07x slower                                                                 |
| generators                 | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                                |
| dulwich_log                | 40.4 ms                                                     | 43.2 ms: 1.07x slower                                                                |
| json_dumps                 | 5.76 ms                                                     | 6.16 ms: 1.07x slower                                                                |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                                 |
| html5lib                   | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                                |
| sympy_expand               | 285 ms                                                      | 308 ms: 1.08x slower                                                                 |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.08x slower                                                               |
| meteor_contest             | 72.3 ms                                                     | 78.5 ms: 1.09x slower                                                                |
| xml_etree_generate         | 53.3 ms                                                     | 57.9 ms: 1.09x slower                                                                |
| genshi_xml                 | 32.8 ms                                                     | 35.8 ms: 1.09x slower                                                                |
| create_gc_cycles           | 829 us                                                      | 910 us: 1.10x slower                                                                 |
| logging_format             | 6.15 us                                                     | 6.77 us: 1.10x slower                                                                |
| sqlglot_optimize           | 33.1 ms                                                     | 36.4 ms: 1.10x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.74 sec: 1.10x slower                                                               |
| logging_simple             | 5.72 us                                                     | 6.34 us: 1.11x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 40.7 ms: 1.11x slower                                                                |
| mako                       | 6.24 ms                                                     | 6.97 ms: 1.12x slower                                                                |
| crypto_pyaes               | 42.8 ms                                                     | 47.9 ms: 1.12x slower                                                                |
| pprint_safe_repr           | 493 ms                                                      | 551 ms: 1.12x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                                 |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                                 |
| sqlglot_normalize          | 171 ms                                                      | 192 ms: 1.12x slower                                                                 |
| regex_compile              | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                                |
| django_template            | 21.8 ms                                                     | 24.6 ms: 1.13x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                                |
| pprint_pformat             | 991 ms                                                      | 1.13 sec: 1.13x slower                                                               |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.66 ms: 1.14x slower                                                                |
| nqueens                    | 55.5 ms                                                     | 63.1 ms: 1.14x slower                                                                |
| scimark_lu                 | 54.0 ms                                                     | 61.6 ms: 1.14x slower                                                                |
| typing_runtime_protocols   | 100 us                                                      | 115 us: 1.14x slower                                                                 |
| genshi_text                | 14.9 ms                                                     | 17.0 ms: 1.14x slower                                                                |
| chaos                      | 37.9 ms                                                     | 43.3 ms: 1.14x slower                                                                |
| pyflate                    | 275 ms                                                      | 316 ms: 1.15x slower                                                                 |
| unpickle_pure_python       | 127 us                                                      | 146 us: 1.15x slower                                                                 |
| tomli_loads                | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| spectral_norm              | 59.2 ms                                                     | 68.3 ms: 1.15x slower                                                                |
| pickle_pure_python         | 183 us                                                      | 212 us: 1.16x slower                                                                 |
| sqlglot_transpile          | 952 us                                                      | 1.10 ms: 1.16x slower                                                                |
| pycparser                  | 758 ms                                                      | 883 ms: 1.17x slower                                                                 |
| comprehensions             | 10.2 us                                                     | 12.0 us: 1.17x slower                                                                |
| scimark_fft                | 174 ms                                                      | 203 ms: 1.17x slower                                                                 |
| sqlglot_parse              | 761 us                                                      | 890 us: 1.17x slower                                                                 |
| go                         | 84.6 ms                                                     | 99.2 ms: 1.17x slower                                                                |
| hexiom                     | 3.69 ms                                                     | 4.33 ms: 1.17x slower                                                                |
| float                      | 48.1 ms                                                     | 56.8 ms: 1.18x slower                                                                |
| fannkuch                   | 245 ms                                                      | 290 ms: 1.18x slower                                                                 |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.0 ms: 1.22x slower                                                                |
| deltablue                  | 1.86 ms                                                     | 2.27 ms: 1.22x slower                                                                |
| logging_silent             | 51.0 ns                                                     | 62.7 ns: 1.23x slower                                                                |
| raytrace                   | 156 ms                                                      | 194 ms: 1.24x slower                                                                 |
| richards_super             | 29.3 ms                                                     | 36.5 ms: 1.25x slower                                                                |
| richards                   | 26.0 ms                                                     | 32.5 ms: 1.25x slower                                                                |
| scimark_sor                | 72.0 ms                                                     | 90.2 ms: 1.25x slower                                                                |
| nbody                      | 64.5 ms                                                     | 83.5 ms: 1.30x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, async_tree_memoization, async_tree_none, bench_thread_pool, tornado_http, regex_dna, async_tree_cpu_io_mixed, regex_v8, python_startup_no_site, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown