# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_gc_old
- machine: linux-x86_64
- commit hash: 1268c80
- commit date: 2024-08-19
- overall geometric mean: 1.00x faster
- HPT reliability: 89.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                | 281 ms: 1.00x slower                                                       |
| html5lib       | 67.2 ms                                                               | 64.2 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                               | 23.1 ms: 1.01x faster                                                      |
| asyncio_tcp      | 499 ms                                                                | 493 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.80 sec: 1.01x faster                                                     |
| async_generators | 452 ms                                                                | 457 ms: 1.01x slower                                                       |
| async_tree_none  | 323 ms                                                                | 329 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                       |
| nbody          | 80.0 ms                                                               | 83.4 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                | 212 ms: 1.04x faster                                                       |
| regex_effbot   | 3.75 ms                                                               | 3.59 ms: 1.04x faster                                                      |
| regex_v8       | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.93 sec                                                              | 1.90 sec: 1.02x faster                                                     |
| xml_etree_process    | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 98.4 ms                                                               | 98.2 ms: 1.00x faster                                                      |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.00x slower                                                      |
| pickle_pure_python   | 302 us                                                                | 304 us: 1.01x slower                                                       |
| unpickle_pure_python | 212 us                                                                | 215 us: 1.01x slower                                                       |
| json_loads           | 28.6 us                                                               | 29.0 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 36.8 ms                                                               | 35.8 ms: 1.03x faster                                                      |
| genshi_text     | 26.6 ms                                                               | 25.9 ms: 1.03x faster                                                      |
| mako            | 9.98 ms                                                               | 10.0 ms: 1.00x slower                                                      |
| genshi_xml      | 59.9 ms                                                               | 61.2 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| html5lib                 | 67.2 ms                                                               | 64.2 ms: 1.05x faster                                                      |
| regex_dna                | 221 ms                                                                | 212 ms: 1.04x faster                                                       |
| regex_effbot             | 3.75 ms                                                               | 3.59 ms: 1.04x faster                                                      |
| spectral_norm            | 102 ms                                                                | 99.3 ms: 1.03x faster                                                      |
| django_template          | 36.8 ms                                                               | 35.8 ms: 1.03x faster                                                      |
| genshi_text              | 26.6 ms                                                               | 25.9 ms: 1.03x faster                                                      |
| scimark_monte_carlo      | 63.6 ms                                                               | 61.9 ms: 1.03x faster                                                      |
| coverage                 | 87.5 ms                                                               | 85.4 ms: 1.02x faster                                                      |
| thrift                   | 797 us                                                                | 782 us: 1.02x faster                                                       |
| tomli_loads              | 1.93 sec                                                              | 1.90 sec: 1.02x faster                                                     |
| scimark_fft              | 308 ms                                                                | 303 ms: 1.02x faster                                                       |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.02x faster                                                       |
| pprint_safe_repr         | 743 ms                                                                | 732 ms: 1.02x faster                                                       |
| coroutines               | 23.4 ms                                                               | 23.1 ms: 1.01x faster                                                      |
| richards                 | 39.4 ms                                                               | 39.0 ms: 1.01x faster                                                      |
| typing_runtime_protocols | 174 us                                                                | 172 us: 1.01x faster                                                       |
| pprint_pformat           | 1.54 sec                                                              | 1.53 sec: 1.01x faster                                                     |
| asyncio_tcp              | 499 ms                                                                | 493 ms: 1.01x faster                                                       |
| deepcopy_memo            | 27.0 us                                                               | 26.7 us: 1.01x faster                                                      |
| crypto_pyaes             | 66.4 ms                                                               | 65.8 ms: 1.01x faster                                                      |
| bpe_tokeniser            | 4.59 sec                                                              | 4.55 sec: 1.01x faster                                                     |
| regex_v8                 | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                      |
| xml_etree_process        | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.01x faster                                                     |
| create_gc_cycles         | 1.75 ms                                                               | 1.74 ms: 1.00x faster                                                      |
| xml_etree_iterparse      | 98.4 ms                                                               | 98.2 ms: 1.00x faster                                                      |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                      |
| mako                     | 9.98 ms                                                               | 10.0 ms: 1.00x slower                                                      |
| sqlglot_optimize         | 57.8 ms                                                               | 57.9 ms: 1.00x slower                                                      |
| bench_thread_pool        | 817 us                                                                | 819 us: 1.00x slower                                                       |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                       |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.00x slower                                                      |
| sympy_expand             | 506 ms                                                                | 508 ms: 1.00x slower                                                       |
| sqlglot_transpile        | 1.68 ms                                                               | 1.69 ms: 1.00x slower                                                      |
| 2to3                     | 279 ms                                                                | 281 ms: 1.00x slower                                                       |
| pyflate                  | 445 ms                                                                | 447 ms: 1.01x slower                                                       |
| logging_format           | 6.00 us                                                               | 6.03 us: 1.01x slower                                                      |
| sympy_integrate          | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                      |
| pickle_pure_python       | 302 us                                                                | 304 us: 1.01x slower                                                       |
| scimark_sor              | 114 ms                                                                | 115 ms: 1.01x slower                                                       |
| sympy_str                | 301 ms                                                                | 303 ms: 1.01x slower                                                       |
| telco                    | 7.76 ms                                                               | 7.82 ms: 1.01x slower                                                      |
| raytrace                 | 264 ms                                                                | 266 ms: 1.01x slower                                                       |
| go                       | 145 ms                                                                | 146 ms: 1.01x slower                                                       |
| sqlglot_normalize        | 113 ms                                                                | 114 ms: 1.01x slower                                                       |
| sympy_sum                | 175 ms                                                                | 177 ms: 1.01x slower                                                       |
| hexiom                   | 6.81 ms                                                               | 6.87 ms: 1.01x slower                                                      |
| async_generators         | 452 ms                                                                | 457 ms: 1.01x slower                                                       |
| logging_simple           | 5.47 us                                                               | 5.53 us: 1.01x slower                                                      |
| deltablue                | 3.11 ms                                                               | 3.15 ms: 1.01x slower                                                      |
| gc_traversal             | 3.67 ms                                                               | 3.72 ms: 1.01x slower                                                      |
| unpickle_pure_python     | 212 us                                                                | 215 us: 1.01x slower                                                       |
| json_loads               | 28.6 us                                                               | 29.0 us: 1.01x slower                                                      |
| async_tree_none          | 323 ms                                                                | 329 ms: 1.02x slower                                                       |
| deepcopy_reduce          | 2.64 us                                                               | 2.69 us: 1.02x slower                                                      |
| deepcopy                 | 263 us                                                                | 268 us: 1.02x slower                                                       |
| genshi_xml               | 59.9 ms                                                               | 61.2 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 4.31 ms                                                               | 4.40 ms: 1.02x slower                                                      |
| nqueens                  | 85.2 ms                                                               | 87.7 ms: 1.03x slower                                                      |
| generators               | 32.6 ms                                                               | 33.5 ms: 1.03x slower                                                      |
| nbody                    | 80.0 ms                                                               | 83.4 ms: 1.04x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (28): xml_etree_parse, async_tree_io, logging_silent, scimark_lu, async_tree_cpu_io_mixed_tg, pycparser, async_tree_memoization, comprehensions, pathlib, docutils, tornado_http, async_tree_cpu_io_mixed, bench_mp_pool, regex_compile, python_startup_no_site, mdp, pylint, asyncio_websockets, async_tree_io_tg, xml_etree_generate, chaos, float, richards_super, fannkuch, sqlglot_parse, json, async_tree_none_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 89.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x