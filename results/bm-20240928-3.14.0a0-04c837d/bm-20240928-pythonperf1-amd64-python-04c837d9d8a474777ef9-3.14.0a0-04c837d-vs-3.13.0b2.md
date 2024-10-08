# Results vs. 3.13.0b2

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.8 ms: 1.17x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 92.7 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 563 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 211 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 56.2 ms: 1.13x slower                                                      |
| nbody          | 67.6 ms                                                         | 89.4 ms: 1.32x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| regex_compile  | 78.0 ms                                                         | 92.9 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.19 us: 1.01x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.6 ms: 1.03x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.01 us: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.1 ms: 1.06x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.86 us: 1.09x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.4 ms: 1.10x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.24 us: 1.10x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.6 ms: 1.14x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.43 ms: 1.14x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 221 us: 1.26x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 156 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.88 ms: 1.08x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.8 ms: 1.13x slower                                                      |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 535 us: 15.15x faster                                                      |
| deepcopy                   | 220 us                                                          | 190 us: 1.16x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 563 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 211 ms: 1.03x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 21.6 us: 1.02x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.95 us: 1.02x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.19 us: 1.01x slower                                                      |
| pickle_dict                | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.63 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.03x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 93.6 ms: 1.03x slower                                                      |
| pickle_list                | 2.90 us                                                         | 3.01 us: 1.04x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| telco                      | 4.67 ms                                                         | 4.91 ms: 1.05x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.6 ms: 1.05x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 80.2 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.1 ms: 1.06x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.58 sec: 1.07x slower                                                     |
| bench_mp_pool              | 64.8 ms                                                         | 69.1 ms: 1.07x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.5 ms: 1.07x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 825 us: 1.08x slower                                                       |
| mako                       | 6.36 ms                                                         | 6.88 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 109 us: 1.08x slower                                                       |
| spectral_norm              | 63.7 ms                                                         | 69.2 ms: 1.08x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 49.4 ms: 1.09x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.86 us: 1.09x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.4 ms: 1.09x slower                                                      |
| go                         | 82.1 ms                                                         | 89.7 ms: 1.09x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 58.4 ms: 1.10x slower                                                      |
| pylint                     | 205 ms                                                          | 225 ms: 1.10x slower                                                       |
| 2to3                       | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| unpickle                   | 8.40 us                                                         | 9.24 us: 1.10x slower                                                      |
| async_generators           | 223 ms                                                          | 246 ms: 1.10x slower                                                       |
| logging_format             | 6.22 us                                                         | 6.90 us: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 526 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.80 ms: 1.12x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.47 us: 1.12x slower                                                      |
| sympy_str                  | 159 ms                                                          | 179 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 36.8 ms: 1.12x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 195 ms: 1.13x slower                                                       |
| float                      | 49.7 ms                                                         | 56.2 ms: 1.13x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 92.7 ms: 1.13x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 35.8 ms: 1.13x slower                                                      |
| coverage                   | 42.1 ms                                                         | 47.7 ms: 1.13x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.6 ms: 1.14x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 79.9 ms: 1.14x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.43 ms: 1.14x slower                                                      |
| sympy_expand               | 271 ms                                                          | 310 ms: 1.15x slower                                                       |
| dulwich_log                | 38.0 ms                                                         | 43.9 ms: 1.15x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 65.8 ms: 1.16x slower                                                      |
| chaos                      | 38.4 ms                                                         | 44.7 ms: 1.16x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 40.8 ms: 1.17x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.9 ms: 1.17x slower                                                      |
| pyflate                    | 279 ms                                                          | 330 ms: 1.18x slower                                                       |
| django_template            | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| comprehensions             | 10.4 us                                                         | 12.3 us: 1.18x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.13 ms: 1.18x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.55 sec: 1.18x slower                                                     |
| pprint_pformat             | 966 ms                                                          | 1.15 sec: 1.19x slower                                                     |
| genshi_text                | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 564 ms: 1.19x slower                                                       |
| regex_compile              | 78.0 ms                                                         | 92.9 ms: 1.19x slower                                                      |
| scimark_fft                | 171 ms                                                          | 205 ms: 1.20x slower                                                       |
| scimark_lu                 | 56.6 ms                                                         | 68.1 ms: 1.20x slower                                                      |
| raytrace                   | 162 ms                                                          | 196 ms: 1.21x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| sqlglot_parse              | 748 us                                                          | 906 us: 1.21x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.32 ms: 1.23x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 65.4 ns: 1.24x slower                                                      |
| richards_super             | 30.2 ms                                                         | 37.4 ms: 1.24x slower                                                      |
| richards                   | 26.7 ms                                                         | 33.3 ms: 1.25x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 221 us: 1.26x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.70 ms: 1.26x slower                                                      |
| fannkuch                   | 243 ms                                                          | 308 ms: 1.27x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 95.5 ms: 1.27x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 156 us: 1.28x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 51.6 ms: 1.32x slower                                                      |
| nbody                      | 67.6 ms                                                         | 89.4 ms: 1.32x slower                                                      |
| json                       | 3.19 ms                                                         | 4.24 ms: 1.33x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (10): regex_v8, pycparser, async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, json_loads, regex_dna, create_gc_cycles, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown