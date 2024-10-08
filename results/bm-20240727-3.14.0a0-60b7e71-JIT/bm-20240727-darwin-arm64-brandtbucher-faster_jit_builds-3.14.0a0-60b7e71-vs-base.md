# Results vs. base

- fork: brandtbucher
- ref: faster_jit_builds
- machine: darwin-arm64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.00x slower
- HPT reliability: 96.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                | 176 ms: 1.02x slower                                                     |
| html5lib       | 30.8 ms                                                               | 30.9 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_tcp         | 430 ms                                                                | 408 ms: 1.05x faster                                                     |
| async_generators    | 294 ms                                                                | 289 ms: 1.02x faster                                                     |
| async_tree_eager    | 62.2 ms                                                               | 61.8 ms: 1.01x faster                                                    |
| async_tree_eager_tg | 41.3 ms                                                               | 41.4 ms: 1.00x slower                                                    |
| coroutines          | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (16): asyncio_tcp_ssl, async_tree_none, async_tree_memoization, asyncio_websockets, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 62.9 ms                                                               | 63.0 ms: 1.00x slower                                                    |
| pidigits       | 282 ms                                                                | 282 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 151 ms                                                                | 150 ms: 1.01x faster                                                     |
| regex_compile  | 72.8 ms                                                               | 73.4 ms: 1.01x slower                                                    |
| regex_effbot   | 2.59 ms                                                               | 2.73 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads          | 17.2 us                                                               | 17.0 us: 1.01x faster                                                    |
| json_dumps          | 6.27 ms                                                               | 6.19 ms: 1.01x faster                                                    |
| xml_etree_process   | 35.8 ms                                                               | 35.4 ms: 1.01x faster                                                    |
| xml_etree_generate  | 51.9 ms                                                               | 51.7 ms: 1.00x faster                                                    |
| pickle_pure_python  | 174 us                                                                | 173 us: 1.00x faster                                                     |
| tomli_loads         | 1.24 sec                                                              | 1.24 sec: 1.01x slower                                                   |
| xml_etree_iterparse | 72.0 ms                                                               | 72.7 ms: 1.01x slower                                                    |
| xml_etree_parse     | 108 ms                                                                | 109 ms: 1.02x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.8 ms                                                               | 17.1 ms: 1.02x slower                                                    |
| python_startup_no_site | 14.0 ms                                                               | 14.3 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 22.2 ms                                                               | 21.3 ms: 1.04x faster                                                    |
| mako            | 6.47 ms                                                               | 6.43 ms: 1.01x faster                                                    |
| genshi_text     | 16.2 ms                                                               | 16.5 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_tcp             | 430 ms                                                                | 408 ms: 1.05x faster                                                     |
| django_template         | 22.2 ms                                                               | 21.3 ms: 1.04x faster                                                    |
| async_generators        | 294 ms                                                                | 289 ms: 1.02x faster                                                     |
| richards                | 30.8 ms                                                               | 30.4 ms: 1.01x faster                                                    |
| json_loads              | 17.2 us                                                               | 17.0 us: 1.01x faster                                                    |
| json_dumps              | 6.27 ms                                                               | 6.19 ms: 1.01x faster                                                    |
| xml_etree_process       | 35.8 ms                                                               | 35.4 ms: 1.01x faster                                                    |
| coverage                | 46.5 ms                                                               | 46.0 ms: 1.01x faster                                                    |
| sqlglot_optimize        | 33.1 ms                                                               | 32.8 ms: 1.01x faster                                                    |
| sympy_sum               | 74.1 ms                                                               | 73.4 ms: 1.01x faster                                                    |
| regex_dna               | 151 ms                                                                | 150 ms: 1.01x faster                                                     |
| async_tree_eager        | 62.2 ms                                                               | 61.8 ms: 1.01x faster                                                    |
| scimark_fft             | 183 ms                                                                | 182 ms: 1.01x faster                                                     |
| sympy_str               | 140 ms                                                                | 140 ms: 1.01x faster                                                     |
| sympy_expand            | 243 ms                                                                | 241 ms: 1.01x faster                                                     |
| mako                    | 6.47 ms                                                               | 6.43 ms: 1.01x faster                                                    |
| deepcopy_memo           | 16.6 us                                                               | 16.6 us: 1.00x faster                                                    |
| sqlglot_transpile       | 1.01 ms                                                               | 1.00 ms: 1.00x faster                                                    |
| xml_etree_generate      | 51.9 ms                                                               | 51.7 ms: 1.00x faster                                                    |
| pickle_pure_python      | 174 us                                                                | 173 us: 1.00x faster                                                     |
| comprehensions          | 12.3 us                                                               | 12.3 us: 1.00x faster                                                    |
| nbody                   | 62.9 ms                                                               | 63.0 ms: 1.00x slower                                                    |
| pidigits                | 282 ms                                                                | 282 ms: 1.00x slower                                                     |
| pprint_safe_repr        | 486 ms                                                                | 487 ms: 1.00x slower                                                     |
| deepcopy                | 154 us                                                                | 154 us: 1.00x slower                                                     |
| raytrace                | 160 ms                                                                | 160 ms: 1.00x slower                                                     |
| chaos                   | 38.4 ms                                                               | 38.5 ms: 1.00x slower                                                    |
| bpe_tokeniser           | 3.02 sec                                                              | 3.03 sec: 1.00x slower                                                   |
| async_tree_eager_tg     | 41.3 ms                                                               | 41.4 ms: 1.00x slower                                                    |
| logging_silent          | 61.1 ns                                                               | 61.4 ns: 1.00x slower                                                    |
| crypto_pyaes            | 51.7 ms                                                               | 51.9 ms: 1.00x slower                                                    |
| deepcopy_reduce         | 1.53 us                                                               | 1.54 us: 1.00x slower                                                    |
| html5lib                | 30.8 ms                                                               | 30.9 ms: 1.00x slower                                                    |
| generators              | 21.5 ms                                                               | 21.6 ms: 1.00x slower                                                    |
| go                      | 100 ms                                                                | 101 ms: 1.01x slower                                                     |
| pprint_pformat          | 997 ms                                                                | 1.00 sec: 1.01x slower                                                   |
| sympy_integrate         | 11.1 ms                                                               | 11.2 ms: 1.01x slower                                                    |
| fannkuch                | 246 ms                                                                | 248 ms: 1.01x slower                                                     |
| tomli_loads             | 1.24 sec                                                              | 1.24 sec: 1.01x slower                                                   |
| regex_compile           | 72.8 ms                                                               | 73.4 ms: 1.01x slower                                                    |
| scimark_sor             | 99.9 ms                                                               | 101 ms: 1.01x slower                                                     |
| scimark_lu              | 79.4 ms                                                               | 80.2 ms: 1.01x slower                                                    |
| xml_etree_iterparse     | 72.0 ms                                                               | 72.7 ms: 1.01x slower                                                    |
| mdp                     | 1.42 sec                                                              | 1.44 sec: 1.01x slower                                                   |
| coroutines              | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult | 2.86 ms                                                               | 2.89 ms: 1.01x slower                                                    |
| richards_super          | 34.1 ms                                                               | 34.6 ms: 1.01x slower                                                    |
| xml_etree_parse         | 108 ms                                                                | 109 ms: 1.02x slower                                                     |
| dulwich_log             | 28.0 ms                                                               | 28.5 ms: 1.02x slower                                                    |
| python_startup          | 16.8 ms                                                               | 17.1 ms: 1.02x slower                                                    |
| 2to3                    | 173 ms                                                                | 176 ms: 1.02x slower                                                     |
| thrift                  | 431 us                                                                | 440 us: 1.02x slower                                                     |
| genshi_text             | 16.2 ms                                                               | 16.5 ms: 1.02x slower                                                    |
| python_startup_no_site  | 14.0 ms                                                               | 14.3 ms: 1.02x slower                                                    |
| scimark_monte_carlo     | 42.7 ms                                                               | 43.9 ms: 1.03x slower                                                    |
| regex_effbot            | 2.59 ms                                                               | 2.73 ms: 1.05x slower                                                    |
| pycparser               | 669 ms                                                                | 708 ms: 1.06x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (42): bench_mp_pool, asyncio_tcp_ssl, async_tree_none, gc_traversal, genshi_xml, float, create_gc_cycles, async_tree_memoization, logging_format, tornado_http, asyncio_websockets, docutils, meteor_contest, async_tree_eager_memoization_tg, pyflate, async_tree_cpu_io_mixed_tg, dask, sqlglot_parse, nqueens, regex_v8, typing_runtime_protocols, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_io, deltablue, async_tree_memoization_tg, logging_simple, async_tree_io_tg, spectral_norm, async_tree_none_tg, telco, hexiom, pylint, sqlglot_normalize, async_tree_io, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, json, bench_thread_pool, unpickle_pure_python, pathlib

# HPT report

- Reliability score: 96.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x