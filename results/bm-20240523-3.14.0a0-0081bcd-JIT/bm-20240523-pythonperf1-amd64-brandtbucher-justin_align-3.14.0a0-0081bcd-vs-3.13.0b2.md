# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_align
- machine: windows-amd64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.01x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 233 ms: 1.13x slower                                                     |
| chameleon      | 4.80 ms                                                         | 5.08 ms: 1.06x slower                                                    |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                   |
| html5lib       | 35.0 ms                                                         | 37.6 ms: 1.07x slower                                                    |
| tornado_http   | 81.8 ms                                                         | 85.4 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                           | 1.08x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 625 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 404 ms: 1.04x slower                                                     |
| async_tree_io             | 588 ms                                                          | 611 ms: 1.04x slower                                                     |
| async_tree_memoization_tg | 258 ms                                                          | 275 ms: 1.06x slower                                                     |
| async_tree_none           | 218 ms                                                          | 233 ms: 1.07x slower                                                     |
| async_tree_memoization    | 264 ms                                                          | 283 ms: 1.07x slower                                                     |
| async_tree_none_tg        | 202 ms                                                          | 218 ms: 1.08x slower                                                     |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                             |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                    |
| float          | 49.7 ms                                                         | 44.6 ms: 1.11x faster                                                    |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                           | 1.14x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                     |
| regex_compile  | 78.0 ms                                                         | 87.4 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                           | 1.02x slower                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.24 sec: 1.09x faster                                                   |
| xml_etree_iterparse  | 62.3 ms                                                         | 59.8 ms: 1.04x faster                                                    |
| xml_etree_generate   | 53.2 ms                                                         | 51.5 ms: 1.03x faster                                                    |
| json_loads           | 14.2 us                                                         | 13.9 us: 1.02x faster                                                    |
| pickle_dict          | 18.1 us                                                         | 17.8 us: 1.02x faster                                                    |
| pickle_pure_python   | 175 us                                                          | 173 us: 1.02x faster                                                     |
| xml_etree_parse      | 90.9 ms                                                         | 89.9 ms: 1.01x faster                                                    |
| json_dumps           | 5.61 ms                                                         | 5.65 ms: 1.01x slower                                                    |
| unpickle             | 8.40 us                                                         | 8.68 us: 1.03x slower                                                    |
| unpickle_pure_python | 122 us                                                          | 127 us: 1.04x slower                                                     |
| pickle               | 7.11 us                                                         | 7.55 us: 1.06x slower                                                    |
| unpickle_list        | 2.62 us                                                         | 2.79 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                             |

Benchmark hidden because not significant (2): pickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.8 ms: 1.07x slower                                                    |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                    |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.00 ms: 1.27x faster                                                    |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                    |
| genshi_text     | 14.4 ms                                                         | 18.9 ms: 1.32x slower                                                    |
| genshi_xml      | 31.6 ms                                                         | 46.2 ms: 1.46x slower                                                    |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 506 us: 16.04x faster                                                    |
| spectral_norm             | 63.7 ms                                                         | 47.8 ms: 1.33x faster                                                    |
| nbody                     | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                    |
| mako                      | 6.36 ms                                                         | 5.00 ms: 1.27x faster                                                    |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                    |
| scimark_fft               | 171 ms                                                          | 149 ms: 1.15x faster                                                     |
| float                     | 49.7 ms                                                         | 44.6 ms: 1.11x faster                                                    |
| crypto_pyaes              | 45.5 ms                                                         | 41.0 ms: 1.11x faster                                                    |
| json                      | 3.19 ms                                                         | 2.88 ms: 1.11x faster                                                    |
| tomli_loads               | 1.35 sec                                                        | 1.24 sec: 1.09x faster                                                   |
| deepcopy_memo             | 22.1 us                                                         | 20.3 us: 1.09x faster                                                    |
| pyflate                   | 279 ms                                                          | 259 ms: 1.08x faster                                                     |
| fannkuch                  | 243 ms                                                          | 230 ms: 1.06x faster                                                     |
| pprint_pformat            | 966 ms                                                          | 920 ms: 1.05x faster                                                     |
| pprint_safe_repr          | 474 ms                                                          | 453 ms: 1.05x faster                                                     |
| xml_etree_iterparse       | 62.3 ms                                                         | 59.8 ms: 1.04x faster                                                    |
| xml_etree_generate        | 53.2 ms                                                         | 51.5 ms: 1.03x faster                                                    |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.9 ms: 1.03x faster                                                    |
| telco                     | 4.67 ms                                                         | 4.57 ms: 1.02x faster                                                    |
| json_loads                | 14.2 us                                                         | 13.9 us: 1.02x faster                                                    |
| pickle_dict               | 18.1 us                                                         | 17.8 us: 1.02x faster                                                    |
| pickle_pure_python        | 175 us                                                          | 173 us: 1.02x faster                                                     |
| xml_etree_parse           | 90.9 ms                                                         | 89.9 ms: 1.01x faster                                                    |
| comprehensions            | 10.4 us                                                         | 10.3 us: 1.01x faster                                                    |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                     |
| flaskblogging             | 2.03 sec                                                        | 2.03 sec: 1.00x faster                                                   |
| json_dumps                | 5.61 ms                                                         | 5.65 ms: 1.01x slower                                                    |
| sqlite_synth              | 1.60 us                                                         | 1.62 us: 1.01x slower                                                    |
| create_gc_cycles          | 888 us                                                          | 904 us: 1.02x slower                                                     |
| regex_dna                 | 119 ms                                                          | 121 ms: 1.02x slower                                                     |
| meteor_contest            | 69.9 ms                                                         | 72.1 ms: 1.03x slower                                                    |
| async_tree_io_tg          | 605 ms                                                          | 625 ms: 1.03x slower                                                     |
| unpickle                  | 8.40 us                                                         | 8.68 us: 1.03x slower                                                    |
| pathlib                   | 75.9 ms                                                         | 78.7 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 404 ms: 1.04x slower                                                     |
| chaos                     | 38.4 ms                                                         | 39.9 ms: 1.04x slower                                                    |
| async_tree_io             | 588 ms                                                          | 611 ms: 1.04x slower                                                     |
| tornado_http              | 81.8 ms                                                         | 85.4 ms: 1.04x slower                                                    |
| unpickle_pure_python      | 122 us                                                          | 127 us: 1.04x slower                                                     |
| deepcopy_reduce           | 1.99 us                                                         | 2.09 us: 1.05x slower                                                    |
| logging_silent            | 52.9 ns                                                         | 55.5 ns: 1.05x slower                                                    |
| chameleon                 | 4.80 ms                                                         | 5.08 ms: 1.06x slower                                                    |
| nqueens                   | 56.7 ms                                                         | 60.1 ms: 1.06x slower                                                    |
| pickle                    | 7.11 us                                                         | 7.55 us: 1.06x slower                                                    |
| async_tree_memoization_tg | 258 ms                                                          | 275 ms: 1.06x slower                                                     |
| unpickle_list             | 2.62 us                                                         | 2.79 us: 1.07x slower                                                    |
| async_tree_none           | 218 ms                                                          | 233 ms: 1.07x slower                                                     |
| coroutines                | 12.8 ms                                                         | 13.7 ms: 1.07x slower                                                    |
| html5lib                  | 35.0 ms                                                         | 37.6 ms: 1.07x slower                                                    |
| async_tree_memoization    | 264 ms                                                          | 283 ms: 1.07x slower                                                     |
| sqlglot_parse             | 748 us                                                          | 803 us: 1.07x slower                                                     |
| python_startup            | 20.3 ms                                                         | 21.8 ms: 1.07x slower                                                    |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                    |
| async_tree_none_tg        | 202 ms                                                          | 218 ms: 1.08x slower                                                     |
| bench_mp_pool             | 64.8 ms                                                         | 70.1 ms: 1.08x slower                                                    |
| raytrace                  | 162 ms                                                          | 176 ms: 1.08x slower                                                     |
| bench_thread_pool         | 768 us                                                          | 833 us: 1.08x slower                                                     |
| generators                | 19.6 ms                                                         | 21.3 ms: 1.09x slower                                                    |
| docutils                  | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                   |
| coverage                  | 42.1 ms                                                         | 46.0 ms: 1.09x slower                                                    |
| deepcopy                  | 220 us                                                          | 242 us: 1.10x slower                                                     |
| richards                  | 26.7 ms                                                         | 29.5 ms: 1.10x slower                                                    |
| sympy_sum                 | 84.4 ms                                                         | 93.3 ms: 1.11x slower                                                    |
| scimark_sor               | 75.3 ms                                                         | 83.4 ms: 1.11x slower                                                    |
| richards_super            | 30.2 ms                                                         | 33.4 ms: 1.11x slower                                                    |
| typing_runtime_protocols  | 101 us                                                          | 113 us: 1.11x slower                                                     |
| regex_compile             | 78.0 ms                                                         | 87.4 ms: 1.12x slower                                                    |
| sqlglot_optimize          | 32.7 ms                                                         | 36.7 ms: 1.12x slower                                                    |
| sympy_str                 | 159 ms                                                          | 178 ms: 1.12x slower                                                     |
| python_startup_no_site    | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                    |
| 2to3                      | 207 ms                                                          | 233 ms: 1.13x slower                                                     |
| mdp                       | 1.31 sec                                                        | 1.49 sec: 1.13x slower                                                   |
| sympy_integrate           | 12.2 ms                                                         | 13.9 ms: 1.14x slower                                                    |
| async_generators          | 223 ms                                                          | 254 ms: 1.14x slower                                                     |
| go                        | 82.1 ms                                                         | 94.5 ms: 1.15x slower                                                    |
| sympy_expand              | 271 ms                                                          | 312 ms: 1.15x slower                                                     |
| pylint                    | 205 ms                                                          | 237 ms: 1.16x slower                                                     |
| django_template           | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                    |
| scimark_lu                | 56.6 ms                                                         | 67.8 ms: 1.20x slower                                                    |
| hexiom                    | 3.72 ms                                                         | 4.66 ms: 1.25x slower                                                    |
| deltablue                 | 1.88 ms                                                         | 2.37 ms: 1.26x slower                                                    |
| genshi_text               | 14.4 ms                                                         | 18.9 ms: 1.32x slower                                                    |
| genshi_xml                | 31.6 ms                                                         | 46.2 ms: 1.46x slower                                                    |
| Geometric mean            | (ref)                                                           | 1.01x slower                                                             |

Benchmark hidden because not significant (11): regex_v8, pickle_list, asyncio_tcp_ssl, regex_effbot, xml_etree_process, gc_traversal, logging_format, logging_simple, asyncio_tcp, async_tree_cpu_io_mixed_tg, pycparser
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown