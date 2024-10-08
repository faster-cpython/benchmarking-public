# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 8dab2c9
- commit date: 2024-08-13
- overall geometric mean: 1.00x slower
- HPT reliability: 92.37%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                | 284 ms: 1.01x slower                                                  |
| docutils       | 2.99 sec                                                              | 2.98 sec: 1.01x faster                                                |
| html5lib       | 66.6 ms                                                               | 67.4 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators | 456 ms                                                                | 447 ms: 1.02x faster                                                  |
| asyncio_tcp      | 504 ms                                                                | 503 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                |
| coroutines       | 22.4 ms                                                               | 22.7 ms: 1.01x slower                                                 |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_io, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 73.9 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                                | 142 ms: 1.01x faster                                                  |
| regex_v8       | 23.8 ms                                                               | 24.0 ms: 1.01x slower                                                 |
| regex_effbot   | 3.56 ms                                                               | 3.59 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.4 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| pickle_pure_python   | 302 us                                                                | 305 us: 1.01x slower                                                  |
| unpickle_pure_python | 212 us                                                                | 214 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 97.6 ms                                                               | 101 ms: 1.04x slower                                                  |
| xml_etree_parse      | 147 ms                                                                | 153 ms: 1.04x slower                                                  |
| xml_etree_process    | 56.1 ms                                                               | 58.8 ms: 1.05x slower                                                 |
| xml_etree_generate   | 80.3 ms                                                               | 84.9 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.09 ms: 1.00x faster                                                 |
| python_startup         | 10.5 ms                                                               | 10.4 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                               | 25.2 ms: 1.01x slower                                                 |
| mako            | 9.65 ms                                                               | 9.87 ms: 1.02x slower                                                 |
| django_template | 35.7 ms                                                               | 37.0 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal             | 3.81 ms                                                               | 3.48 ms: 1.09x faster                                                 |
| sympy_sum                | 175 ms                                                                | 170 ms: 1.03x faster                                                  |
| pprint_safe_repr         | 763 ms                                                                | 745 ms: 1.02x faster                                                  |
| sympy_str                | 303 ms                                                                | 296 ms: 1.02x faster                                                  |
| async_generators         | 456 ms                                                                | 447 ms: 1.02x faster                                                  |
| telco                    | 7.92 ms                                                               | 7.82 ms: 1.01x faster                                                 |
| pyflate                  | 440 ms                                                                | 434 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.76 ms                                                               | 1.73 ms: 1.01x faster                                                 |
| json_loads               | 28.7 us                                                               | 28.4 us: 1.01x faster                                                 |
| deepcopy_reduce          | 2.68 us                                                               | 2.65 us: 1.01x faster                                                 |
| logging_simple           | 5.60 us                                                               | 5.54 us: 1.01x faster                                                 |
| sympy_integrate          | 23.0 ms                                                               | 22.8 ms: 1.01x faster                                                 |
| regex_compile            | 143 ms                                                                | 142 ms: 1.01x faster                                                  |
| sympy_expand             | 509 ms                                                                | 505 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult  | 4.27 ms                                                               | 4.23 ms: 1.01x faster                                                 |
| sqlglot_normalize        | 114 ms                                                                | 113 ms: 1.01x faster                                                  |
| docutils                 | 2.99 sec                                                              | 2.98 sec: 1.01x faster                                                |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| logging_silent           | 103 ns                                                                | 103 ns: 1.00x faster                                                  |
| python_startup_no_site   | 7.12 ms                                                               | 7.09 ms: 1.00x faster                                                 |
| richards_super           | 45.8 ms                                                               | 45.6 ms: 1.00x faster                                                 |
| python_startup           | 10.5 ms                                                               | 10.4 ms: 1.00x faster                                                 |
| asyncio_tcp              | 504 ms                                                                | 503 ms: 1.00x faster                                                  |
| scimark_fft              | 307 ms                                                                | 306 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                |
| go                       | 148 ms                                                                | 148 ms: 1.00x slower                                                  |
| deltablue                | 3.12 ms                                                               | 3.13 ms: 1.00x slower                                                 |
| regex_v8                 | 23.8 ms                                                               | 24.0 ms: 1.01x slower                                                 |
| sqlglot_parse            | 1.32 ms                                                               | 1.33 ms: 1.01x slower                                                 |
| thrift                   | 790 us                                                                | 795 us: 1.01x slower                                                  |
| comprehensions           | 16.4 us                                                               | 16.5 us: 1.01x slower                                                 |
| raytrace                 | 268 ms                                                                | 270 ms: 1.01x slower                                                  |
| scimark_monte_carlo      | 62.0 ms                                                               | 62.6 ms: 1.01x slower                                                 |
| genshi_text              | 25.0 ms                                                               | 25.2 ms: 1.01x slower                                                 |
| pickle_pure_python       | 302 us                                                                | 305 us: 1.01x slower                                                  |
| regex_effbot             | 3.56 ms                                                               | 3.59 ms: 1.01x slower                                                 |
| html5lib                 | 66.6 ms                                                               | 67.4 ms: 1.01x slower                                                 |
| unpickle_pure_python     | 212 us                                                                | 214 us: 1.01x slower                                                  |
| mdp                      | 2.53 sec                                                              | 2.56 sec: 1.01x slower                                                |
| typing_runtime_protocols | 170 us                                                                | 172 us: 1.01x slower                                                  |
| pprint_pformat           | 1.54 sec                                                              | 1.56 sec: 1.01x slower                                                |
| 2to3                     | 281 ms                                                                | 284 ms: 1.01x slower                                                  |
| pycparser                | 1.15 sec                                                              | 1.17 sec: 1.01x slower                                                |
| coroutines               | 22.4 ms                                                               | 22.7 ms: 1.01x slower                                                 |
| scimark_lu               | 108 ms                                                                | 110 ms: 1.02x slower                                                  |
| deepcopy                 | 265 us                                                                | 269 us: 1.02x slower                                                  |
| crypto_pyaes             | 65.9 ms                                                               | 67.3 ms: 1.02x slower                                                 |
| mako                     | 9.65 ms                                                               | 9.87 ms: 1.02x slower                                                 |
| richards                 | 39.6 ms                                                               | 40.5 ms: 1.02x slower                                                 |
| json                     | 5.37 ms                                                               | 5.50 ms: 1.02x slower                                                 |
| spectral_norm            | 98.2 ms                                                               | 101 ms: 1.03x slower                                                  |
| django_template          | 35.7 ms                                                               | 37.0 ms: 1.03x slower                                                 |
| xml_etree_iterparse      | 97.6 ms                                                               | 101 ms: 1.04x slower                                                  |
| xml_etree_parse          | 147 ms                                                                | 153 ms: 1.04x slower                                                  |
| nqueens                  | 84.1 ms                                                               | 87.8 ms: 1.04x slower                                                 |
| xml_etree_process        | 56.1 ms                                                               | 58.8 ms: 1.05x slower                                                 |
| float                    | 70.4 ms                                                               | 73.9 ms: 1.05x slower                                                 |
| xml_etree_generate       | 80.3 ms                                                               | 84.9 ms: 1.06x slower                                                 |
| generators               | 33.5 ms                                                               | 35.4 ms: 1.06x slower                                                 |
| bpe_tokeniser            | 4.56 sec                                                              | 4.86 sec: 1.07x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (29): async_tree_memoization_tg, pylint, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, coverage, pathlib, meteor_contest, sqlglot_optimize, nbody, async_tree_none_tg, logging_format, tomli_loads, chaos, async_tree_none, tornado_http, bench_mp_pool, pidigits, async_tree_io, hexiom, bench_thread_pool, asyncio_websockets, scimark_sor, fannkuch, sqlglot_transpile, regex_dna, genshi_xml, async_tree_memoization, deepcopy_memo

# HPT report

- Reliability score: 92.37% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x