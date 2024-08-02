# Results vs. base

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-amd64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                                     | 227 ms: 1.09x slower                                                       |
| docutils       | 1.61 sec                                                                   | 1.68 sec: 1.05x slower                                                     |
| html5lib       | 34.8 ms                                                                    | 38.4 ms: 1.10x slower                                                      |
| tornado_http   | 80.3 ms                                                                    | 82.7 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 376 ms                                                                     | 387 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 372 ms                                                                     | 392 ms: 1.05x slower                                                       |
| async_tree_memoization_tg  | 235 ms                                                                     | 247 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 509 ms                                                                     | 539 ms: 1.06x slower                                                       |
| async_tree_memoization     | 241 ms                                                                     | 261 ms: 1.08x slower                                                       |
| async_tree_none_tg         | 179 ms                                                                     | 198 ms: 1.11x slower                                                       |
| async_tree_none            | 196 ms                                                                     | 218 ms: 1.11x slower                                                       |
| async_tree_io              | 507 ms                                                                     | 570 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                                      | 1.08x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 151 ms                                                                     | 150 ms: 1.00x faster                                                       |
| float          | 49.5 ms                                                                    | 58.3 ms: 1.18x slower                                                      |
| nbody          | 66.8 ms                                                                    | 83.8 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                     | 127 ms: 1.06x slower                                                       |
| regex_compile  | 76.1 ms                                                                    | 88.1 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.07x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 94.7 ms                                                                    | 93.4 ms: 1.01x faster                                                      |
| json_loads           | 13.8 us                                                                    | 14.2 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 63.7 ms                                                                    | 67.7 ms: 1.06x slower                                                      |
| json_dumps           | 5.65 ms                                                                    | 6.00 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                                    | 59.5 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.4 ms                                                                    | 42.1 ms: 1.15x slower                                                      |
| tomli_loads          | 1.37 sec                                                                   | 1.62 sec: 1.18x slower                                                     |
| pickle_pure_python   | 177 us                                                                     | 214 us: 1.21x slower                                                       |
| unpickle_pure_python | 123 us                                                                     | 161 us: 1.31x slower                                                       |
| Geometric mean       | (ref)                                                                      | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.4 ms                                                                    | 17.0 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.8 ms                                                                    | 24.7 ms: 1.14x slower                                                      |
| genshi_text     | 14.8 ms                                                                    | 16.9 ms: 1.14x slower                                                      |
| genshi_xml      | 32.6 ms                                                                    | 38.6 ms: 1.18x slower                                                      |
| mako            | 6.59 ms                                                                    | 7.87 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240626-pythonperf1-amd64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site     | 17.4 ms                                                                    | 17.0 ms: 1.02x faster                                                      |
| xml_etree_parse            | 94.7 ms                                                                    | 93.4 ms: 1.01x faster                                                      |
| pidigits                   | 151 ms                                                                     | 150 ms: 1.00x faster                                                       |
| create_gc_cycles           | 889 us                                                                     | 902 us: 1.01x slower                                                       |
| coverage                   | 45.7 ms                                                                    | 46.4 ms: 1.02x slower                                                      |
| bench_mp_pool              | 64.9 ms                                                                    | 66.0 ms: 1.02x slower                                                      |
| json                       | 2.89 ms                                                                    | 2.96 ms: 1.02x slower                                                      |
| json_loads                 | 13.8 us                                                                    | 14.2 us: 1.03x slower                                                      |
| tornado_http               | 80.3 ms                                                                    | 82.7 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed    | 376 ms                                                                     | 387 ms: 1.03x slower                                                       |
| bench_thread_pool          | 746 us                                                                     | 771 us: 1.03x slower                                                       |
| thrift                     | 507 us                                                                     | 528 us: 1.04x slower                                                       |
| docutils                   | 1.61 sec                                                                   | 1.68 sec: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 372 ms                                                                     | 392 ms: 1.05x slower                                                       |
| async_tree_memoization_tg  | 235 ms                                                                     | 247 ms: 1.05x slower                                                       |
| mdp                        | 1.35 sec                                                                   | 1.42 sec: 1.05x slower                                                     |
| sympy_sum                  | 84.2 ms                                                                    | 88.8 ms: 1.05x slower                                                      |
| regex_dna                  | 120 ms                                                                     | 127 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 509 ms                                                                     | 539 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 63.7 ms                                                                    | 67.7 ms: 1.06x slower                                                      |
| json_dumps                 | 5.65 ms                                                                    | 6.00 ms: 1.06x slower                                                      |
| sympy_expand               | 275 ms                                                                     | 295 ms: 1.07x slower                                                       |
| sympy_str                  | 160 ms                                                                     | 173 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 32.6 ms                                                                    | 35.2 ms: 1.08x slower                                                      |
| sqlglot_normalize          | 174 ms                                                                     | 188 ms: 1.08x slower                                                       |
| async_tree_memoization     | 241 ms                                                                     | 261 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.2 ms                                                                    | 13.2 ms: 1.08x slower                                                      |
| telco                      | 4.64 ms                                                                    | 5.03 ms: 1.08x slower                                                      |
| 2to3                       | 209 ms                                                                     | 227 ms: 1.09x slower                                                       |
| meteor_contest             | 70.8 ms                                                                    | 77.5 ms: 1.09x slower                                                      |
| html5lib                   | 34.8 ms                                                                    | 38.4 ms: 1.10x slower                                                      |
| coroutines                 | 13.3 ms                                                                    | 14.7 ms: 1.10x slower                                                      |
| async_tree_none_tg         | 179 ms                                                                     | 198 ms: 1.11x slower                                                       |
| logging_format             | 6.09 us                                                                    | 6.76 us: 1.11x slower                                                      |
| logging_simple             | 5.66 us                                                                    | 6.29 us: 1.11x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                                    | 59.5 ms: 1.11x slower                                                      |
| async_tree_none            | 196 ms                                                                     | 218 ms: 1.11x slower                                                       |
| deepcopy_reduce            | 1.68 us                                                                    | 1.87 us: 1.12x slower                                                      |
| async_generators           | 227 ms                                                                     | 255 ms: 1.12x slower                                                       |
| async_tree_io              | 507 ms                                                                     | 570 ms: 1.12x slower                                                       |
| deepcopy                   | 164 us                                                                     | 185 us: 1.13x slower                                                       |
| django_template            | 21.8 ms                                                                    | 24.7 ms: 1.14x slower                                                      |
| nqueens                    | 56.9 ms                                                                    | 64.8 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 100 us                                                                     | 114 us: 1.14x slower                                                       |
| genshi_text                | 14.8 ms                                                                    | 16.9 ms: 1.14x slower                                                      |
| generators                 | 20.3 ms                                                                    | 23.3 ms: 1.15x slower                                                      |
| go                         | 83.5 ms                                                                    | 95.8 ms: 1.15x slower                                                      |
| xml_etree_process          | 36.4 ms                                                                    | 42.1 ms: 1.15x slower                                                      |
| regex_compile              | 76.1 ms                                                                    | 88.1 ms: 1.16x slower                                                      |
| pprint_pformat             | 982 ms                                                                     | 1.15 sec: 1.17x slower                                                     |
| sqlglot_transpile          | 962 us                                                                     | 1.13 ms: 1.17x slower                                                      |
| deltablue                  | 1.93 ms                                                                    | 2.27 ms: 1.17x slower                                                      |
| pprint_safe_repr           | 481 ms                                                                     | 564 ms: 1.17x slower                                                       |
| chaos                      | 38.0 ms                                                                    | 44.6 ms: 1.17x slower                                                      |
| pyflate                    | 279 ms                                                                     | 328 ms: 1.17x slower                                                       |
| richards_super             | 29.5 ms                                                                    | 34.7 ms: 1.18x slower                                                      |
| scimark_sparse_mat_mult    | 2.63 ms                                                                    | 3.09 ms: 1.18x slower                                                      |
| float                      | 49.5 ms                                                                    | 58.3 ms: 1.18x slower                                                      |
| tomli_loads                | 1.37 sec                                                                   | 1.62 sec: 1.18x slower                                                     |
| genshi_xml                 | 32.6 ms                                                                    | 38.6 ms: 1.18x slower                                                      |
| sqlglot_parse              | 768 us                                                                     | 911 us: 1.19x slower                                                       |
| raytrace                   | 157 ms                                                                     | 186 ms: 1.19x slower                                                       |
| crypto_pyaes               | 44.9 ms                                                                    | 53.5 ms: 1.19x slower                                                      |
| richards                   | 26.0 ms                                                                    | 31.1 ms: 1.19x slower                                                      |
| mako                       | 6.59 ms                                                                    | 7.87 ms: 1.19x slower                                                      |
| pickle_pure_python         | 177 us                                                                     | 214 us: 1.21x slower                                                       |
| spectral_norm              | 61.4 ms                                                                    | 74.7 ms: 1.22x slower                                                      |
| scimark_lu                 | 55.3 ms                                                                    | 67.5 ms: 1.22x slower                                                      |
| comprehensions             | 10.3 us                                                                    | 12.5 us: 1.22x slower                                                      |
| logging_silent             | 53.8 ns                                                                    | 66.3 ns: 1.23x slower                                                      |
| hexiom                     | 3.70 ms                                                                    | 4.56 ms: 1.23x slower                                                      |
| scimark_sor                | 73.5 ms                                                                    | 92.0 ms: 1.25x slower                                                      |
| nbody                      | 66.8 ms                                                                    | 83.8 ms: 1.25x slower                                                      |
| scimark_fft                | 174 ms                                                                     | 220 ms: 1.26x slower                                                       |
| deepcopy_memo              | 17.1 us                                                                    | 21.8 us: 1.27x slower                                                      |
| fannkuch                   | 243 ms                                                                     | 311 ms: 1.28x slower                                                       |
| scimark_monte_carlo        | 39.6 ms                                                                    | 51.9 ms: 1.31x slower                                                      |
| unpickle_pure_python       | 123 us                                                                     | 161 us: 1.31x slower                                                       |
| Geometric mean             | (ref)                                                                      | 1.11x slower                                                               |

Benchmark hidden because not significant (9): python_startup, asyncio_tcp, regex_effbot, gc_traversal, pathlib, pycparser, pylint, asyncio_tcp_ssl, regex_v8

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown