# Results vs. base

- fork: brandtbucher
- ref: cache_dynamic_exits
- machine: linux-x86_64
- commit hash: 55bff1c
- commit date: 2024-08-28
- overall geometric mean: 1.00x slower
- HPT reliability: 58.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 274 ms: 1.01x faster                                                       |
| docutils       | 3.04 sec                                                              | 3.05 sec: 1.00x slower                                                     |
| html5lib       | 63.4 ms                                                               | 66.8 ms: 1.05x slower                                                      |
| tornado_http   | 94.7 ms                                                               | 94.3 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines       | 23.0 ms                                                               | 22.5 ms: 1.03x faster                                                      |
| asyncio_tcp      | 499 ms                                                                | 491 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                     |
| async_tree_io    | 924 ms                                                                | 933 ms: 1.01x slower                                                       |
| async_generators | 454 ms                                                                | 461 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (8): async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 82.0 ms                                                               | 79.7 ms: 1.03x faster                                                      |
| pidigits       | 187 ms                                                                | 185 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 143 ms: 1.01x slower                                                       |
| regex_effbot   | 3.51 ms                                                               | 3.56 ms: 1.02x slower                                                      |
| regex_v8       | 23.9 ms                                                               | 24.4 ms: 1.02x slower                                                      |
| regex_dna      | 210 ms                                                                | 217 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 77.7 ms                                                               | 76.6 ms: 1.01x faster                                                      |
| xml_etree_process    | 54.7 ms                                                               | 54.2 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.3 ms: 1.01x slower                                                      |
| tomli_loads          | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                                     |
| pickle_pure_python   | 302 us                                                                | 305 us: 1.01x slower                                                       |
| unpickle_pure_python | 213 us                                                                | 215 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 23.8 ms: 1.08x faster                                                      |
| genshi_xml      | 59.0 ms                                                               | 56.4 ms: 1.05x faster                                                      |
| mako            | 9.79 ms                                                               | 9.87 ms: 1.01x slower                                                      |
| django_template | 35.6 ms                                                               | 37.7 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text             | 25.7 ms                                                               | 23.8 ms: 1.08x faster                                                      |
| genshi_xml              | 59.0 ms                                                               | 56.4 ms: 1.05x faster                                                      |
| nbody                   | 82.0 ms                                                               | 79.7 ms: 1.03x faster                                                      |
| coroutines              | 23.0 ms                                                               | 22.5 ms: 1.03x faster                                                      |
| nqueens                 | 85.7 ms                                                               | 83.8 ms: 1.02x faster                                                      |
| sympy_integrate         | 22.8 ms                                                               | 22.3 ms: 1.02x faster                                                      |
| sympy_sum               | 171 ms                                                                | 169 ms: 1.02x faster                                                       |
| asyncio_tcp             | 499 ms                                                                | 491 ms: 1.01x faster                                                       |
| xml_etree_generate      | 77.7 ms                                                               | 76.6 ms: 1.01x faster                                                      |
| pyflate                 | 450 ms                                                                | 445 ms: 1.01x faster                                                       |
| pidigits                | 187 ms                                                                | 185 ms: 1.01x faster                                                       |
| crypto_pyaes            | 66.6 ms                                                               | 65.9 ms: 1.01x faster                                                      |
| logging_simple          | 5.54 us                                                               | 5.49 us: 1.01x faster                                                      |
| scimark_fft             | 314 ms                                                                | 311 ms: 1.01x faster                                                       |
| xml_etree_process       | 54.7 ms                                                               | 54.2 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult | 4.47 ms                                                               | 4.44 ms: 1.01x faster                                                      |
| mdp                     | 2.56 sec                                                              | 2.54 sec: 1.01x faster                                                     |
| 2to3                    | 276 ms                                                                | 274 ms: 1.01x faster                                                       |
| meteor_contest          | 106 ms                                                                | 106 ms: 1.00x faster                                                       |
| fannkuch                | 372 ms                                                                | 370 ms: 1.00x faster                                                       |
| tornado_http            | 94.7 ms                                                               | 94.3 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                     |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| bench_thread_pool       | 817 us                                                                | 820 us: 1.00x slower                                                       |
| docutils                | 3.04 sec                                                              | 3.05 sec: 1.00x slower                                                     |
| deepcopy_memo           | 27.0 us                                                               | 27.1 us: 1.00x slower                                                      |
| deltablue               | 3.18 ms                                                               | 3.20 ms: 1.01x slower                                                      |
| coverage                | 85.6 ms                                                               | 86.2 ms: 1.01x slower                                                      |
| regex_compile           | 142 ms                                                                | 143 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 97.7 ms                                                               | 98.3 ms: 1.01x slower                                                      |
| tomli_loads             | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                                     |
| hexiom                  | 6.89 ms                                                               | 6.95 ms: 1.01x slower                                                      |
| mako                    | 9.79 ms                                                               | 9.87 ms: 1.01x slower                                                      |
| pickle_pure_python      | 302 us                                                                | 305 us: 1.01x slower                                                       |
| richards_super          | 45.0 ms                                                               | 45.4 ms: 1.01x slower                                                      |
| async_tree_io           | 924 ms                                                                | 933 ms: 1.01x slower                                                       |
| unpickle_pure_python    | 213 us                                                                | 215 us: 1.01x slower                                                       |
| sqlglot_parse           | 1.34 ms                                                               | 1.35 ms: 1.01x slower                                                      |
| deepcopy                | 265 us                                                                | 269 us: 1.01x slower                                                       |
| async_generators        | 454 ms                                                                | 461 ms: 1.02x slower                                                       |
| regex_effbot            | 3.51 ms                                                               | 3.56 ms: 1.02x slower                                                      |
| create_gc_cycles        | 1.75 ms                                                               | 1.78 ms: 1.02x slower                                                      |
| telco                   | 7.63 ms                                                               | 7.75 ms: 1.02x slower                                                      |
| raytrace                | 276 ms                                                                | 281 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 1.69 ms                                                               | 1.71 ms: 1.02x slower                                                      |
| generators              | 33.3 ms                                                               | 33.9 ms: 1.02x slower                                                      |
| sympy_expand            | 504 ms                                                                | 514 ms: 1.02x slower                                                       |
| regex_v8                | 23.9 ms                                                               | 24.4 ms: 1.02x slower                                                      |
| richards                | 38.6 ms                                                               | 39.6 ms: 1.03x slower                                                      |
| regex_dna               | 210 ms                                                                | 217 ms: 1.03x slower                                                       |
| scimark_lu              | 109 ms                                                                | 114 ms: 1.05x slower                                                       |
| gc_traversal            | 3.58 ms                                                               | 3.75 ms: 1.05x slower                                                      |
| html5lib                | 63.4 ms                                                               | 66.8 ms: 1.05x slower                                                      |
| django_template         | 35.6 ms                                                               | 37.7 ms: 1.06x slower                                                      |
| scimark_sor             | 116 ms                                                                | 127 ms: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (34): pylint, async_tree_none, typing_runtime_protocols, json, chaos, asyncio_websockets, pprint_safe_repr, sqlglot_optimize, async_tree_none_tg, pycparser, deepcopy_reduce, bpe_tokeniser, spectral_norm, thrift, comprehensions, sympy_str, json_loads, xml_etree_parse, python_startup_no_site, logging_silent, async_tree_cpu_io_mixed, bench_mp_pool, json_dumps, float, async_tree_memoization_tg, scimark_monte_carlo, sqlglot_normalize, async_tree_cpu_io_mixed_tg, pathlib, go, pprint_pformat, logging_format, async_tree_memoization, async_tree_io_tg

# HPT report

- Reliability score: 58.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x