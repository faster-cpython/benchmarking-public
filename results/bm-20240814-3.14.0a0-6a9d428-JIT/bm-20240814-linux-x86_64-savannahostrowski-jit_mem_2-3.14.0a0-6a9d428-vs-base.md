# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 6a9d428
- commit date: 2024-08-14
- overall geometric mean: 1.00x slower
- HPT reliability: 94.19%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                | 282 ms: 1.01x slower                                                  |
| docutils       | 2.99 sec                                                              | 2.96 sec: 1.01x faster                                                |
| html5lib       | 66.6 ms                                                               | 67.0 ms: 1.01x slower                                                 |
| tornado_http   | 94.2 ms                                                               | 94.5 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp     | 504 ms                                                                | 493 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                |
| coroutines      | 22.4 ms                                                               | 22.9 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, async_tree_io, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                  |
| float          | 70.4 ms                                                               | 71.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                                | 142 ms: 1.01x faster                                                  |
| regex_v8       | 23.8 ms                                                               | 24.3 ms: 1.02x slower                                                 |
| regex_dna      | 214 ms                                                                | 220 ms: 1.03x slower                                                  |
| regex_effbot   | 3.56 ms                                                               | 3.69 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 302 us                                                                | 298 us: 1.01x faster                                                  |
| json_loads           | 28.7 us                                                               | 28.6 us: 1.00x faster                                                 |
| unpickle_pure_python | 212 us                                                                | 211 us: 1.00x faster                                                  |
| xml_etree_iterparse  | 97.6 ms                                                               | 98.7 ms: 1.01x slower                                                 |
| tomli_loads          | 1.90 sec                                                              | 1.94 sec: 1.02x slower                                                |
| xml_etree_process    | 56.1 ms                                                               | 58.7 ms: 1.05x slower                                                 |
| xml_etree_generate   | 80.3 ms                                                               | 85.3 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.08 ms: 1.01x faster                                                 |
| python_startup         | 10.5 ms                                                               | 10.4 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 25.0 ms                                                               | 24.6 ms: 1.02x faster                                                 |
| django_template | 35.7 ms                                                               | 36.8 ms: 1.03x slower                                                 |
| mako            | 9.65 ms                                                               | 10.0 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal           | 3.81 ms                                                               | 3.51 ms: 1.09x faster                                                 |
| pprint_safe_repr       | 763 ms                                                                | 729 ms: 1.05x faster                                                  |
| sympy_sum              | 175 ms                                                                | 171 ms: 1.03x faster                                                  |
| asyncio_tcp            | 504 ms                                                                | 493 ms: 1.02x faster                                                  |
| sympy_str              | 303 ms                                                                | 296 ms: 1.02x faster                                                  |
| go                     | 148 ms                                                                | 145 ms: 1.02x faster                                                  |
| genshi_text            | 25.0 ms                                                               | 24.6 ms: 1.02x faster                                                 |
| sympy_expand           | 509 ms                                                                | 501 ms: 1.02x faster                                                  |
| create_gc_cycles       | 1.76 ms                                                               | 1.73 ms: 1.02x faster                                                 |
| pprint_pformat         | 1.54 sec                                                              | 1.51 sec: 1.02x faster                                                |
| sympy_integrate        | 23.0 ms                                                               | 22.7 ms: 1.01x faster                                                 |
| raytrace               | 268 ms                                                                | 264 ms: 1.01x faster                                                  |
| pickle_pure_python     | 302 us                                                                | 298 us: 1.01x faster                                                  |
| sqlglot_normalize      | 114 ms                                                                | 113 ms: 1.01x faster                                                  |
| docutils               | 2.99 sec                                                              | 2.96 sec: 1.01x faster                                                |
| regex_compile          | 143 ms                                                                | 142 ms: 1.01x faster                                                  |
| json                   | 5.37 ms                                                               | 5.33 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.12 ms                                                               | 7.08 ms: 1.01x faster                                                 |
| python_startup         | 10.5 ms                                                               | 10.4 ms: 1.00x faster                                                 |
| json_loads             | 28.7 us                                                               | 28.6 us: 1.00x faster                                                 |
| scimark_fft            | 307 ms                                                                | 305 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                |
| deltablue              | 3.12 ms                                                               | 3.11 ms: 1.00x faster                                                 |
| unpickle_pure_python   | 212 us                                                                | 211 us: 1.00x faster                                                  |
| pidigits               | 185 ms                                                                | 185 ms: 1.00x faster                                                  |
| tornado_http           | 94.2 ms                                                               | 94.5 ms: 1.00x slower                                                 |
| 2to3                   | 281 ms                                                                | 282 ms: 1.01x slower                                                  |
| html5lib               | 66.6 ms                                                               | 67.0 ms: 1.01x slower                                                 |
| richards_super         | 45.8 ms                                                               | 46.1 ms: 1.01x slower                                                 |
| mdp                    | 2.53 sec                                                              | 2.55 sec: 1.01x slower                                                |
| fannkuch               | 368 ms                                                                | 371 ms: 1.01x slower                                                  |
| sqlglot_transpile      | 1.68 ms                                                               | 1.70 ms: 1.01x slower                                                 |
| hexiom                 | 6.79 ms                                                               | 6.86 ms: 1.01x slower                                                 |
| spectral_norm          | 98.2 ms                                                               | 99.2 ms: 1.01x slower                                                 |
| xml_etree_iterparse    | 97.6 ms                                                               | 98.7 ms: 1.01x slower                                                 |
| comprehensions         | 16.4 us                                                               | 16.6 us: 1.01x slower                                                 |
| meteor_contest         | 104 ms                                                                | 106 ms: 1.01x slower                                                  |
| logging_format         | 6.10 us                                                               | 6.21 us: 1.02x slower                                                 |
| float                  | 70.4 ms                                                               | 71.7 ms: 1.02x slower                                                 |
| regex_v8               | 23.8 ms                                                               | 24.3 ms: 1.02x slower                                                 |
| scimark_lu             | 108 ms                                                                | 110 ms: 1.02x slower                                                  |
| tomli_loads            | 1.90 sec                                                              | 1.94 sec: 1.02x slower                                                |
| coroutines             | 22.4 ms                                                               | 22.9 ms: 1.02x slower                                                 |
| scimark_sor            | 115 ms                                                                | 118 ms: 1.02x slower                                                  |
| pyflate                | 440 ms                                                                | 451 ms: 1.03x slower                                                  |
| regex_dna              | 214 ms                                                                | 220 ms: 1.03x slower                                                  |
| django_template        | 35.7 ms                                                               | 36.8 ms: 1.03x slower                                                 |
| generators             | 33.5 ms                                                               | 34.6 ms: 1.03x slower                                                 |
| richards               | 39.6 ms                                                               | 41.1 ms: 1.04x slower                                                 |
| regex_effbot           | 3.56 ms                                                               | 3.69 ms: 1.04x slower                                                 |
| mako                   | 9.65 ms                                                               | 10.0 ms: 1.04x slower                                                 |
| crypto_pyaes           | 65.9 ms                                                               | 68.6 ms: 1.04x slower                                                 |
| nqueens                | 84.1 ms                                                               | 87.7 ms: 1.04x slower                                                 |
| pycparser              | 1.15 sec                                                              | 1.20 sec: 1.04x slower                                                |
| xml_etree_process      | 56.1 ms                                                               | 58.7 ms: 1.05x slower                                                 |
| xml_etree_generate     | 80.3 ms                                                               | 85.3 ms: 1.06x slower                                                 |
| bpe_tokeniser          | 4.56 sec                                                              | 4.90 sec: 1.08x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (32): pylint, telco, async_tree_memoization_tg, scimark_sparse_mat_mult, deepcopy, chaos, json_dumps, async_tree_none_tg, logging_silent, thrift, async_tree_none, async_tree_cpu_io_mixed_tg, pathlib, async_tree_cpu_io_mixed, deepcopy_memo, genshi_xml, coverage, typing_runtime_protocols, bench_mp_pool, scimark_monte_carlo, sqlglot_optimize, asyncio_websockets, bench_thread_pool, async_generators, nbody, logging_simple, xml_etree_parse, async_tree_io, sqlglot_parse, async_tree_io_tg, deepcopy_reduce, async_tree_memoization

# HPT report

- Reliability score: 94.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x