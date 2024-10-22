# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 2d4d2a8
- commit date: 2024-08-28
- overall geometric mean: 1.00x slower
- HPT reliability: 85.29%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 277 ms: 1.01x slower                                                      |
| html5lib       | 63.4 ms                                                               | 64.2 ms: 1.01x slower                                                     |
| tornado_http   | 94.7 ms                                                               | 94.4 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_tcp            | 499 ms                                                                | 492 ms: 1.01x faster                                                      |
| async_generators       | 454 ms                                                                | 459 ms: 1.01x slower                                                      |
| async_tree_io          | 924 ms                                                                | 938 ms: 1.02x slower                                                      |
| async_tree_io_tg       | 886 ms                                                                | 902 ms: 1.02x slower                                                      |
| coroutines             | 23.0 ms                                                               | 23.6 ms: 1.02x slower                                                     |
| async_tree_memoization | 395 ms                                                                | 417 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 82.0 ms                                                               | 79.6 ms: 1.03x faster                                                     |
| pidigits       | 187 ms                                                                | 186 ms: 1.01x faster                                                      |
| float          | 70.4 ms                                                               | 70.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 141 ms: 1.01x faster                                                      |
| regex_effbot   | 3.51 ms                                                               | 3.56 ms: 1.01x slower                                                     |
| regex_dna      | 210 ms                                                                | 213 ms: 1.02x slower                                                      |
| regex_v8       | 23.9 ms                                                               | 24.3 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 28.6 us                                                               | 28.8 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.6 ms: 1.01x slower                                                     |
| unpickle_pure_python | 213 us                                                                | 216 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (6): xml_etree_process, json_dumps, xml_etree_generate, pickle_pure_python, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.14 ms                                                               | 7.17 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 24.1 ms: 1.06x faster                                                     |
| genshi_xml      | 59.0 ms                                                               | 56.7 ms: 1.04x faster                                                     |
| mako            | 9.79 ms                                                               | 9.67 ms: 1.01x faster                                                     |
| django_template | 35.6 ms                                                               | 36.7 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text             | 25.7 ms                                                               | 24.1 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult | 4.47 ms                                                               | 4.30 ms: 1.04x faster                                                     |
| genshi_xml              | 59.0 ms                                                               | 56.7 ms: 1.04x faster                                                     |
| pyflate                 | 450 ms                                                                | 435 ms: 1.04x faster                                                      |
| nbody                   | 82.0 ms                                                               | 79.6 ms: 1.03x faster                                                     |
| spectral_norm           | 101 ms                                                                | 98.5 ms: 1.03x faster                                                     |
| deepcopy_reduce         | 2.70 us                                                               | 2.63 us: 1.02x faster                                                     |
| scimark_fft             | 314 ms                                                                | 307 ms: 1.02x faster                                                      |
| generators              | 33.3 ms                                                               | 32.6 ms: 1.02x faster                                                     |
| deepcopy                | 265 us                                                                | 261 us: 1.02x faster                                                      |
| nqueens                 | 85.7 ms                                                               | 84.3 ms: 1.02x faster                                                     |
| crypto_pyaes            | 66.6 ms                                                               | 65.6 ms: 1.02x faster                                                     |
| asyncio_tcp             | 499 ms                                                                | 492 ms: 1.01x faster                                                      |
| mako                    | 9.79 ms                                                               | 9.67 ms: 1.01x faster                                                     |
| pidigits                | 187 ms                                                                | 186 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 113 ms                                                                | 112 ms: 1.01x faster                                                      |
| comprehensions          | 16.7 us                                                               | 16.6 us: 1.01x faster                                                     |
| bpe_tokeniser           | 4.43 sec                                                              | 4.40 sec: 1.01x faster                                                    |
| regex_compile           | 142 ms                                                                | 141 ms: 1.01x faster                                                      |
| hexiom                  | 6.89 ms                                                               | 6.86 ms: 1.00x faster                                                     |
| fannkuch                | 372 ms                                                                | 370 ms: 1.00x faster                                                      |
| tornado_http            | 94.7 ms                                                               | 94.4 ms: 1.00x faster                                                     |
| python_startup          | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site  | 7.14 ms                                                               | 7.17 ms: 1.00x slower                                                     |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.00x slower                                                      |
| 2to3                    | 276 ms                                                                | 277 ms: 1.01x slower                                                      |
| float                   | 70.4 ms                                                               | 70.8 ms: 1.01x slower                                                     |
| json_loads              | 28.6 us                                                               | 28.8 us: 1.01x slower                                                     |
| logging_silent          | 103 ns                                                                | 104 ns: 1.01x slower                                                      |
| xml_etree_iterparse     | 97.7 ms                                                               | 98.6 ms: 1.01x slower                                                     |
| deltablue               | 3.18 ms                                                               | 3.22 ms: 1.01x slower                                                     |
| json                    | 5.32 ms                                                               | 5.38 ms: 1.01x slower                                                     |
| async_generators        | 454 ms                                                                | 459 ms: 1.01x slower                                                      |
| sqlglot_parse           | 1.34 ms                                                               | 1.35 ms: 1.01x slower                                                     |
| scimark_monte_carlo     | 62.5 ms                                                               | 63.2 ms: 1.01x slower                                                     |
| logging_simple          | 5.54 us                                                               | 5.61 us: 1.01x slower                                                     |
| html5lib                | 63.4 ms                                                               | 64.2 ms: 1.01x slower                                                     |
| pprint_pformat          | 1.49 sec                                                              | 1.51 sec: 1.01x slower                                                    |
| unpickle_pure_python    | 213 us                                                                | 216 us: 1.01x slower                                                      |
| scimark_lu              | 109 ms                                                                | 110 ms: 1.01x slower                                                      |
| regex_effbot            | 3.51 ms                                                               | 3.56 ms: 1.01x slower                                                     |
| regex_dna               | 210 ms                                                                | 213 ms: 1.02x slower                                                      |
| async_tree_io           | 924 ms                                                                | 938 ms: 1.02x slower                                                      |
| regex_v8                | 23.9 ms                                                               | 24.3 ms: 1.02x slower                                                     |
| richards                | 38.6 ms                                                               | 39.3 ms: 1.02x slower                                                     |
| coverage                | 85.6 ms                                                               | 87.1 ms: 1.02x slower                                                     |
| async_tree_io_tg        | 886 ms                                                                | 902 ms: 1.02x slower                                                      |
| thrift                  | 789 us                                                                | 803 us: 1.02x slower                                                      |
| pycparser               | 1.18 sec                                                              | 1.20 sec: 1.02x slower                                                    |
| create_gc_cycles        | 1.75 ms                                                               | 1.79 ms: 1.02x slower                                                     |
| coroutines              | 23.0 ms                                                               | 23.6 ms: 1.02x slower                                                     |
| gc_traversal            | 3.58 ms                                                               | 3.67 ms: 1.02x slower                                                     |
| logging_format          | 6.04 us                                                               | 6.21 us: 1.03x slower                                                     |
| django_template         | 35.6 ms                                                               | 36.7 ms: 1.03x slower                                                     |
| async_tree_memoization  | 395 ms                                                                | 417 ms: 1.06x slower                                                      |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (34): typing_runtime_protocols, async_tree_cpu_io_mixed_tg, deepcopy_memo, xml_etree_process, json_dumps, asyncio_websockets, chaos, sympy_str, mdp, sqlglot_optimize, async_tree_cpu_io_mixed, xml_etree_generate, bench_thread_pool, telco, sympy_expand, bench_mp_pool, pylint, sympy_sum, pickle_pure_python, asyncio_tcp_ssl, go, richards_super, tomli_loads, docutils, sympy_integrate, sqlglot_transpile, pprint_safe_repr, async_tree_memoization_tg, pathlib, raytrace, async_tree_none_tg, xml_etree_parse, async_tree_none, scimark_sor

# HPT report

- Reliability score: 85.29% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x