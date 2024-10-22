# Results vs. base

- fork: mdboom
- ref: initialize_locals
- machine: linux-x86_64
- commit hash: 1021191
- commit date: 2024-08-29
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 284 ms: 1.00x slower                                                     |
| docutils       | 2.92 sec                                                                    | 2.93 sec: 1.00x slower                                                   |
| html5lib       | 70.5 ms                                                                     | 71.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets     | 391 ms                                                                      | 387 ms: 1.01x faster                                                     |
| asyncio_tcp            | 368 ms                                                                      | 369 ms: 1.00x slower                                                     |
| coroutines             | 21.3 ms                                                                     | 21.4 ms: 1.00x slower                                                    |
| async_tree_memoization | 399 ms                                                                      | 402 ms: 1.01x slower                                                     |
| async_generators       | 363 ms                                                                      | 371 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                             |

Benchmark hidden because not significant (8): async_tree_none_tg, asyncio_tcp_ssl, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                     | 78.4 ms: 1.01x faster                                                    |
| pidigits       | 254 ms                                                                      | 253 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                      | 235 ms: 1.08x faster                                                     |
| regex_effbot   | 3.58 ms                                                                     | 3.50 ms: 1.02x faster                                                    |
| regex_compile  | 140 ms                                                                      | 142 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 146 ms                                                                      | 144 ms: 1.01x faster                                                     |
| json_dumps           | 10.9 ms                                                                     | 11.0 ms: 1.00x slower                                                    |
| xml_etree_process    | 59.2 ms                                                                     | 59.5 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 101 ms                                                                      | 101 ms: 1.01x slower                                                     |
| json_loads           | 24.7 us                                                                     | 24.9 us: 1.01x slower                                                    |
| xml_etree_generate   | 84.8 ms                                                                     | 85.7 ms: 1.01x slower                                                    |
| pickle_pure_python   | 314 us                                                                      | 318 us: 1.01x slower                                                     |
| tomli_loads          | 2.53 sec                                                                    | 2.58 sec: 1.02x slower                                                   |
| unpickle_pure_python | 210 us                                                                      | 219 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 9.06 ms                                                                     | 9.09 ms: 1.00x slower                                                    |
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 54.8 ms                                                                     | 53.6 ms: 1.02x faster                                                    |
| mako            | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                    |
| genshi_text     | 24.7 ms                                                                     | 24.9 ms: 1.01x slower                                                    |
| django_template | 40.0 ms                                                                     | 41.2 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna               | 254 ms                                                                      | 235 ms: 1.08x faster                                                     |
| logging_format          | 6.99 us                                                                     | 6.78 us: 1.03x faster                                                    |
| logging_simple          | 6.43 us                                                                     | 6.27 us: 1.03x faster                                                    |
| gc_traversal            | 4.58 ms                                                                     | 4.47 ms: 1.02x faster                                                    |
| genshi_xml              | 54.8 ms                                                                     | 53.6 ms: 1.02x faster                                                    |
| regex_effbot            | 3.58 ms                                                                     | 3.50 ms: 1.02x faster                                                    |
| float                   | 79.4 ms                                                                     | 78.4 ms: 1.01x faster                                                    |
| xml_etree_parse         | 146 ms                                                                      | 144 ms: 1.01x faster                                                     |
| asyncio_websockets      | 391 ms                                                                      | 387 ms: 1.01x faster                                                     |
| fannkuch                | 354 ms                                                                      | 351 ms: 1.01x faster                                                     |
| comprehensions          | 17.7 us                                                                     | 17.6 us: 1.01x faster                                                    |
| bpe_tokeniser           | 4.93 sec                                                                    | 4.91 sec: 1.01x faster                                                   |
| richards_super          | 56.8 ms                                                                     | 56.5 ms: 1.01x faster                                                    |
| pprint_safe_repr        | 799 ms                                                                      | 795 ms: 1.00x faster                                                     |
| spectral_norm           | 96.9 ms                                                                     | 96.5 ms: 1.00x faster                                                    |
| pidigits                | 254 ms                                                                      | 253 ms: 1.00x faster                                                     |
| python_startup_no_site  | 9.06 ms                                                                     | 9.09 ms: 1.00x slower                                                    |
| meteor_contest          | 127 ms                                                                      | 127 ms: 1.00x slower                                                     |
| asyncio_tcp             | 368 ms                                                                      | 369 ms: 1.00x slower                                                     |
| docutils                | 2.92 sec                                                                    | 2.93 sec: 1.00x slower                                                   |
| 2to3                    | 282 ms                                                                      | 284 ms: 1.00x slower                                                     |
| coroutines              | 21.3 ms                                                                     | 21.4 ms: 1.00x slower                                                    |
| json_dumps              | 10.9 ms                                                                     | 11.0 ms: 1.00x slower                                                    |
| xml_etree_process       | 59.2 ms                                                                     | 59.5 ms: 1.01x slower                                                    |
| python_startup          | 13.4 ms                                                                     | 13.4 ms: 1.01x slower                                                    |
| xml_etree_iterparse     | 101 ms                                                                      | 101 ms: 1.01x slower                                                     |
| hexiom                  | 6.17 ms                                                                     | 6.20 ms: 1.01x slower                                                    |
| async_tree_memoization  | 399 ms                                                                      | 402 ms: 1.01x slower                                                     |
| telco                   | 8.31 ms                                                                     | 8.37 ms: 1.01x slower                                                    |
| json_loads              | 24.7 us                                                                     | 24.9 us: 1.01x slower                                                    |
| nqueens                 | 89.2 ms                                                                     | 89.9 ms: 1.01x slower                                                    |
| scimark_sor             | 118 ms                                                                      | 119 ms: 1.01x slower                                                     |
| scimark_monte_carlo     | 66.2 ms                                                                     | 66.7 ms: 1.01x slower                                                    |
| sympy_integrate         | 23.0 ms                                                                     | 23.2 ms: 1.01x slower                                                    |
| mako                    | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                    |
| html5lib                | 70.5 ms                                                                     | 71.2 ms: 1.01x slower                                                    |
| sqlglot_normalize       | 119 ms                                                                      | 120 ms: 1.01x slower                                                     |
| genshi_text             | 24.7 ms                                                                     | 24.9 ms: 1.01x slower                                                    |
| sympy_sum               | 152 ms                                                                      | 153 ms: 1.01x slower                                                     |
| xml_etree_generate      | 84.8 ms                                                                     | 85.7 ms: 1.01x slower                                                    |
| deepcopy_reduce         | 2.88 us                                                                     | 2.91 us: 1.01x slower                                                    |
| chaos                   | 61.0 ms                                                                     | 61.8 ms: 1.01x slower                                                    |
| pathlib                 | 15.7 ms                                                                     | 15.9 ms: 1.01x slower                                                    |
| sqlglot_parse           | 1.42 ms                                                                     | 1.44 ms: 1.01x slower                                                    |
| pickle_pure_python      | 314 us                                                                      | 318 us: 1.01x slower                                                     |
| regex_compile           | 140 ms                                                                      | 142 ms: 1.01x slower                                                     |
| sympy_str               | 291 ms                                                                      | 295 ms: 1.02x slower                                                     |
| generators              | 28.6 ms                                                                     | 29.1 ms: 1.02x slower                                                    |
| scimark_fft             | 307 ms                                                                      | 313 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult | 4.22 ms                                                                     | 4.30 ms: 1.02x slower                                                    |
| tomli_loads             | 2.53 sec                                                                    | 2.58 sec: 1.02x slower                                                   |
| sqlglot_optimize        | 58.5 ms                                                                     | 59.7 ms: 1.02x slower                                                    |
| sqlglot_transpile       | 1.79 ms                                                                     | 1.83 ms: 1.02x slower                                                    |
| sympy_expand            | 496 ms                                                                      | 506 ms: 1.02x slower                                                     |
| async_generators        | 363 ms                                                                      | 371 ms: 1.02x slower                                                     |
| mdp                     | 2.48 sec                                                                    | 2.53 sec: 1.02x slower                                                   |
| crypto_pyaes            | 72.2 ms                                                                     | 73.9 ms: 1.02x slower                                                    |
| go                      | 133 ms                                                                      | 137 ms: 1.03x slower                                                     |
| deepcopy                | 280 us                                                                      | 287 us: 1.03x slower                                                     |
| thrift                  | 848 us                                                                      | 872 us: 1.03x slower                                                     |
| django_template         | 40.0 ms                                                                     | 41.2 ms: 1.03x slower                                                    |
| create_gc_cycles        | 1.93 ms                                                                     | 1.99 ms: 1.03x slower                                                    |
| pycparser               | 1.21 sec                                                                    | 1.25 sec: 1.04x slower                                                   |
| logging_silent          | 97.7 ns                                                                     | 101 ns: 1.04x slower                                                     |
| unpickle_pure_python    | 210 us                                                                      | 219 us: 1.04x slower                                                     |
| raytrace                | 272 ms                                                                      | 285 ms: 1.04x slower                                                     |
| deepcopy_memo           | 28.5 us                                                                     | 29.9 us: 1.05x slower                                                    |
| coverage                | 76.2 ms                                                                     | 80.1 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                                       | 1.01x slower                                                             |

Benchmark hidden because not significant (21): regex_v8, json, nbody, pprint_pformat, deltablue, scimark_lu, pyflate, richards, typing_runtime_protocols, pylint, async_tree_none_tg, asyncio_tcp_ssl, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, tornado_http, async_tree_io_tg, bench_thread_pool, bench_mp_pool, async_tree_none

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x