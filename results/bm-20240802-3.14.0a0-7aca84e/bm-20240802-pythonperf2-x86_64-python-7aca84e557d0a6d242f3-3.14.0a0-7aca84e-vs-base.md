# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                      | 287 ms: 1.01x slower                                                        |
| docutils       | 2.97 sec                                                                    | 3.00 sec: 1.01x slower                                                      |
| html5lib       | 72.3 ms                                                                     | 74.1 ms: 1.02x slower                                                       |
| tornado_http   | 118 ms                                                                      | 116 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines     | 21.1 ms                                                                     | 21.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (12): async_tree_io, async_tree_io_tg, async_generators, asyncio_tcp_ssl, asyncio_tcp, async_tree_memoization, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                                      | 252 ms: 1.00x slower                                                        |
| float          | 79.7 ms                                                                     | 81.0 ms: 1.02x slower                                                       |
| nbody          | 87.9 ms                                                                     | 90.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                                      | 143 ms: 1.01x slower                                                        |
| regex_dna      | 240 ms                                                                      | 254 ms: 1.06x slower                                                        |
| regex_v8       | 25.4 ms                                                                     | 26.9 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 326 us                                                                      | 312 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                                      | 102 ms: 1.01x slower                                                        |
| unpickle_pure_python | 211 us                                                                      | 213 us: 1.01x slower                                                        |
| xml_etree_parse      | 141 ms                                                                      | 143 ms: 1.01x slower                                                        |
| xml_etree_process    | 58.8 ms                                                                     | 59.5 ms: 1.01x slower                                                       |
| json_dumps           | 10.6 ms                                                                     | 10.8 ms: 1.02x slower                                                       |
| tomli_loads          | 2.24 sec                                                                    | 2.28 sec: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                                     | 13.3 ms: 1.00x slower                                                       |
| python_startup_no_site | 9.02 ms                                                                     | 9.04 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 55.1 ms                                                                     | 54.0 ms: 1.02x faster                                                       |
| genshi_text    | 25.7 ms                                                                     | 25.4 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_lu              | 97.8 ms                                                                     | 93.5 ms: 1.05x faster                                                       |
| pickle_pure_python      | 326 us                                                                      | 312 us: 1.04x faster                                                        |
| thrift                  | 890 us                                                                      | 871 us: 1.02x faster                                                        |
| genshi_xml              | 55.1 ms                                                                     | 54.0 ms: 1.02x faster                                                       |
| json                    | 5.53 ms                                                                     | 5.42 ms: 1.02x faster                                                       |
| raytrace                | 281 ms                                                                      | 276 ms: 1.02x faster                                                        |
| scimark_sor             | 110 ms                                                                      | 108 ms: 1.02x faster                                                        |
| pycparser               | 1.26 sec                                                                    | 1.24 sec: 1.02x faster                                                      |
| tornado_http            | 118 ms                                                                      | 116 ms: 1.02x faster                                                        |
| sqlglot_normalize       | 119 ms                                                                      | 118 ms: 1.01x faster                                                        |
| deepcopy                | 289 us                                                                      | 286 us: 1.01x faster                                                        |
| genshi_text             | 25.7 ms                                                                     | 25.4 ms: 1.01x faster                                                       |
| sqlglot_optimize        | 58.9 ms                                                                     | 58.3 ms: 1.01x faster                                                       |
| generators              | 29.0 ms                                                                     | 28.7 ms: 1.01x faster                                                       |
| scimark_monte_carlo     | 67.7 ms                                                                     | 67.2 ms: 1.01x faster                                                       |
| deepcopy_memo           | 30.1 us                                                                     | 29.9 us: 1.01x faster                                                       |
| chaos                   | 61.6 ms                                                                     | 61.1 ms: 1.01x faster                                                       |
| python_startup          | 13.3 ms                                                                     | 13.3 ms: 1.00x slower                                                       |
| python_startup_no_site  | 9.02 ms                                                                     | 9.04 ms: 1.00x slower                                                       |
| pidigits                | 252 ms                                                                      | 252 ms: 1.00x slower                                                        |
| mdp                     | 2.50 sec                                                                    | 2.50 sec: 1.00x slower                                                      |
| comprehensions          | 17.4 us                                                                     | 17.5 us: 1.00x slower                                                       |
| sympy_str               | 295 ms                                                                      | 296 ms: 1.00x slower                                                        |
| 2to3                    | 285 ms                                                                      | 287 ms: 1.01x slower                                                        |
| bpe_tokeniser           | 4.87 sec                                                                    | 4.90 sec: 1.01x slower                                                      |
| richards                | 50.9 ms                                                                     | 51.2 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 101 ms                                                                      | 102 ms: 1.01x slower                                                        |
| docutils                | 2.97 sec                                                                    | 3.00 sec: 1.01x slower                                                      |
| unpickle_pure_python    | 211 us                                                                      | 213 us: 1.01x slower                                                        |
| sympy_expand            | 501 ms                                                                      | 507 ms: 1.01x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                                     | 1.41 ms: 1.01x slower                                                       |
| crypto_pyaes            | 71.8 ms                                                                     | 72.6 ms: 1.01x slower                                                       |
| telco                   | 7.88 ms                                                                     | 7.98 ms: 1.01x slower                                                       |
| xml_etree_parse         | 141 ms                                                                      | 143 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.77 ms                                                                     | 1.79 ms: 1.01x slower                                                       |
| xml_etree_process       | 58.8 ms                                                                     | 59.5 ms: 1.01x slower                                                       |
| nqueens                 | 88.2 ms                                                                     | 89.4 ms: 1.01x slower                                                       |
| regex_compile           | 141 ms                                                                      | 143 ms: 1.01x slower                                                        |
| logging_format          | 6.91 us                                                                     | 7.02 us: 1.02x slower                                                       |
| pyflate                 | 484 ms                                                                      | 492 ms: 1.02x slower                                                        |
| float                   | 79.7 ms                                                                     | 81.0 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult | 4.16 ms                                                                     | 4.23 ms: 1.02x slower                                                       |
| json_dumps              | 10.6 ms                                                                     | 10.8 ms: 1.02x slower                                                       |
| deltablue               | 3.39 ms                                                                     | 3.45 ms: 1.02x slower                                                       |
| tomli_loads             | 2.24 sec                                                                    | 2.28 sec: 1.02x slower                                                      |
| logging_silent          | 95.9 ns                                                                     | 97.8 ns: 1.02x slower                                                       |
| pprint_pformat          | 1.68 sec                                                                    | 1.71 sec: 1.02x slower                                                      |
| pprint_safe_repr        | 820 ms                                                                      | 837 ms: 1.02x slower                                                        |
| fannkuch                | 362 ms                                                                      | 370 ms: 1.02x slower                                                        |
| meteor_contest          | 125 ms                                                                      | 128 ms: 1.02x slower                                                        |
| create_gc_cycles        | 1.99 ms                                                                     | 2.04 ms: 1.02x slower                                                       |
| html5lib                | 72.3 ms                                                                     | 74.1 ms: 1.02x slower                                                       |
| scimark_fft             | 295 ms                                                                      | 302 ms: 1.02x slower                                                        |
| hexiom                  | 6.11 ms                                                                     | 6.27 ms: 1.03x slower                                                       |
| nbody                   | 87.9 ms                                                                     | 90.6 ms: 1.03x slower                                                       |
| coroutines              | 21.1 ms                                                                     | 21.8 ms: 1.03x slower                                                       |
| logging_simple          | 6.27 us                                                                     | 6.47 us: 1.03x slower                                                       |
| coverage                | 84.5 ms                                                                     | 87.3 ms: 1.03x slower                                                       |
| go                      | 157 ms                                                                      | 163 ms: 1.04x slower                                                        |
| regex_dna               | 240 ms                                                                      | 254 ms: 1.06x slower                                                        |
| regex_v8                | 25.4 ms                                                                     | 26.9 ms: 1.06x slower                                                       |
| gc_traversal            | 4.35 ms                                                                     | 4.74 ms: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (28): async_tree_io, async_tree_io_tg, django_template, async_generators, sympy_integrate, json_loads, sympy_sum, richards_super, regex_effbot, asyncio_tcp_ssl, asyncio_tcp, pathlib, async_tree_memoization, deepcopy_reduce, xml_etree_generate, spectral_norm, asyncio_websockets, async_tree_memoization_tg, mako, typing_runtime_protocols, async_tree_cpu_io_mixed, pylint, async_tree_cpu_io_mixed_tg, dask, bench_thread_pool, async_tree_none, async_tree_none_tg, bench_mp_pool

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x