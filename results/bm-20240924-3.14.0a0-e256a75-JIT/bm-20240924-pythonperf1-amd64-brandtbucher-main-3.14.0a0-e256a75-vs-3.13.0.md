# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.00x slower
- HPT reliability: 99.38%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 240 ms: 1.10x slower                                             |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.22x slower                                           |
| html5lib       | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                            |
| tornado_http   | 92.8 ms                                                     | 88.1 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                       | 1.08x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 477 ms: 1.37x faster                                             |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.37 sec: 1.20x faster                                           |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                             |
| async_tree_none            | 223 ms                                                      | 202 ms: 1.11x faster                                             |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.06x faster                                             |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 396 ms: 1.06x slower                                             |
| async_tree_io_tg           | 512 ms                                                      | 556 ms: 1.08x slower                                             |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                            |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                             |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                             |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.6 ms: 1.30x faster                                            |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                             |
| float          | 48.1 ms                                                     | 53.4 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                       | 1.05x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                            |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                             |
| regex_compile  | 80.1 ms                                                     | 94.7 ms: 1.18x slower                                            |
| Geometric mean | (ref)                                                       | 1.06x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.29 sec: 1.05x faster                                           |
| xml_etree_process    | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                            |
| xml_etree_iterparse  | 62.3 ms                                                     | 59.8 ms: 1.04x faster                                            |
| pickle_list          | 2.89 us                                                     | 2.79 us: 1.04x faster                                            |
| pickle_dict          | 18.0 us                                                     | 17.8 us: 1.02x faster                                            |
| xml_etree_parse      | 93.2 ms                                                     | 92.1 ms: 1.01x faster                                            |
| json_loads           | 14.3 us                                                     | 14.4 us: 1.01x slower                                            |
| pickle               | 7.34 us                                                     | 7.43 us: 1.01x slower                                            |
| unpickle_list        | 2.72 us                                                     | 2.76 us: 1.01x slower                                            |
| json_dumps           | 5.76 ms                                                     | 5.89 ms: 1.02x slower                                            |
| unpickle             | 8.63 us                                                     | 9.11 us: 1.06x slower                                            |
| pickle_pure_python   | 183 us                                                      | 196 us: 1.07x slower                                             |
| unpickle_pure_python | 127 us                                                      | 143 us: 1.13x slower                                             |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.20 ms: 1.20x faster                                            |
| django_template | 21.8 ms                                                     | 26.4 ms: 1.21x slower                                            |
| genshi_text     | 14.9 ms                                                     | 19.2 ms: 1.29x slower                                            |
| genshi_xml      | 32.8 ms                                                     | 45.5 ms: 1.39x slower                                            |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 516 us: 16.82x faster                                            |
| deepcopy_memo              | 21.8 us                                                     | 15.3 us: 1.43x faster                                            |
| asyncio_tcp                | 654 ms                                                      | 477 ms: 1.37x faster                                             |
| spectral_norm              | 59.2 ms                                                     | 44.8 ms: 1.32x faster                                            |
| nbody                      | 64.5 ms                                                     | 49.6 ms: 1.30x faster                                            |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                             |
| mako                       | 6.24 ms                                                     | 5.20 ms: 1.20x faster                                            |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.37 sec: 1.20x faster                                           |
| scimark_sor                | 72.0 ms                                                     | 60.5 ms: 1.19x faster                                            |
| scimark_fft                | 174 ms                                                      | 147 ms: 1.19x faster                                             |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.06 ms: 1.14x faster                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                             |
| crypto_pyaes               | 42.8 ms                                                     | 38.1 ms: 1.12x faster                                            |
| async_tree_none            | 223 ms                                                      | 202 ms: 1.11x faster                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.10x faster                                            |
| pycparser                  | 758 ms                                                      | 706 ms: 1.07x faster                                             |
| pathlib                    | 81.2 ms                                                     | 75.6 ms: 1.07x faster                                            |
| telco                      | 4.85 ms                                                     | 4.53 ms: 1.07x faster                                            |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.06x faster                                             |
| tornado_http               | 92.8 ms                                                     | 88.1 ms: 1.05x faster                                            |
| tomli_loads                | 1.36 sec                                                    | 1.29 sec: 1.05x faster                                           |
| fannkuch                   | 245 ms                                                      | 233 ms: 1.05x faster                                             |
| pyflate                    | 275 ms                                                      | 263 ms: 1.05x faster                                             |
| xml_etree_process          | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                            |
| xml_etree_iterparse        | 62.3 ms                                                     | 59.8 ms: 1.04x faster                                            |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.04x faster                                             |
| pickle_list                | 2.89 us                                                     | 2.79 us: 1.04x faster                                            |
| json                       | 2.98 ms                                                     | 2.90 ms: 1.03x faster                                            |
| deltablue                  | 1.86 ms                                                     | 1.83 ms: 1.02x faster                                            |
| pickle_dict                | 18.0 us                                                     | 17.8 us: 1.02x faster                                            |
| xml_etree_parse            | 93.2 ms                                                     | 92.1 ms: 1.01x faster                                            |
| gc_traversal               | 1.55 ms                                                     | 1.55 ms: 1.00x faster                                            |
| coverage                   | 46.7 ms                                                     | 46.5 ms: 1.00x faster                                            |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                             |
| json_loads                 | 14.3 us                                                     | 14.4 us: 1.01x slower                                            |
| bench_mp_pool              | 69.6 ms                                                     | 70.2 ms: 1.01x slower                                            |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                            |
| pickle                     | 7.34 us                                                     | 7.43 us: 1.01x slower                                            |
| unpickle_list              | 2.72 us                                                     | 2.76 us: 1.01x slower                                            |
| python_startup_no_site     | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                            |
| json_dumps                 | 5.76 ms                                                     | 5.89 ms: 1.02x slower                                            |
| comprehensions             | 10.2 us                                                     | 10.5 us: 1.02x slower                                            |
| logging_format             | 6.15 us                                                     | 6.33 us: 1.03x slower                                            |
| logging_simple             | 5.72 us                                                     | 5.91 us: 1.03x slower                                            |
| dulwich_log                | 40.4 ms                                                     | 42.0 ms: 1.04x slower                                            |
| meteor_contest             | 72.3 ms                                                     | 75.3 ms: 1.04x slower                                            |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                             |
| unpickle                   | 8.63 us                                                     | 9.11 us: 1.06x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 396 ms: 1.06x slower                                             |
| scimark_monte_carlo        | 40.3 ms                                                     | 42.7 ms: 1.06x slower                                            |
| pprint_safe_repr           | 493 ms                                                      | 524 ms: 1.06x slower                                             |
| pickle_pure_python         | 183 us                                                      | 196 us: 1.07x slower                                             |
| html5lib                   | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                            |
| chaos                      | 37.9 ms                                                     | 40.7 ms: 1.07x slower                                            |
| create_gc_cycles           | 829 us                                                      | 895 us: 1.08x slower                                             |
| sqlite_synth               | 1.60 us                                                     | 1.73 us: 1.08x slower                                            |
| pprint_pformat             | 991 ms                                                      | 1.07 sec: 1.08x slower                                           |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.08x slower                                           |
| async_tree_io_tg           | 512 ms                                                      | 556 ms: 1.08x slower                                             |
| nqueens                    | 55.5 ms                                                     | 60.2 ms: 1.08x slower                                            |
| go                         | 84.6 ms                                                     | 91.7 ms: 1.08x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                            |
| 2to3                       | 217 ms                                                      | 240 ms: 1.10x slower                                             |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                             |
| float                      | 48.1 ms                                                     | 53.4 ms: 1.11x slower                                            |
| typing_runtime_protocols   | 100 us                                                      | 112 us: 1.11x slower                                             |
| logging_silent             | 51.0 ns                                                     | 57.0 ns: 1.12x slower                                            |
| generators                 | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                            |
| unpickle_pure_python       | 127 us                                                      | 143 us: 1.13x slower                                             |
| sympy_str                  | 166 ms                                                      | 189 ms: 1.14x slower                                             |
| sympy_sum                  | 86.4 ms                                                     | 99.1 ms: 1.15x slower                                            |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                             |
| sqlglot_normalize          | 171 ms                                                      | 198 ms: 1.16x slower                                             |
| sympy_expand               | 285 ms                                                      | 332 ms: 1.16x slower                                             |
| sqlglot_parse              | 761 us                                                      | 887 us: 1.17x slower                                             |
| regex_compile              | 80.1 ms                                                     | 94.7 ms: 1.18x slower                                            |
| sqlglot_optimize           | 33.1 ms                                                     | 39.7 ms: 1.20x slower                                            |
| sympy_integrate            | 12.3 ms                                                     | 14.9 ms: 1.21x slower                                            |
| django_template            | 21.8 ms                                                     | 26.4 ms: 1.21x slower                                            |
| sqlglot_transpile          | 952 us                                                      | 1.16 ms: 1.22x slower                                            |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.22x slower                                           |
| pylint                     | 211 ms                                                      | 264 ms: 1.25x slower                                             |
| raytrace                   | 156 ms                                                      | 198 ms: 1.27x slower                                             |
| genshi_text                | 14.9 ms                                                     | 19.2 ms: 1.29x slower                                            |
| hexiom                     | 3.69 ms                                                     | 4.88 ms: 1.32x slower                                            |
| richards_super             | 29.3 ms                                                     | 39.3 ms: 1.34x slower                                            |
| genshi_xml                 | 32.8 ms                                                     | 45.5 ms: 1.39x slower                                            |
| richards                   | 26.0 ms                                                     | 36.6 ms: 1.41x slower                                            |
| unpack_sequence            | 40.0 ns                                                     | 59.6 ns: 1.49x slower                                            |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                     |

Benchmark hidden because not significant (6): xml_etree_generate, bench_thread_pool, regex_effbot, scimark_lu, python_startup, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 99.38% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown