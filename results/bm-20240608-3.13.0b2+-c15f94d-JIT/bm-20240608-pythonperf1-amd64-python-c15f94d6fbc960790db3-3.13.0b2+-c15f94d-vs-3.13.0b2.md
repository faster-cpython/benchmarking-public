# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 231 ms: 1.12x slower                                                        |
| chameleon      | 4.80 ms                                                         | 4.96 ms: 1.03x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                      |
| html5lib       | 35.0 ms                                                         | 36.5 ms: 1.04x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 86.3 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 620 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 400 ms: 1.03x slower                                                        |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 276 ms: 1.04x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 214 ms: 1.06x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.4 ms: 1.34x faster                                                       |
| float          | 49.7 ms                                                         | 44.3 ms: 1.12x faster                                                       |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                        |
| regex_compile  | 78.0 ms                                                         | 88.0 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                      |
| pickle_list          | 2.90 us                                                         | 2.80 us: 1.04x faster                                                       |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                                       |
| pickle_pure_python   | 175 us                                                          | 171 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.4 ms: 1.02x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 52.4 ms: 1.01x faster                                                       |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.00x slower                                                       |
| pickle               | 7.11 us                                                         | 7.18 us: 1.01x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.50 us: 1.01x slower                                                       |
| xml_etree_process    | 36.4 ms                                                         | 37.0 ms: 1.02x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.77 ms: 1.03x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.70 us: 1.03x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 126 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.07 ms: 1.25x faster                                                       |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm             | 63.7 ms                                                         | 44.4 ms: 1.43x faster                                                       |
| nbody                     | 67.6 ms                                                         | 50.4 ms: 1.34x faster                                                       |
| mako                      | 6.36 ms                                                         | 5.07 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                       |
| scimark_fft               | 171 ms                                                          | 148 ms: 1.16x faster                                                        |
| fannkuch                  | 243 ms                                                          | 211 ms: 1.15x faster                                                        |
| float                     | 49.7 ms                                                         | 44.3 ms: 1.12x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 41.4 ms: 1.10x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 20.1 us: 1.10x faster                                                       |
| pyflate                   | 279 ms                                                          | 257 ms: 1.08x faster                                                        |
| telco                     | 4.67 ms                                                         | 4.49 ms: 1.04x faster                                                       |
| pickle_list               | 2.90 us                                                         | 2.80 us: 1.04x faster                                                       |
| pickle_dict               | 18.1 us                                                         | 17.6 us: 1.03x faster                                                       |
| pickle_pure_python        | 175 us                                                          | 171 us: 1.03x faster                                                        |
| pprint_safe_repr          | 474 ms                                                          | 462 ms: 1.03x faster                                                        |
| pprint_pformat            | 966 ms                                                          | 947 ms: 1.02x faster                                                        |
| xml_etree_iterparse       | 62.3 ms                                                         | 61.4 ms: 1.02x faster                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 52.4 ms: 1.01x faster                                                       |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.01x faster                                                       |
| sqlite_synth              | 1.60 us                                                         | 1.58 us: 1.01x faster                                                       |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                        |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.00x slower                                                       |
| regex_dna                 | 119 ms                                                          | 120 ms: 1.01x slower                                                        |
| pickle                    | 7.11 us                                                         | 7.18 us: 1.01x slower                                                       |
| unpickle                  | 8.40 us                                                         | 8.50 us: 1.01x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 37.0 ms: 1.02x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 620 ms: 1.02x slower                                                        |
| chaos                     | 38.4 ms                                                         | 39.3 ms: 1.02x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.77 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 400 ms: 1.03x slower                                                        |
| chameleon                 | 4.80 ms                                                         | 4.96 ms: 1.03x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.70 us: 1.03x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 126 us: 1.03x slower                                                        |
| coroutines                | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                                       |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                        |
| create_gc_cycles          | 888 us                                                          | 924 us: 1.04x slower                                                        |
| meteor_contest            | 69.9 ms                                                         | 72.8 ms: 1.04x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 36.5 ms: 1.04x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 59.1 ms: 1.04x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 276 ms: 1.04x slower                                                        |
| aiohttp                   | 889 us                                                          | 929 us: 1.05x slower                                                        |
| deepcopy_reduce           | 1.99 us                                                         | 2.09 us: 1.05x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 86.3 ms: 1.06x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 214 ms: 1.06x slower                                                        |
| dulwich_log               | 38.0 ms                                                         | 40.5 ms: 1.07x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 56.5 ns: 1.07x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 800 us: 1.07x slower                                                        |
| richards                  | 26.7 ms                                                         | 28.6 ms: 1.07x slower                                                       |
| richards_super            | 30.2 ms                                                         | 32.3 ms: 1.07x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 69.4 ms: 1.07x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 824 us: 1.07x slower                                                        |
| scimark_sor               | 75.3 ms                                                         | 81.1 ms: 1.08x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.41 sec: 1.08x slower                                                      |
| deepcopy                  | 220 us                                                          | 237 us: 1.08x slower                                                        |
| python_startup            | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                       |
| generators                | 19.6 ms                                                         | 21.5 ms: 1.10x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 111 us: 1.10x slower                                                        |
| raytrace                  | 162 ms                                                          | 180 ms: 1.11x slower                                                        |
| coverage                  | 42.1 ms                                                         | 46.8 ms: 1.11x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 93.9 ms: 1.11x slower                                                       |
| 2to3                      | 207 ms                                                          | 231 ms: 1.12x slower                                                        |
| async_generators          | 223 ms                                                          | 249 ms: 1.12x slower                                                        |
| sqlglot_optimize          | 32.7 ms                                                         | 36.7 ms: 1.12x slower                                                       |
| thrift                    | 8.11 ms                                                         | 9.10 ms: 1.12x slower                                                       |
| sympy_str                 | 159 ms                                                          | 179 ms: 1.13x slower                                                        |
| regex_compile             | 78.0 ms                                                         | 88.0 ms: 1.13x slower                                                       |
| go                        | 82.1 ms                                                         | 93.6 ms: 1.14x slower                                                       |
| pylint                    | 205 ms                                                          | 235 ms: 1.15x slower                                                        |
| sympy_expand              | 271 ms                                                          | 312 ms: 1.15x slower                                                        |
| sympy_integrate           | 12.2 ms                                                         | 14.1 ms: 1.16x slower                                                       |
| mypy2                     | 418 ms                                                          | 484 ms: 1.16x slower                                                        |
| django_template           | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 69.0 ms: 1.22x slower                                                       |
| hexiom                    | 3.72 ms                                                         | 4.66 ms: 1.25x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.37 ms: 1.26x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.03x slower                                                                |

Benchmark hidden because not significant (15): json, asyncio_tcp_ssl, xml_etree_parse, pathlib, logging_simple, flaskblogging, regex_effbot, logging_format, gc_traversal, asyncio_tcp, scimark_monte_carlo, pycparser, async_tree_io, async_tree_cpu_io_mixed_tg, regex_v8
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown