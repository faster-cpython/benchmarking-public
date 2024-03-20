# Results vs. base

- fork: brandtbucher
- ref: justin_plt
- machine: darwin-arm64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                 | 182 ms: 1.03x faster                                               |
| chameleon      | 4.87 ms                                                                | 4.81 ms: 1.01x faster                                              |
| docutils       | 1.53 sec                                                               | 1.50 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager    | 70.4 ms                                                                | 69.7 ms: 1.01x faster                                              |
| async_tree_eager_tg | 47.4 ms                                                                | 47.3 ms: 1.00x faster                                              |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (14): async_tree_eager_io, async_tree_memoization, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 70.2 ms                                                                | 69.2 ms: 1.02x faster                                              |
| float          | 53.0 ms                                                                | 52.6 ms: 1.01x faster                                              |
| pidigits       | 283 ms                                                                 | 282 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 84.9 ms                                                                | 76.8 ms: 1.10x faster                                              |
| regex_v8       | 17.2 ms                                                                | 17.2 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                               | 1.29 sec: 1.05x faster                                             |
| unpickle_pure_python | 150 us                                                                 | 147 us: 1.02x faster                                               |
| xml_etree_generate   | 56.8 ms                                                                | 56.2 ms: 1.01x faster                                              |
| pickle               | 7.29 us                                                                | 7.25 us: 1.01x faster                                              |
| json_loads           | 17.1 us                                                                | 17.1 us: 1.00x faster                                              |
| json_dumps           | 6.47 ms                                                                | 6.51 ms: 1.01x slower                                              |
| pickle_pure_python   | 196 us                                                                 | 198 us: 1.01x slower                                               |
| unpickle_list        | 3.05 us                                                                | 3.08 us: 1.01x slower                                              |
| xml_etree_parse      | 105 ms                                                                 | 107 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (5): xml_etree_iterparse, unpickle, xml_etree_process, pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.7 ms                                                                | 15.6 ms: 1.08x faster                                              |
| python_startup         | 18.5 ms                                                                | 17.2 ms: 1.07x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.07x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 36.9 ms                                                                | 34.6 ms: 1.07x faster                                              |
| mako           | 6.74 ms                                                                | 6.55 ms: 1.03x faster                                              |
| genshi_text    | 15.8 ms                                                                | 15.5 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpack_sequence         | 114 ns                                                                 | 72.7 ns: 1.57x faster                                              |
| fannkuch                | 311 ms                                                                 | 247 ms: 1.26x faster                                               |
| richards                | 37.5 ms                                                                | 32.6 ms: 1.15x faster                                              |
| richards_super          | 41.5 ms                                                                | 36.4 ms: 1.14x faster                                              |
| regex_compile           | 84.9 ms                                                                | 76.8 ms: 1.10x faster                                              |
| hexiom                  | 5.13 ms                                                                | 4.64 ms: 1.10x faster                                              |
| pprint_safe_repr        | 519 ms                                                                 | 473 ms: 1.10x faster                                               |
| pprint_pformat          | 1.06 sec                                                               | 972 ms: 1.09x faster                                               |
| pyflate                 | 343 ms                                                                 | 318 ms: 1.08x faster                                               |
| python_startup_no_site  | 16.7 ms                                                                | 15.6 ms: 1.08x faster                                              |
| python_startup          | 18.5 ms                                                                | 17.2 ms: 1.07x faster                                              |
| go                      | 115 ms                                                                 | 107 ms: 1.07x faster                                               |
| genshi_xml              | 36.9 ms                                                                | 34.6 ms: 1.07x faster                                              |
| tomli_loads             | 1.36 sec                                                               | 1.29 sec: 1.05x faster                                             |
| scimark_monte_carlo     | 44.2 ms                                                                | 42.1 ms: 1.05x faster                                              |
| comprehensions          | 12.6 us                                                                | 12.1 us: 1.04x faster                                              |
| scimark_sparse_mat_mult | 3.15 ms                                                                | 3.03 ms: 1.04x faster                                              |
| bench_mp_pool           | 53.2 ms                                                                | 51.3 ms: 1.04x faster                                              |
| spectral_norm           | 74.8 ms                                                                | 72.2 ms: 1.04x faster                                              |
| sympy_integrate         | 11.5 ms                                                                | 11.1 ms: 1.04x faster                                              |
| sympy_sum               | 77.7 ms                                                                | 75.0 ms: 1.04x faster                                              |
| sqlglot_transpile       | 1.02 ms                                                                | 988 us: 1.03x faster                                               |
| pycparser               | 727 ms                                                                 | 705 ms: 1.03x faster                                               |
| telco                   | 4.58 ms                                                                | 4.44 ms: 1.03x faster                                              |
| sqlglot_parse           | 831 us                                                                 | 805 us: 1.03x faster                                               |
| mako                    | 6.74 ms                                                                | 6.55 ms: 1.03x faster                                              |
| sqlglot_optimize        | 35.4 ms                                                                | 34.5 ms: 1.03x faster                                              |
| 2to3                    | 187 ms                                                                 | 182 ms: 1.03x faster                                               |
| sympy_str               | 145 ms                                                                 | 142 ms: 1.03x faster                                               |
| scimark_fft             | 200 ms                                                                 | 195 ms: 1.03x faster                                               |
| crypto_pyaes            | 47.7 ms                                                                | 46.5 ms: 1.02x faster                                              |
| raytrace                | 192 ms                                                                 | 187 ms: 1.02x faster                                               |
| chaos                   | 40.4 ms                                                                | 39.5 ms: 1.02x faster                                              |
| docutils                | 1.53 sec                                                               | 1.50 sec: 1.02x faster                                             |
| unpickle_pure_python    | 150 us                                                                 | 147 us: 1.02x faster                                               |
| scimark_lu              | 85.7 ms                                                                | 83.9 ms: 1.02x faster                                              |
| nqueens                 | 64.2 ms                                                                | 63.1 ms: 1.02x faster                                              |
| meteor_contest          | 75.2 ms                                                                | 74.1 ms: 1.02x faster                                              |
| nbody                   | 70.2 ms                                                                | 69.2 ms: 1.02x faster                                              |
| logging_simple          | 3.50 us                                                                | 3.45 us: 1.01x faster                                              |
| deepcopy_reduce         | 2.00 us                                                                | 1.97 us: 1.01x faster                                              |
| genshi_text             | 15.8 ms                                                                | 15.5 ms: 1.01x faster                                              |
| chameleon               | 4.87 ms                                                                | 4.81 ms: 1.01x faster                                              |
| sympy_expand            | 249 ms                                                                 | 246 ms: 1.01x faster                                               |
| logging_format          | 3.79 us                                                                | 3.74 us: 1.01x faster                                              |
| deepcopy                | 231 us                                                                 | 228 us: 1.01x faster                                               |
| mdp                     | 1.62 sec                                                               | 1.60 sec: 1.01x faster                                             |
| bench_thread_pool       | 514 us                                                                 | 508 us: 1.01x faster                                               |
| xml_etree_generate      | 56.8 ms                                                                | 56.2 ms: 1.01x faster                                              |
| async_tree_eager        | 70.4 ms                                                                | 69.7 ms: 1.01x faster                                              |
| scimark_sor             | 111 ms                                                                 | 110 ms: 1.01x faster                                               |
| coverage                | 47.9 ms                                                                | 47.5 ms: 1.01x faster                                              |
| deltablue               | 2.53 ms                                                                | 2.51 ms: 1.01x faster                                              |
| sqlglot_normalize       | 182 ms                                                                 | 181 ms: 1.01x faster                                               |
| deepcopy_memo           | 26.2 us                                                                | 26.0 us: 1.01x faster                                              |
| generators              | 28.5 ms                                                                | 28.3 ms: 1.01x faster                                              |
| float                   | 53.0 ms                                                                | 52.6 ms: 1.01x faster                                              |
| async_generators        | 313 ms                                                                 | 311 ms: 1.01x faster                                               |
| pickle                  | 7.29 us                                                                | 7.25 us: 1.01x faster                                              |
| json                    | 2.97 ms                                                                | 2.95 ms: 1.01x faster                                              |
| dulwich_log             | 30.6 ms                                                                | 30.5 ms: 1.00x faster                                              |
| pidigits                | 283 ms                                                                 | 282 ms: 1.00x faster                                               |
| logging_silent          | 72.3 ns                                                                | 72.1 ns: 1.00x faster                                              |
| regex_v8                | 17.2 ms                                                                | 17.2 ms: 1.00x faster                                              |
| json_loads              | 17.1 us                                                                | 17.1 us: 1.00x faster                                              |
| async_tree_eager_tg     | 47.4 ms                                                                | 47.3 ms: 1.00x faster                                              |
| sqlite_synth            | 1.58 us                                                                | 1.59 us: 1.00x slower                                              |
| json_dumps              | 6.47 ms                                                                | 6.51 ms: 1.01x slower                                              |
| thrift                  | 461 us                                                                 | 464 us: 1.01x slower                                               |
| create_gc_cycles        | 714 us                                                                 | 719 us: 1.01x slower                                               |
| pickle_pure_python      | 196 us                                                                 | 198 us: 1.01x slower                                               |
| unpickle_list           | 3.05 us                                                                | 3.08 us: 1.01x slower                                              |
| xml_etree_parse         | 105 ms                                                                 | 107 ms: 1.01x slower                                               |
| coroutines              | 18.1 ms                                                                | 18.4 ms: 1.01x slower                                              |
| Geometric mean          | (ref)                                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (35): asyncio_tcp, mypy2, pylint, gunicorn, async_tree_eager_io, pathlib, html5lib, aiohttp, typing_runtime_protocols, async_tree_memoization, async_tree_eager_cpu_io_mixed, xml_etree_iterparse, async_tree_io, async_tree_none, unpickle, asyncio_tcp_ssl, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_cpu_io_mixed, xml_etree_process, gc_traversal, async_tree_memoization_tg, regex_effbot, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_none_tg, regex_dna, dask, pickle_dict, asyncio_websockets, django_template, pickle_list, tornado_http


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.80x