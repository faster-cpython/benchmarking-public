# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_100
- machine: linux-x86_64
- commit hash: 11fa189
- commit date: 2024-08-13
- overall geometric mean: 1.01x slower
- HPT reliability: 99.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                | 293 ms: 1.04x slower                                                    |
| docutils       | 2.99 sec                                                              | 2.87 sec: 1.04x faster                                                  |
| html5lib       | 66.6 ms                                                               | 65.3 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp            | 504 ms                                                                | 501 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                  |
| asyncio_websockets     | 555 ms                                                                | 559 ms: 1.01x slower                                                    |
| async_tree_none        | 331 ms                                                                | 335 ms: 1.01x slower                                                    |
| async_tree_memoization | 428 ms                                                                | 435 ms: 1.02x slower                                                    |
| coroutines             | 22.4 ms                                                               | 22.8 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_generators, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 188 ms: 1.01x slower                                                    |
| nbody          | 80.1 ms                                                               | 81.7 ms: 1.02x slower                                                   |
| float          | 70.4 ms                                                               | 74.0 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.56 ms                                                               | 3.49 ms: 1.02x faster                                                   |
| regex_dna      | 214 ms                                                                | 211 ms: 1.02x faster                                                    |
| regex_compile  | 143 ms                                                                | 142 ms: 1.01x faster                                                    |
| regex_v8       | 23.8 ms                                                               | 24.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 302 us                                                                | 304 us: 1.01x slower                                                    |
| unpickle_pure_python | 212 us                                                                | 214 us: 1.01x slower                                                    |
| json_dumps           | 10.4 ms                                                               | 10.6 ms: 1.02x slower                                                   |
| xml_etree_parse      | 147 ms                                                                | 153 ms: 1.05x slower                                                    |
| xml_etree_iterparse  | 97.6 ms                                                               | 103 ms: 1.05x slower                                                    |
| xml_etree_process    | 56.1 ms                                                               | 59.0 ms: 1.05x slower                                                   |
| xml_etree_generate   | 80.3 ms                                                               | 85.4 ms: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.09 ms: 1.00x faster                                                   |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 25.0 ms                                                               | 25.3 ms: 1.01x slower                                                   |
| mako           | 9.65 ms                                                               | 9.90 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal            | 3.81 ms                                                               | 3.51 ms: 1.09x faster                                                   |
| docutils                | 2.99 sec                                                              | 2.87 sec: 1.04x faster                                                  |
| sympy_sum               | 175 ms                                                                | 169 ms: 1.03x faster                                                    |
| logging_silent          | 103 ns                                                                | 99.7 ns: 1.03x faster                                                   |
| pprint_safe_repr        | 763 ms                                                                | 738 ms: 1.03x faster                                                    |
| telco                   | 7.92 ms                                                               | 7.75 ms: 1.02x faster                                                   |
| json                    | 5.37 ms                                                               | 5.25 ms: 1.02x faster                                                   |
| html5lib                | 66.6 ms                                                               | 65.3 ms: 1.02x faster                                                   |
| regex_effbot            | 3.56 ms                                                               | 3.49 ms: 1.02x faster                                                   |
| sympy_str               | 303 ms                                                                | 296 ms: 1.02x faster                                                    |
| sympy_integrate         | 23.0 ms                                                               | 22.7 ms: 1.02x faster                                                   |
| regex_dna               | 214 ms                                                                | 211 ms: 1.02x faster                                                    |
| deepcopy_memo           | 27.0 us                                                               | 26.6 us: 1.02x faster                                                   |
| create_gc_cycles        | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                   |
| regex_compile           | 143 ms                                                                | 142 ms: 1.01x faster                                                    |
| sympy_expand            | 509 ms                                                                | 505 ms: 1.01x faster                                                    |
| logging_simple          | 5.60 us                                                               | 5.56 us: 1.01x faster                                                   |
| pathlib                 | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                   |
| asyncio_tcp             | 504 ms                                                                | 501 ms: 1.01x faster                                                    |
| python_startup_no_site  | 7.12 ms                                                               | 7.09 ms: 1.00x faster                                                   |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| fannkuch                | 368 ms                                                                | 367 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                  |
| raytrace                | 268 ms                                                                | 269 ms: 1.01x slower                                                    |
| asyncio_websockets      | 555 ms                                                                | 559 ms: 1.01x slower                                                    |
| logging_format          | 6.10 us                                                               | 6.15 us: 1.01x slower                                                   |
| pickle_pure_python      | 302 us                                                                | 304 us: 1.01x slower                                                    |
| scimark_monte_carlo     | 62.0 ms                                                               | 62.6 ms: 1.01x slower                                                   |
| async_tree_none         | 331 ms                                                                | 335 ms: 1.01x slower                                                    |
| pidigits                | 185 ms                                                                | 188 ms: 1.01x slower                                                    |
| pycparser               | 1.15 sec                                                              | 1.16 sec: 1.01x slower                                                  |
| genshi_text             | 25.0 ms                                                               | 25.3 ms: 1.01x slower                                                   |
| scimark_lu              | 108 ms                                                                | 109 ms: 1.01x slower                                                    |
| unpickle_pure_python    | 212 us                                                                | 214 us: 1.01x slower                                                    |
| comprehensions          | 16.4 us                                                               | 16.6 us: 1.01x slower                                                   |
| crypto_pyaes            | 65.9 ms                                                               | 66.8 ms: 1.01x slower                                                   |
| deltablue               | 3.12 ms                                                               | 3.17 ms: 1.01x slower                                                   |
| async_tree_memoization  | 428 ms                                                                | 435 ms: 1.02x slower                                                    |
| json_dumps              | 10.4 ms                                                               | 10.6 ms: 1.02x slower                                                   |
| coroutines              | 22.4 ms                                                               | 22.8 ms: 1.02x slower                                                   |
| spectral_norm           | 98.2 ms                                                               | 99.9 ms: 1.02x slower                                                   |
| sqlglot_parse           | 1.32 ms                                                               | 1.35 ms: 1.02x slower                                                   |
| meteor_contest          | 104 ms                                                                | 106 ms: 1.02x slower                                                    |
| nqueens                 | 84.1 ms                                                               | 85.7 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 58.4 ms                                                               | 59.6 ms: 1.02x slower                                                   |
| mdp                     | 2.53 sec                                                              | 2.58 sec: 1.02x slower                                                  |
| nbody                   | 80.1 ms                                                               | 81.7 ms: 1.02x slower                                                   |
| sqlglot_transpile       | 1.68 ms                                                               | 1.72 ms: 1.02x slower                                                   |
| regex_v8                | 23.8 ms                                                               | 24.4 ms: 1.02x slower                                                   |
| richards                | 39.6 ms                                                               | 40.5 ms: 1.02x slower                                                   |
| mako                    | 9.65 ms                                                               | 9.90 ms: 1.03x slower                                                   |
| pyflate                 | 440 ms                                                                | 451 ms: 1.03x slower                                                    |
| pprint_pformat          | 1.54 sec                                                              | 1.58 sec: 1.03x slower                                                  |
| scimark_fft             | 307 ms                                                                | 318 ms: 1.04x slower                                                    |
| generators              | 33.5 ms                                                               | 34.8 ms: 1.04x slower                                                   |
| 2to3                    | 281 ms                                                                | 293 ms: 1.04x slower                                                    |
| xml_etree_parse         | 147 ms                                                                | 153 ms: 1.05x slower                                                    |
| xml_etree_iterparse     | 97.6 ms                                                               | 103 ms: 1.05x slower                                                    |
| float                   | 70.4 ms                                                               | 74.0 ms: 1.05x slower                                                   |
| xml_etree_process       | 56.1 ms                                                               | 59.0 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult | 4.27 ms                                                               | 4.54 ms: 1.06x slower                                                   |
| xml_etree_generate      | 80.3 ms                                                               | 85.4 ms: 1.06x slower                                                   |
| bpe_tokeniser           | 4.56 sec                                                              | 4.89 sec: 1.07x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (26): deepcopy_reduce, django_template, async_tree_memoization_tg, pylint, json_loads, tomli_loads, thrift, async_tree_none_tg, scimark_sor, typing_runtime_protocols, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_generators, tornado_http, bench_mp_pool, go, sqlglot_normalize, genshi_xml, chaos, hexiom, bench_thread_pool, deepcopy, richards_super, async_tree_io, coverage

# HPT report

- Reliability score: 99.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x