# Results vs. base

- fork: brandtbucher
- ref: underflow_no_yield
- machine: linux-x86_64
- commit hash: f9222b1
- commit date: 2024-08-26
- overall geometric mean: 1.02x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 277 ms: 1.01x slower                                                      |
| docutils       | 3.04 sec                                                              | 3.34 sec: 1.10x slower                                                    |
| html5lib       | 63.4 ms                                                               | 69.7 ms: 1.10x slower                                                     |
| tornado_http   | 94.7 ms                                                               | 102 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines             | 23.0 ms                                                               | 22.7 ms: 1.02x faster                                                     |
| async_generators       | 454 ms                                                                | 459 ms: 1.01x slower                                                      |
| async_tree_io          | 924 ms                                                                | 938 ms: 1.02x slower                                                      |
| asyncio_tcp            | 499 ms                                                                | 513 ms: 1.03x slower                                                      |
| async_tree_memoization | 395 ms                                                                | 410 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (8): asyncio_websockets, asyncio_tcp_ssl, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 82.0 ms                                                               | 80.8 ms: 1.02x faster                                                     |
| pidigits       | 187 ms                                                                | 185 ms: 1.01x faster                                                      |
| float          | 70.4 ms                                                               | 71.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                | 213 ms: 1.01x slower                                                      |
| regex_effbot   | 3.51 ms                                                               | 3.62 ms: 1.03x slower                                                     |
| regex_v8       | 23.9 ms                                                               | 24.7 ms: 1.03x slower                                                     |
| regex_compile  | 142 ms                                                                | 150 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 197 us: 1.08x faster                                                      |
| json_dumps           | 9.98 ms                                                               | 9.91 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.3 ms: 1.01x slower                                                     |
| json_loads           | 28.6 us                                                               | 29.6 us: 1.04x slower                                                     |
| pickle_pure_python   | 302 us                                                                | 313 us: 1.04x slower                                                      |
| tomli_loads          | 1.92 sec                                                              | 2.06 sec: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| python_startup_no_site | 7.14 ms                                                               | 7.14 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 25.5 ms: 1.01x faster                                                     |
| mako            | 9.79 ms                                                               | 9.76 ms: 1.00x faster                                                     |
| genshi_xml      | 59.0 ms                                                               | 60.4 ms: 1.02x slower                                                     |
| django_template | 35.6 ms                                                               | 38.5 ms: 1.08x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python    | 213 us                                                                | 197 us: 1.08x faster                                                      |
| scimark_monte_carlo     | 62.5 ms                                                               | 58.9 ms: 1.06x faster                                                     |
| richards_super          | 45.0 ms                                                               | 42.8 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult | 4.47 ms                                                               | 4.30 ms: 1.04x faster                                                     |
| logging_silent          | 103 ns                                                                | 99.5 ns: 1.04x faster                                                     |
| deepcopy_memo           | 27.0 us                                                               | 26.4 us: 1.02x faster                                                     |
| scimark_fft             | 314 ms                                                                | 308 ms: 1.02x faster                                                      |
| deepcopy_reduce         | 2.70 us                                                               | 2.65 us: 1.02x faster                                                     |
| coroutines              | 23.0 ms                                                               | 22.7 ms: 1.02x faster                                                     |
| nbody                   | 82.0 ms                                                               | 80.8 ms: 1.02x faster                                                     |
| crypto_pyaes            | 66.6 ms                                                               | 65.7 ms: 1.01x faster                                                     |
| pidigits                | 187 ms                                                                | 185 ms: 1.01x faster                                                      |
| json                    | 5.32 ms                                                               | 5.26 ms: 1.01x faster                                                     |
| thrift                  | 789 us                                                                | 781 us: 1.01x faster                                                      |
| richards                | 38.6 ms                                                               | 38.3 ms: 1.01x faster                                                     |
| json_dumps              | 9.98 ms                                                               | 9.91 ms: 1.01x faster                                                     |
| genshi_text             | 25.7 ms                                                               | 25.5 ms: 1.01x faster                                                     |
| hexiom                  | 6.89 ms                                                               | 6.85 ms: 1.01x faster                                                     |
| meteor_contest          | 106 ms                                                                | 106 ms: 1.01x faster                                                      |
| mako                    | 9.79 ms                                                               | 9.76 ms: 1.00x faster                                                     |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| python_startup_no_site  | 7.14 ms                                                               | 7.14 ms: 1.00x slower                                                     |
| 2to3                    | 276 ms                                                                | 277 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 97.7 ms                                                               | 98.3 ms: 1.01x slower                                                     |
| float                   | 70.4 ms                                                               | 71.2 ms: 1.01x slower                                                     |
| bench_thread_pool       | 817 us                                                                | 826 us: 1.01x slower                                                      |
| async_generators        | 454 ms                                                                | 459 ms: 1.01x slower                                                      |
| regex_dna               | 210 ms                                                                | 213 ms: 1.01x slower                                                      |
| create_gc_cycles        | 1.75 ms                                                               | 1.78 ms: 1.01x slower                                                     |
| spectral_norm           | 101 ms                                                                | 103 ms: 1.01x slower                                                      |
| async_tree_io           | 924 ms                                                                | 938 ms: 1.02x slower                                                      |
| deltablue               | 3.18 ms                                                               | 3.24 ms: 1.02x slower                                                     |
| pyflate                 | 450 ms                                                                | 458 ms: 1.02x slower                                                      |
| gc_traversal            | 3.58 ms                                                               | 3.66 ms: 1.02x slower                                                     |
| genshi_xml              | 59.0 ms                                                               | 60.4 ms: 1.02x slower                                                     |
| scimark_lu              | 109 ms                                                                | 111 ms: 1.02x slower                                                      |
| pprint_pformat          | 1.49 sec                                                              | 1.53 sec: 1.03x slower                                                    |
| asyncio_tcp             | 499 ms                                                                | 513 ms: 1.03x slower                                                      |
| regex_effbot            | 3.51 ms                                                               | 3.62 ms: 1.03x slower                                                     |
| regex_v8                | 23.9 ms                                                               | 24.7 ms: 1.03x slower                                                     |
| json_loads              | 28.6 us                                                               | 29.6 us: 1.04x slower                                                     |
| pickle_pure_python      | 302 us                                                                | 313 us: 1.04x slower                                                      |
| async_tree_memoization  | 395 ms                                                                | 410 ms: 1.04x slower                                                      |
| sqlglot_optimize        | 58.1 ms                                                               | 60.4 ms: 1.04x slower                                                     |
| sqlglot_transpile       | 1.69 ms                                                               | 1.78 ms: 1.05x slower                                                     |
| regex_compile           | 142 ms                                                                | 150 ms: 1.06x slower                                                      |
| sqlglot_normalize       | 113 ms                                                                | 120 ms: 1.06x slower                                                      |
| scimark_sor             | 116 ms                                                                | 123 ms: 1.06x slower                                                      |
| sympy_expand            | 504 ms                                                                | 536 ms: 1.06x slower                                                      |
| mdp                     | 2.56 sec                                                              | 2.73 sec: 1.06x slower                                                    |
| logging_simple          | 5.54 us                                                               | 5.90 us: 1.06x slower                                                     |
| tomli_loads             | 1.92 sec                                                              | 2.06 sec: 1.07x slower                                                    |
| logging_format          | 6.04 us                                                               | 6.47 us: 1.07x slower                                                     |
| sympy_str               | 299 ms                                                                | 321 ms: 1.07x slower                                                      |
| pycparser               | 1.18 sec                                                              | 1.27 sec: 1.07x slower                                                    |
| tornado_http            | 94.7 ms                                                               | 102 ms: 1.08x slower                                                      |
| django_template         | 35.6 ms                                                               | 38.5 ms: 1.08x slower                                                     |
| pylint                  | 372 ms                                                                | 406 ms: 1.09x slower                                                      |
| sympy_integrate         | 22.8 ms                                                               | 24.9 ms: 1.09x slower                                                     |
| html5lib                | 63.4 ms                                                               | 69.7 ms: 1.10x slower                                                     |
| docutils                | 3.04 sec                                                              | 3.34 sec: 1.10x slower                                                    |
| sympy_sum               | 171 ms                                                                | 189 ms: 1.10x slower                                                      |
| sqlglot_parse           | 1.34 ms                                                               | 1.52 ms: 1.14x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (26): raytrace, xml_etree_parse, chaos, go, xml_etree_process, xml_etree_generate, asyncio_websockets, pathlib, telco, asyncio_tcp_ssl, deepcopy, bench_mp_pool, pprint_safe_repr, fannkuch, async_tree_none, bpe_tokeniser, async_tree_cpu_io_mixed_tg, comprehensions, coverage, generators, async_tree_cpu_io_mixed, nqueens, typing_runtime_protocols, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x