# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 0e340e1
- commit date: 2024-08-26
- overall geometric mean: 1.02x slower
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 283 ms: 1.03x slower                                             |
| docutils       | 3.04 sec                                                              | 3.34 sec: 1.10x slower                                           |
| html5lib       | 63.4 ms                                                               | 70.6 ms: 1.11x slower                                            |
| tornado_http   | 94.7 ms                                                               | 102 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| coroutines             | 23.0 ms                                                               | 22.7 ms: 1.02x faster                                            |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                           |
| async_generators       | 454 ms                                                                | 456 ms: 1.01x slower                                             |
| async_tree_io          | 924 ms                                                                | 941 ms: 1.02x slower                                             |
| asyncio_tcp            | 499 ms                                                                | 514 ms: 1.03x slower                                             |
| async_tree_memoization | 395 ms                                                                | 414 ms: 1.05x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 82.0 ms                                                               | 79.6 ms: 1.03x faster                                            |
| pidigits       | 187 ms                                                                | 185 ms: 1.01x faster                                             |
| float          | 70.4 ms                                                               | 71.0 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                               | 24.2 ms: 1.01x slower                                            |
| regex_effbot   | 3.51 ms                                                               | 3.60 ms: 1.03x slower                                            |
| regex_dna      | 210 ms                                                                | 216 ms: 1.03x slower                                             |
| regex_compile  | 142 ms                                                                | 150 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 198 us: 1.08x faster                                             |
| xml_etree_generate   | 77.7 ms                                                               | 77.0 ms: 1.01x faster                                            |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.8 ms: 1.01x slower                                            |
| pickle_pure_python   | 302 us                                                                | 310 us: 1.03x slower                                             |
| json_loads           | 28.6 us                                                               | 29.6 us: 1.04x slower                                            |
| tomli_loads          | 1.92 sec                                                              | 2.05 sec: 1.07x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                            |
| python_startup_no_site | 7.14 ms                                                               | 7.16 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 24.3 ms: 1.06x faster                                            |
| mako            | 9.79 ms                                                               | 9.61 ms: 1.02x faster                                            |
| django_template | 35.6 ms                                                               | 38.3 ms: 1.08x slower                                            |
| genshi_xml      | 59.0 ms                                                               | 65.0 ms: 1.10x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                     |

All benchmarks:
===============

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python   | 213 us                                                                | 198 us: 1.08x faster                                             |
| genshi_text            | 25.7 ms                                                               | 24.3 ms: 1.06x faster                                            |
| scimark_monte_carlo    | 62.5 ms                                                               | 59.1 ms: 1.06x faster                                            |
| richards_super         | 45.0 ms                                                               | 43.1 ms: 1.04x faster                                            |
| nbody                  | 82.0 ms                                                               | 79.6 ms: 1.03x faster                                            |
| nqueens                | 85.7 ms                                                               | 83.7 ms: 1.02x faster                                            |
| pyflate                | 450 ms                                                                | 440 ms: 1.02x faster                                             |
| mako                   | 9.79 ms                                                               | 9.61 ms: 1.02x faster                                            |
| logging_silent         | 103 ns                                                                | 101 ns: 1.02x faster                                             |
| coroutines             | 23.0 ms                                                               | 22.7 ms: 1.02x faster                                            |
| scimark_fft            | 314 ms                                                                | 310 ms: 1.01x faster                                             |
| richards               | 38.6 ms                                                               | 38.1 ms: 1.01x faster                                            |
| deepcopy_memo          | 27.0 us                                                               | 26.6 us: 1.01x faster                                            |
| json                   | 5.32 ms                                                               | 5.26 ms: 1.01x faster                                            |
| fannkuch               | 372 ms                                                                | 367 ms: 1.01x faster                                             |
| pidigits               | 187 ms                                                                | 185 ms: 1.01x faster                                             |
| crypto_pyaes           | 66.6 ms                                                               | 65.9 ms: 1.01x faster                                            |
| hexiom                 | 6.89 ms                                                               | 6.82 ms: 1.01x faster                                            |
| meteor_contest         | 106 ms                                                                | 105 ms: 1.01x faster                                             |
| xml_etree_generate     | 77.7 ms                                                               | 77.0 ms: 1.01x faster                                            |
| deepcopy               | 265 us                                                                | 263 us: 1.01x faster                                             |
| spectral_norm          | 101 ms                                                                | 101 ms: 1.01x faster                                             |
| mdp                    | 2.56 sec                                                              | 2.55 sec: 1.00x faster                                           |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                            |
| python_startup_no_site | 7.14 ms                                                               | 7.16 ms: 1.00x slower                                            |
| async_generators       | 454 ms                                                                | 456 ms: 1.01x slower                                             |
| float                  | 70.4 ms                                                               | 71.0 ms: 1.01x slower                                            |
| bench_thread_pool      | 817 us                                                                | 825 us: 1.01x slower                                             |
| xml_etree_iterparse    | 97.7 ms                                                               | 98.8 ms: 1.01x slower                                            |
| generators             | 33.3 ms                                                               | 33.7 ms: 1.01x slower                                            |
| regex_v8               | 23.9 ms                                                               | 24.2 ms: 1.01x slower                                            |
| coverage               | 85.6 ms                                                               | 86.9 ms: 1.01x slower                                            |
| create_gc_cycles       | 1.75 ms                                                               | 1.78 ms: 1.02x slower                                            |
| async_tree_io          | 924 ms                                                                | 941 ms: 1.02x slower                                             |
| regex_effbot           | 3.51 ms                                                               | 3.60 ms: 1.03x slower                                            |
| 2to3                   | 276 ms                                                                | 283 ms: 1.03x slower                                             |
| deltablue              | 3.18 ms                                                               | 3.27 ms: 1.03x slower                                            |
| pickle_pure_python     | 302 us                                                                | 310 us: 1.03x slower                                             |
| regex_dna              | 210 ms                                                                | 216 ms: 1.03x slower                                             |
| asyncio_tcp            | 499 ms                                                                | 514 ms: 1.03x slower                                             |
| json_loads             | 28.6 us                                                               | 29.6 us: 1.04x slower                                            |
| sqlglot_optimize       | 58.1 ms                                                               | 60.4 ms: 1.04x slower                                            |
| pycparser              | 1.18 sec                                                              | 1.23 sec: 1.05x slower                                           |
| async_tree_memoization | 395 ms                                                                | 414 ms: 1.05x slower                                             |
| scimark_lu             | 109 ms                                                                | 114 ms: 1.05x slower                                             |
| logging_simple         | 5.54 us                                                               | 5.84 us: 1.05x slower                                            |
| gc_traversal           | 3.58 ms                                                               | 3.78 ms: 1.05x slower                                            |
| regex_compile          | 142 ms                                                                | 150 ms: 1.06x slower                                             |
| sympy_expand           | 504 ms                                                                | 536 ms: 1.06x slower                                             |
| tomli_loads            | 1.92 sec                                                              | 2.05 sec: 1.07x slower                                           |
| sqlglot_transpile      | 1.69 ms                                                               | 1.80 ms: 1.07x slower                                            |
| scimark_sor            | 116 ms                                                                | 124 ms: 1.07x slower                                             |
| sqlglot_normalize      | 113 ms                                                                | 121 ms: 1.07x slower                                             |
| sympy_str              | 299 ms                                                                | 321 ms: 1.08x slower                                             |
| logging_format         | 6.04 us                                                               | 6.51 us: 1.08x slower                                            |
| django_template        | 35.6 ms                                                               | 38.3 ms: 1.08x slower                                            |
| tornado_http           | 94.7 ms                                                               | 102 ms: 1.08x slower                                             |
| sympy_integrate        | 22.8 ms                                                               | 25.0 ms: 1.10x slower                                            |
| docutils               | 3.04 sec                                                              | 3.34 sec: 1.10x slower                                           |
| genshi_xml             | 59.0 ms                                                               | 65.0 ms: 1.10x slower                                            |
| html5lib               | 63.4 ms                                                               | 70.6 ms: 1.11x slower                                            |
| pylint                 | 372 ms                                                                | 415 ms: 1.12x slower                                             |
| sympy_sum              | 171 ms                                                                | 192 ms: 1.12x slower                                             |
| sqlglot_parse          | 1.34 ms                                                               | 1.51 ms: 1.13x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (24): typing_runtime_protocols, pprint_safe_repr, scimark_sparse_mat_mult, chaos, xml_etree_process, comprehensions, xml_etree_parse, pprint_pformat, deepcopy_reduce, async_tree_cpu_io_mixed_tg, go, asyncio_websockets, async_tree_cpu_io_mixed, bench_mp_pool, json_dumps, thrift, pathlib, raytrace, bpe_tokeniser, telco, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

# HPT report

- Reliability score: 98.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x