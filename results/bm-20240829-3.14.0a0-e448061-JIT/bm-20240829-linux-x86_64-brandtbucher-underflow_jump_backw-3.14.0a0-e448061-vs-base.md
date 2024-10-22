# Results vs. base

- fork: brandtbucher
- ref: underflow_jump_backw
- machine: linux-x86_64
- commit hash: e448061
- commit date: 2024-08-29
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 290 ms: 1.05x slower                                                        |
| docutils       | 3.04 sec                                                              | 3.58 sec: 1.18x slower                                                      |
| html5lib       | 63.4 ms                                                               | 75.5 ms: 1.19x slower                                                       |
| tornado_http   | 94.7 ms                                                               | 120 ms: 1.26x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 556 ms                                                                | 559 ms: 1.01x slower                                                        |
| async_generators           | 454 ms                                                                | 457 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 541 ms                                                                | 558 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed    | 561 ms                                                                | 581 ms: 1.04x slower                                                        |
| coroutines                 | 23.0 ms                                                               | 24.0 ms: 1.04x slower                                                       |
| async_tree_none_tg         | 307 ms                                                                | 321 ms: 1.04x slower                                                        |
| async_tree_io              | 924 ms                                                                | 966 ms: 1.05x slower                                                        |
| asyncio_tcp                | 499 ms                                                                | 531 ms: 1.06x slower                                                        |
| async_tree_none            | 325 ms                                                                | 347 ms: 1.07x slower                                                        |
| async_tree_memoization     | 395 ms                                                                | 437 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                                |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 82.0 ms                                                               | 80.3 ms: 1.02x faster                                                       |
| pidigits       | 187 ms                                                                | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 147 ms: 1.04x slower                                                        |
| regex_dna      | 210 ms                                                                | 221 ms: 1.05x slower                                                        |
| regex_v8       | 23.9 ms                                                               | 25.5 ms: 1.07x slower                                                       |
| regex_effbot   | 3.51 ms                                                               | 3.79 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 302 us                                                                | 288 us: 1.05x faster                                                        |
| json_loads           | 28.6 us                                                               | 28.3 us: 1.01x faster                                                       |
| unpickle_pure_python | 213 us                                                                | 211 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.2 ms: 1.01x slower                                                       |
| xml_etree_process    | 54.7 ms                                                               | 57.2 ms: 1.05x slower                                                       |
| xml_etree_generate   | 77.7 ms                                                               | 81.4 ms: 1.05x slower                                                       |
| tomli_loads          | 1.92 sec                                                              | 2.18 sec: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.19 ms: 1.01x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 24.3 ms: 1.06x faster                                                       |
| mako            | 9.79 ms                                                               | 10.3 ms: 1.06x slower                                                       |
| genshi_xml      | 59.0 ms                                                               | 67.5 ms: 1.14x slower                                                       |
| django_template | 35.6 ms                                                               | 42.1 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.08x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_monte_carlo        | 62.5 ms                                                               | 58.9 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 728 ms                                                                | 688 ms: 1.06x faster                                                        |
| genshi_text                | 25.7 ms                                                               | 24.3 ms: 1.06x faster                                                       |
| pickle_pure_python         | 302 us                                                                | 288 us: 1.05x faster                                                        |
| scimark_fft                | 314 ms                                                                | 301 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.49 sec                                                              | 1.44 sec: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 4.47 ms                                                               | 4.34 ms: 1.03x faster                                                       |
| json                       | 5.32 ms                                                               | 5.18 ms: 1.03x faster                                                       |
| nbody                      | 82.0 ms                                                               | 80.3 ms: 1.02x faster                                                       |
| crypto_pyaes               | 66.6 ms                                                               | 65.7 ms: 1.01x faster                                                       |
| typing_runtime_protocols   | 165 us                                                                | 163 us: 1.01x faster                                                        |
| pyflate                    | 450 ms                                                                | 445 ms: 1.01x faster                                                        |
| json_loads                 | 28.6 us                                                               | 28.3 us: 1.01x faster                                                       |
| unpickle_pure_python       | 213 us                                                                | 211 us: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                                | 186 ms: 1.01x faster                                                        |
| fannkuch                   | 372 ms                                                                | 373 ms: 1.00x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                               | 24.1 ms: 1.00x slower                                                       |
| asyncio_websockets         | 556 ms                                                                | 559 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 97.7 ms                                                               | 98.2 ms: 1.01x slower                                                       |
| async_generators           | 454 ms                                                                | 457 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.14 ms                                                               | 7.19 ms: 1.01x slower                                                       |
| nqueens                    | 85.7 ms                                                               | 86.6 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                      |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| bpe_tokeniser              | 4.43 sec                                                              | 4.49 sec: 1.01x slower                                                      |
| coverage                   | 85.6 ms                                                               | 87.4 ms: 1.02x slower                                                       |
| deepcopy                   | 265 us                                                                | 272 us: 1.02x slower                                                        |
| raytrace                   | 276 ms                                                                | 284 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed_tg | 541 ms                                                                | 558 ms: 1.03x slower                                                        |
| comprehensions             | 16.7 us                                                               | 17.3 us: 1.03x slower                                                       |
| create_gc_cycles           | 1.75 ms                                                               | 1.81 ms: 1.03x slower                                                       |
| regex_compile              | 142 ms                                                                | 147 ms: 1.04x slower                                                        |
| generators                 | 33.3 ms                                                               | 34.5 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed    | 561 ms                                                                | 581 ms: 1.04x slower                                                        |
| hexiom                     | 6.89 ms                                                               | 7.15 ms: 1.04x slower                                                       |
| coroutines                 | 23.0 ms                                                               | 24.0 ms: 1.04x slower                                                       |
| async_tree_none_tg         | 307 ms                                                                | 321 ms: 1.04x slower                                                        |
| xml_etree_process          | 54.7 ms                                                               | 57.2 ms: 1.05x slower                                                       |
| async_tree_io              | 924 ms                                                                | 966 ms: 1.05x slower                                                        |
| xml_etree_generate         | 77.7 ms                                                               | 81.4 ms: 1.05x slower                                                       |
| 2to3                       | 276 ms                                                                | 290 ms: 1.05x slower                                                        |
| regex_dna                  | 210 ms                                                                | 221 ms: 1.05x slower                                                        |
| thrift                     | 789 us                                                                | 831 us: 1.05x slower                                                        |
| gc_traversal               | 3.58 ms                                                               | 3.78 ms: 1.05x slower                                                       |
| mako                       | 9.79 ms                                                               | 10.3 ms: 1.06x slower                                                       |
| spectral_norm              | 101 ms                                                                | 107 ms: 1.06x slower                                                        |
| deepcopy_reduce            | 2.70 us                                                               | 2.86 us: 1.06x slower                                                       |
| scimark_lu                 | 109 ms                                                                | 115 ms: 1.06x slower                                                        |
| asyncio_tcp                | 499 ms                                                                | 531 ms: 1.06x slower                                                        |
| async_tree_none            | 325 ms                                                                | 347 ms: 1.07x slower                                                        |
| go                         | 170 ms                                                                | 182 ms: 1.07x slower                                                        |
| regex_v8                   | 23.9 ms                                                               | 25.5 ms: 1.07x slower                                                       |
| chaos                      | 58.6 ms                                                               | 62.6 ms: 1.07x slower                                                       |
| deepcopy_memo              | 27.0 us                                                               | 28.9 us: 1.07x slower                                                       |
| regex_effbot               | 3.51 ms                                                               | 3.79 ms: 1.08x slower                                                       |
| mdp                        | 2.56 sec                                                              | 2.80 sec: 1.09x slower                                                      |
| logging_silent             | 103 ns                                                                | 113 ns: 1.10x slower                                                        |
| scimark_sor                | 116 ms                                                                | 128 ms: 1.10x slower                                                        |
| async_tree_memoization     | 395 ms                                                                | 437 ms: 1.11x slower                                                        |
| bench_thread_pool          | 817 us                                                                | 914 us: 1.12x slower                                                        |
| pycparser                  | 1.18 sec                                                              | 1.32 sec: 1.12x slower                                                      |
| sympy_expand               | 504 ms                                                                | 565 ms: 1.12x slower                                                        |
| sqlglot_normalize          | 113 ms                                                                | 128 ms: 1.13x slower                                                        |
| tomli_loads                | 1.92 sec                                                              | 2.18 sec: 1.13x slower                                                      |
| sympy_str                  | 299 ms                                                                | 339 ms: 1.13x slower                                                        |
| sqlglot_optimize           | 58.1 ms                                                               | 66.3 ms: 1.14x slower                                                       |
| genshi_xml                 | 59.0 ms                                                               | 67.5 ms: 1.14x slower                                                       |
| docutils                   | 3.04 sec                                                              | 3.58 sec: 1.18x slower                                                      |
| django_template            | 35.6 ms                                                               | 42.1 ms: 1.18x slower                                                       |
| html5lib                   | 63.4 ms                                                               | 75.5 ms: 1.19x slower                                                       |
| sqlglot_transpile          | 1.69 ms                                                               | 2.02 ms: 1.20x slower                                                       |
| sqlglot_parse              | 1.34 ms                                                               | 1.60 ms: 1.20x slower                                                       |
| sympy_integrate            | 22.8 ms                                                               | 27.3 ms: 1.20x slower                                                       |
| logging_format             | 6.04 us                                                               | 7.45 us: 1.23x slower                                                       |
| sympy_sum                  | 171 ms                                                                | 213 ms: 1.24x slower                                                        |
| logging_simple             | 5.54 us                                                               | 6.91 us: 1.25x slower                                                       |
| tornado_http               | 94.7 ms                                                               | 120 ms: 1.26x slower                                                        |
| pylint                     | 372 ms                                                                | 486 ms: 1.31x slower                                                        |
| richards_super             | 45.0 ms                                                               | 62.0 ms: 1.38x slower                                                       |
| deltablue                  | 3.18 ms                                                               | 4.46 ms: 1.40x slower                                                       |
| richards                   | 38.6 ms                                                               | 54.2 ms: 1.40x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                                |

Benchmark hidden because not significant (8): pathlib, json_dumps, float, telco, xml_etree_parse, meteor_contest, async_tree_io_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.05x