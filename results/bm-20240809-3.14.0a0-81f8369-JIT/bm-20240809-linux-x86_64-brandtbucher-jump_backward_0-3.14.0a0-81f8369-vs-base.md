# Results vs. base

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 81f8369
- commit date: 2024-08-09
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 283 ms: 1.03x slower                                                   |
| docutils       | 2.92 sec                                                              | 3.08 sec: 1.05x slower                                                 |
| html5lib       | 63.8 ms                                                               | 64.2 ms: 1.01x slower                                                  |
| tornado_http   | 92.6 ms                                                               | 107 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets     | 554 ms                                                                | 559 ms: 1.01x slower                                                   |
| async_generators       | 453 ms                                                                | 457 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                 |
| async_tree_none        | 327 ms                                                                | 333 ms: 1.02x slower                                                   |
| async_tree_none_tg     | 300 ms                                                                | 307 ms: 1.02x slower                                                   |
| async_tree_memoization | 422 ms                                                                | 434 ms: 1.03x slower                                                   |
| asyncio_tcp            | 498 ms                                                                | 530 ms: 1.06x slower                                                   |
| coroutines             | 22.9 ms                                                               | 25.2 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 70.5 ms                                                               | 69.0 ms: 1.02x faster                                                  |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                   |
| nbody          | 79.1 ms                                                               | 79.6 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.60 ms: 1.06x faster                                                  |
| regex_dna      | 223 ms                                                                | 212 ms: 1.05x faster                                                   |
| regex_v8       | 24.4 ms                                                               | 24.2 ms: 1.01x faster                                                  |
| regex_compile  | 135 ms                                                                | 138 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|--------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process  | 57.2 ms                                                               | 54.7 ms: 1.05x faster                                                  |
| pickle_pure_python | 300 us                                                                | 293 us: 1.02x faster                                                   |
| xml_etree_generate | 81.6 ms                                                               | 80.0 ms: 1.02x faster                                                  |
| json_loads         | 27.7 us                                                               | 27.2 us: 1.02x faster                                                  |
| json_dumps         | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                  |
| tomli_loads        | 1.91 sec                                                              | 1.94 sec: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.16 ms: 1.00x faster                                                  |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 24.5 ms                                                               | 23.9 ms: 1.02x faster                                                  |
| genshi_xml      | 53.4 ms                                                               | 55.1 ms: 1.03x slower                                                  |
| django_template | 36.0 ms                                                               | 39.3 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| logging_silent          | 104 ns                                                                | 98.3 ns: 1.06x faster                                                  |
| regex_effbot            | 3.83 ms                                                               | 3.60 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.30 ms: 1.06x faster                                                  |
| regex_dna               | 223 ms                                                                | 212 ms: 1.05x faster                                                   |
| xml_etree_process       | 57.2 ms                                                               | 54.7 ms: 1.05x faster                                                  |
| gc_traversal            | 3.85 ms                                                               | 3.71 ms: 1.04x faster                                                  |
| scimark_sor             | 117 ms                                                                | 113 ms: 1.03x faster                                                   |
| telco                   | 7.97 ms                                                               | 7.75 ms: 1.03x faster                                                  |
| genshi_text             | 24.5 ms                                                               | 23.9 ms: 1.02x faster                                                  |
| pickle_pure_python      | 300 us                                                                | 293 us: 1.02x faster                                                   |
| float                   | 70.5 ms                                                               | 69.0 ms: 1.02x faster                                                  |
| xml_etree_generate      | 81.6 ms                                                               | 80.0 ms: 1.02x faster                                                  |
| json_loads              | 27.7 us                                                               | 27.2 us: 1.02x faster                                                  |
| scimark_monte_carlo     | 60.7 ms                                                               | 59.8 ms: 1.01x faster                                                  |
| json                    | 5.09 ms                                                               | 5.03 ms: 1.01x faster                                                  |
| deepcopy                | 273 us                                                                | 270 us: 1.01x faster                                                   |
| pathlib                 | 16.1 ms                                                               | 15.9 ms: 1.01x faster                                                  |
| regex_v8                | 24.4 ms                                                               | 24.2 ms: 1.01x faster                                                  |
| comprehensions          | 16.2 us                                                               | 16.1 us: 1.00x faster                                                  |
| python_startup_no_site  | 7.17 ms                                                               | 7.16 ms: 1.00x faster                                                  |
| pidigits                | 186 ms                                                                | 186 ms: 1.00x slower                                                   |
| create_gc_cycles        | 1.78 ms                                                               | 1.79 ms: 1.00x slower                                                  |
| html5lib                | 63.8 ms                                                               | 64.2 ms: 1.01x slower                                                  |
| python_startup          | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| nbody                   | 79.1 ms                                                               | 79.6 ms: 1.01x slower                                                  |
| bpe_tokeniser           | 4.52 sec                                                              | 4.54 sec: 1.01x slower                                                 |
| asyncio_websockets      | 554 ms                                                                | 559 ms: 1.01x slower                                                   |
| async_generators        | 453 ms                                                                | 457 ms: 1.01x slower                                                   |
| coverage                | 91.8 ms                                                               | 92.7 ms: 1.01x slower                                                  |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                 |
| tomli_loads             | 1.91 sec                                                              | 1.94 sec: 1.01x slower                                                 |
| logging_simple          | 5.57 us                                                               | 5.66 us: 1.02x slower                                                  |
| nqueens                 | 84.0 ms                                                               | 85.4 ms: 1.02x slower                                                  |
| hexiom                  | 6.71 ms                                                               | 6.83 ms: 1.02x slower                                                  |
| async_tree_none         | 327 ms                                                                | 333 ms: 1.02x slower                                                   |
| pprint_pformat          | 1.49 sec                                                              | 1.52 sec: 1.02x slower                                                 |
| meteor_contest          | 105 ms                                                                | 108 ms: 1.02x slower                                                   |
| scimark_fft             | 307 ms                                                                | 313 ms: 1.02x slower                                                   |
| sqlglot_normalize       | 113 ms                                                                | 115 ms: 1.02x slower                                                   |
| async_tree_none_tg      | 300 ms                                                                | 307 ms: 1.02x slower                                                   |
| regex_compile           | 135 ms                                                                | 138 ms: 1.02x slower                                                   |
| go                      | 146 ms                                                                | 150 ms: 1.02x slower                                                   |
| spectral_norm           | 100 ms                                                                | 103 ms: 1.02x slower                                                   |
| pyflate                 | 432 ms                                                                | 444 ms: 1.03x slower                                                   |
| async_tree_memoization  | 422 ms                                                                | 434 ms: 1.03x slower                                                   |
| 2to3                    | 275 ms                                                                | 283 ms: 1.03x slower                                                   |
| raytrace                | 269 ms                                                                | 277 ms: 1.03x slower                                                   |
| genshi_xml              | 53.4 ms                                                               | 55.1 ms: 1.03x slower                                                  |
| thrift                  | 797 us                                                                | 823 us: 1.03x slower                                                   |
| sqlglot_optimize        | 55.9 ms                                                               | 58.1 ms: 1.04x slower                                                  |
| sympy_expand            | 508 ms                                                                | 530 ms: 1.04x slower                                                   |
| mdp                     | 2.56 sec                                                              | 2.67 sec: 1.04x slower                                                 |
| docutils                | 2.92 sec                                                              | 3.08 sec: 1.05x slower                                                 |
| asyncio_tcp             | 498 ms                                                                | 530 ms: 1.06x slower                                                   |
| sqlglot_parse           | 1.29 ms                                                               | 1.37 ms: 1.06x slower                                                  |
| generators              | 32.9 ms                                                               | 35.1 ms: 1.07x slower                                                  |
| sqlglot_transpile       | 1.62 ms                                                               | 1.73 ms: 1.07x slower                                                  |
| sympy_str               | 298 ms                                                                | 320 ms: 1.07x slower                                                   |
| bench_thread_pool       | 822 us                                                                | 883 us: 1.07x slower                                                   |
| richards_super          | 47.5 ms                                                               | 51.7 ms: 1.09x slower                                                  |
| django_template         | 36.0 ms                                                               | 39.3 ms: 1.09x slower                                                  |
| coroutines              | 22.9 ms                                                               | 25.2 ms: 1.10x slower                                                  |
| sympy_integrate         | 22.6 ms                                                               | 25.0 ms: 1.11x slower                                                  |
| richards                | 41.2 ms                                                               | 46.0 ms: 1.12x slower                                                  |
| pylint                  | 356 ms                                                                | 401 ms: 1.13x slower                                                   |
| sympy_sum               | 170 ms                                                                | 197 ms: 1.16x slower                                                   |
| tornado_http            | 92.6 ms                                                               | 107 ms: 1.16x slower                                                   |
| deltablue               | 3.58 ms                                                               | 4.24 ms: 1.18x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (20): deepcopy_memo, logging_format, chaos, typing_runtime_protocols, crypto_pyaes, xml_etree_parse, mako, xml_etree_iterparse, bench_mp_pool, async_tree_cpu_io_mixed, fannkuch, pycparser, scimark_lu, async_tree_cpu_io_mixed_tg, deepcopy_reduce, unpickle_pure_python, pprint_safe_repr, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x