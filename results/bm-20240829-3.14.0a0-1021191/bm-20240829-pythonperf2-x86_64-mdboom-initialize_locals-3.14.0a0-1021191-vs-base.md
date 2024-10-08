# Results vs. base

- fork: mdboom
- ref: initialize_locals
- machine: linux-x86_64
- commit hash: 1021191
- commit date: 2024-08-29
- overall geometric mean: 1.00x slower
- HPT reliability: 97.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 284 ms: 1.01x slower                                                     |
| docutils       | 2.92 sec                                                                    | 2.93 sec: 1.01x slower                                                   |
| html5lib       | 70.5 ms                                                                     | 71.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|--------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets | 391 ms                                                                      | 387 ms: 1.01x faster                                                     |
| async_generators   | 373 ms                                                                      | 371 ms: 1.01x faster                                                     |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_io, asyncio_tcp, async_tree_memoization_tg, coroutines, asyncio_tcp_ssl, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                     | 78.4 ms: 1.01x faster                                                    |
| nbody          | 85.8 ms                                                                     | 84.8 ms: 1.01x faster                                                    |
| pidigits       | 252 ms                                                                      | 253 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 233 ms                                                                      | 235 ms: 1.01x slower                                                     |
| regex_compile  | 140 ms                                                                      | 142 ms: 1.01x slower                                                     |
| regex_effbot   | 3.45 ms                                                                     | 3.50 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 24.7 us                                                                     | 24.9 us: 1.01x slower                                                    |
| xml_etree_generate   | 84.9 ms                                                                     | 85.7 ms: 1.01x slower                                                    |
| xml_etree_process    | 58.8 ms                                                                     | 59.5 ms: 1.01x slower                                                    |
| json_dumps           | 10.8 ms                                                                     | 11.0 ms: 1.01x slower                                                    |
| pickle_pure_python   | 313 us                                                                      | 318 us: 1.02x slower                                                     |
| unpickle_pure_python | 215 us                                                                      | 219 us: 1.02x slower                                                     |
| tomli_loads          | 2.53 sec                                                                    | 2.58 sec: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 9.07 ms                                                                     | 9.09 ms: 1.00x slower                                                    |
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 54.6 ms                                                                     | 53.6 ms: 1.02x faster                                                    |
| mako            | 10.5 ms                                                                     | 10.4 ms: 1.02x faster                                                    |
| genshi_text     | 25.1 ms                                                                     | 24.9 ms: 1.01x faster                                                    |
| django_template | 40.4 ms                                                                     | 41.2 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| logging_format           | 7.08 us                                                                     | 6.78 us: 1.04x faster                                                    |
| coverage                 | 83.2 ms                                                                     | 80.1 ms: 1.04x faster                                                    |
| logging_simple           | 6.47 us                                                                     | 6.27 us: 1.03x faster                                                    |
| fannkuch                 | 361 ms                                                                      | 351 ms: 1.03x faster                                                     |
| generators               | 29.8 ms                                                                     | 29.1 ms: 1.03x faster                                                    |
| gc_traversal             | 4.57 ms                                                                     | 4.47 ms: 1.02x faster                                                    |
| scimark_lu               | 97.5 ms                                                                     | 95.6 ms: 1.02x faster                                                    |
| genshi_xml               | 54.6 ms                                                                     | 53.6 ms: 1.02x faster                                                    |
| mako                     | 10.5 ms                                                                     | 10.4 ms: 1.02x faster                                                    |
| bpe_tokeniser            | 4.99 sec                                                                    | 4.91 sec: 1.02x faster                                                   |
| pathlib                  | 16.1 ms                                                                     | 15.9 ms: 1.01x faster                                                    |
| json                     | 5.37 ms                                                                     | 5.30 ms: 1.01x faster                                                    |
| float                    | 79.4 ms                                                                     | 78.4 ms: 1.01x faster                                                    |
| pprint_pformat           | 1.64 sec                                                                    | 1.62 sec: 1.01x faster                                                   |
| nbody                    | 85.8 ms                                                                     | 84.8 ms: 1.01x faster                                                    |
| richards                 | 50.6 ms                                                                     | 50.0 ms: 1.01x faster                                                    |
| asyncio_websockets       | 391 ms                                                                      | 387 ms: 1.01x faster                                                     |
| deepcopy                 | 290 us                                                                      | 287 us: 1.01x faster                                                     |
| genshi_text              | 25.1 ms                                                                     | 24.9 ms: 1.01x faster                                                    |
| pyflate                  | 473 ms                                                                      | 469 ms: 1.01x faster                                                     |
| richards_super           | 56.8 ms                                                                     | 56.5 ms: 1.01x faster                                                    |
| async_generators         | 373 ms                                                                      | 371 ms: 1.01x faster                                                     |
| python_startup_no_site   | 9.07 ms                                                                     | 9.09 ms: 1.00x slower                                                    |
| pidigits                 | 252 ms                                                                      | 253 ms: 1.00x slower                                                     |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                    |
| nqueens                  | 89.5 ms                                                                     | 89.9 ms: 1.00x slower                                                    |
| sqlglot_optimize         | 59.5 ms                                                                     | 59.7 ms: 1.00x slower                                                    |
| 2to3                     | 282 ms                                                                      | 284 ms: 1.01x slower                                                     |
| json_loads               | 24.7 us                                                                     | 24.9 us: 1.01x slower                                                    |
| docutils                 | 2.92 sec                                                                    | 2.93 sec: 1.01x slower                                                   |
| regex_dna                | 233 ms                                                                      | 235 ms: 1.01x slower                                                     |
| sympy_integrate          | 23.0 ms                                                                     | 23.2 ms: 1.01x slower                                                    |
| html5lib                 | 70.5 ms                                                                     | 71.2 ms: 1.01x slower                                                    |
| scimark_monte_carlo      | 66.1 ms                                                                     | 66.7 ms: 1.01x slower                                                    |
| xml_etree_generate       | 84.9 ms                                                                     | 85.7 ms: 1.01x slower                                                    |
| telco                    | 8.28 ms                                                                     | 8.37 ms: 1.01x slower                                                    |
| regex_compile            | 140 ms                                                                      | 142 ms: 1.01x slower                                                     |
| sqlglot_parse            | 1.42 ms                                                                     | 1.44 ms: 1.01x slower                                                    |
| thrift                   | 862 us                                                                      | 872 us: 1.01x slower                                                     |
| crypto_pyaes             | 73.0 ms                                                                     | 73.9 ms: 1.01x slower                                                    |
| spectral_norm            | 95.3 ms                                                                     | 96.5 ms: 1.01x slower                                                    |
| xml_etree_process        | 58.8 ms                                                                     | 59.5 ms: 1.01x slower                                                    |
| json_dumps               | 10.8 ms                                                                     | 11.0 ms: 1.01x slower                                                    |
| sympy_str                | 291 ms                                                                      | 295 ms: 1.01x slower                                                     |
| pickle_pure_python       | 313 us                                                                      | 318 us: 1.02x slower                                                     |
| regex_effbot             | 3.45 ms                                                                     | 3.50 ms: 1.02x slower                                                    |
| comprehensions           | 17.3 us                                                                     | 17.6 us: 1.02x slower                                                    |
| meteor_contest           | 125 ms                                                                      | 127 ms: 1.02x slower                                                     |
| sympy_expand             | 498 ms                                                                      | 506 ms: 1.02x slower                                                     |
| unpickle_pure_python     | 215 us                                                                      | 219 us: 1.02x slower                                                     |
| mdp                      | 2.49 sec                                                                    | 2.53 sec: 1.02x slower                                                   |
| tomli_loads              | 2.53 sec                                                                    | 2.58 sec: 1.02x slower                                                   |
| sympy_sum                | 151 ms                                                                      | 153 ms: 1.02x slower                                                     |
| logging_silent           | 99.5 ns                                                                     | 101 ns: 1.02x slower                                                     |
| chaos                    | 60.6 ms                                                                     | 61.8 ms: 1.02x slower                                                    |
| sqlglot_transpile        | 1.79 ms                                                                     | 1.83 ms: 1.02x slower                                                    |
| django_template          | 40.4 ms                                                                     | 41.2 ms: 1.02x slower                                                    |
| typing_runtime_protocols | 171 us                                                                      | 175 us: 1.02x slower                                                     |
| go                       | 133 ms                                                                      | 137 ms: 1.03x slower                                                     |
| create_gc_cycles         | 1.93 ms                                                                     | 1.99 ms: 1.03x slower                                                    |
| scimark_sor              | 115 ms                                                                      | 119 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult  | 4.16 ms                                                                     | 4.30 ms: 1.03x slower                                                    |
| pycparser                | 1.21 sec                                                                    | 1.25 sec: 1.03x slower                                                   |
| deepcopy_memo            | 28.8 us                                                                     | 29.9 us: 1.04x slower                                                    |
| scimark_fft              | 296 ms                                                                      | 313 ms: 1.06x slower                                                     |
| raytrace                 | 268 ms                                                                      | 285 ms: 1.06x slower                                                     |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (23): async_tree_none_tg, async_tree_io, tornado_http, bench_mp_pool, pprint_safe_repr, asyncio_tcp, hexiom, async_tree_memoization_tg, coroutines, asyncio_tcp_ssl, deltablue, xml_etree_iterparse, deepcopy_reduce, sqlglot_normalize, async_tree_memoization, async_tree_cpu_io_mixed_tg, pylint, async_tree_cpu_io_mixed, xml_etree_parse, async_tree_io_tg, async_tree_none, bench_thread_pool, regex_v8

# HPT report

- Reliability score: 97.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x