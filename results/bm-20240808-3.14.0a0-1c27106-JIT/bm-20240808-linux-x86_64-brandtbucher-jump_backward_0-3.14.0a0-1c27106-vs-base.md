# Results vs. base

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 1c27106
- commit date: 2024-08-08
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 281 ms: 1.02x slower                                                   |
| docutils       | 2.92 sec                                                              | 3.09 sec: 1.06x slower                                                 |
| html5lib       | 63.8 ms                                                               | 65.8 ms: 1.03x slower                                                  |
| tornado_http   | 92.6 ms                                                               | 110 ms: 1.19x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets     | 554 ms                                                                | 558 ms: 1.01x slower                                                   |
| async_generators       | 453 ms                                                                | 457 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                 |
| async_tree_none_tg     | 300 ms                                                                | 308 ms: 1.02x slower                                                   |
| async_tree_io          | 910 ms                                                                | 935 ms: 1.03x slower                                                   |
| async_tree_none        | 327 ms                                                                | 338 ms: 1.04x slower                                                   |
| async_tree_memoization | 422 ms                                                                | 441 ms: 1.04x slower                                                   |
| asyncio_tcp            | 498 ms                                                                | 535 ms: 1.07x slower                                                   |
| coroutines             | 22.9 ms                                                               | 25.5 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                                   |
| nbody          | 79.1 ms                                                               | 80.2 ms: 1.01x slower                                                  |
| float          | 70.5 ms                                                               | 71.6 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.41 ms: 1.12x faster                                                  |
| regex_dna      | 223 ms                                                                | 213 ms: 1.05x faster                                                   |
| regex_v8       | 24.4 ms                                                               | 24.1 ms: 1.01x faster                                                  |
| regex_compile  | 135 ms                                                                | 139 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 57.2 ms                                                               | 56.1 ms: 1.02x faster                                                  |
| xml_etree_generate   | 81.6 ms                                                               | 80.6 ms: 1.01x faster                                                  |
| json_dumps           | 10.3 ms                                                               | 10.2 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 99.2 ms                                                               | 99.6 ms: 1.00x slower                                                  |
| json_loads           | 27.7 us                                                               | 28.5 us: 1.03x slower                                                  |
| tomli_loads          | 1.91 sec                                                              | 1.97 sec: 1.03x slower                                                 |
| unpickle_pure_python | 215 us                                                                | 222 us: 1.03x slower                                                   |
| pickle_pure_python   | 300 us                                                                | 310 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.20 ms: 1.01x slower                                                  |
| python_startup         | 10.6 ms                                                               | 10.7 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 24.5 ms                                                               | 25.3 ms: 1.03x slower                                                  |
| mako            | 9.85 ms                                                               | 10.3 ms: 1.05x slower                                                  |
| genshi_xml      | 53.4 ms                                                               | 56.9 ms: 1.06x slower                                                  |
| django_template | 36.0 ms                                                               | 39.5 ms: 1.10x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.06x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot            | 3.83 ms                                                               | 3.41 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.33 ms: 1.05x faster                                                  |
| regex_dna               | 223 ms                                                                | 213 ms: 1.05x faster                                                   |
| telco                   | 7.97 ms                                                               | 7.72 ms: 1.03x faster                                                  |
| logging_silent          | 104 ns                                                                | 102 ns: 1.03x faster                                                   |
| scimark_monte_carlo     | 60.7 ms                                                               | 59.2 ms: 1.02x faster                                                  |
| xml_etree_process       | 57.2 ms                                                               | 56.1 ms: 1.02x faster                                                  |
| regex_v8                | 24.4 ms                                                               | 24.1 ms: 1.01x faster                                                  |
| xml_etree_generate      | 81.6 ms                                                               | 80.6 ms: 1.01x faster                                                  |
| json_dumps              | 10.3 ms                                                               | 10.2 ms: 1.01x faster                                                  |
| gc_traversal            | 3.85 ms                                                               | 3.81 ms: 1.01x faster                                                  |
| meteor_contest          | 105 ms                                                                | 105 ms: 1.01x faster                                                   |
| crypto_pyaes            | 66.8 ms                                                               | 66.4 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 99.2 ms                                                               | 99.6 ms: 1.00x slower                                                  |
| bpe_tokeniser           | 4.52 sec                                                              | 4.54 sec: 1.00x slower                                                 |
| python_startup_no_site  | 7.17 ms                                                               | 7.20 ms: 1.01x slower                                                  |
| asyncio_websockets      | 554 ms                                                                | 558 ms: 1.01x slower                                                   |
| pathlib                 | 16.1 ms                                                               | 16.2 ms: 1.01x slower                                                  |
| async_generators        | 453 ms                                                                | 457 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                 |
| python_startup          | 10.6 ms                                                               | 10.7 ms: 1.01x slower                                                  |
| create_gc_cycles        | 1.78 ms                                                               | 1.80 ms: 1.01x slower                                                  |
| pprint_pformat          | 1.49 sec                                                              | 1.51 sec: 1.01x slower                                                 |
| pidigits                | 186 ms                                                                | 188 ms: 1.01x slower                                                   |
| nbody                   | 79.1 ms                                                               | 80.2 ms: 1.01x slower                                                  |
| float                   | 70.5 ms                                                               | 71.6 ms: 1.02x slower                                                  |
| scimark_sor             | 117 ms                                                                | 119 ms: 1.02x slower                                                   |
| mdp                     | 2.56 sec                                                              | 2.61 sec: 1.02x slower                                                 |
| coverage                | 91.8 ms                                                               | 93.6 ms: 1.02x slower                                                  |
| 2to3                    | 275 ms                                                                | 281 ms: 1.02x slower                                                   |
| chaos                   | 58.1 ms                                                               | 59.5 ms: 1.02x slower                                                  |
| async_tree_none_tg      | 300 ms                                                                | 308 ms: 1.02x slower                                                   |
| async_tree_io           | 910 ms                                                                | 935 ms: 1.03x slower                                                   |
| json_loads              | 27.7 us                                                               | 28.5 us: 1.03x slower                                                  |
| deepcopy_memo           | 29.1 us                                                               | 30.0 us: 1.03x slower                                                  |
| tomli_loads             | 1.91 sec                                                              | 1.97 sec: 1.03x slower                                                 |
| unpickle_pure_python    | 215 us                                                                | 222 us: 1.03x slower                                                   |
| regex_compile           | 135 ms                                                                | 139 ms: 1.03x slower                                                   |
| html5lib                | 63.8 ms                                                               | 65.8 ms: 1.03x slower                                                  |
| pickle_pure_python      | 300 us                                                                | 310 us: 1.03x slower                                                   |
| genshi_text             | 24.5 ms                                                               | 25.3 ms: 1.03x slower                                                  |
| go                      | 146 ms                                                                | 151 ms: 1.03x slower                                                   |
| hexiom                  | 6.71 ms                                                               | 6.94 ms: 1.03x slower                                                  |
| sqlglot_normalize       | 113 ms                                                                | 117 ms: 1.04x slower                                                   |
| async_tree_none         | 327 ms                                                                | 338 ms: 1.04x slower                                                   |
| comprehensions          | 16.2 us                                                               | 16.9 us: 1.04x slower                                                  |
| async_tree_memoization  | 422 ms                                                                | 441 ms: 1.04x slower                                                   |
| mako                    | 9.85 ms                                                               | 10.3 ms: 1.05x slower                                                  |
| generators              | 32.9 ms                                                               | 34.4 ms: 1.05x slower                                                  |
| deepcopy_reduce         | 2.78 us                                                               | 2.93 us: 1.05x slower                                                  |
| sqlglot_parse           | 1.29 ms                                                               | 1.37 ms: 1.06x slower                                                  |
| sqlglot_optimize        | 55.9 ms                                                               | 59.2 ms: 1.06x slower                                                  |
| docutils                | 2.92 sec                                                              | 3.09 sec: 1.06x slower                                                 |
| sqlglot_transpile       | 1.62 ms                                                               | 1.72 ms: 1.06x slower                                                  |
| sympy_expand            | 508 ms                                                                | 541 ms: 1.06x slower                                                   |
| pyflate                 | 432 ms                                                                | 459 ms: 1.06x slower                                                   |
| genshi_xml              | 53.4 ms                                                               | 56.9 ms: 1.06x slower                                                  |
| asyncio_tcp             | 498 ms                                                                | 535 ms: 1.07x slower                                                   |
| thrift                  | 797 us                                                                | 859 us: 1.08x slower                                                   |
| bench_thread_pool       | 822 us                                                                | 893 us: 1.09x slower                                                   |
| raytrace                | 269 ms                                                                | 293 ms: 1.09x slower                                                   |
| sympy_str               | 298 ms                                                                | 325 ms: 1.09x slower                                                   |
| spectral_norm           | 100 ms                                                                | 110 ms: 1.09x slower                                                   |
| django_template         | 36.0 ms                                                               | 39.5 ms: 1.10x slower                                                  |
| sympy_integrate         | 22.6 ms                                                               | 25.1 ms: 1.11x slower                                                  |
| coroutines              | 22.9 ms                                                               | 25.5 ms: 1.11x slower                                                  |
| richards_super          | 47.5 ms                                                               | 54.0 ms: 1.14x slower                                                  |
| pylint                  | 356 ms                                                                | 408 ms: 1.15x slower                                                   |
| deltablue               | 3.58 ms                                                               | 4.13 ms: 1.15x slower                                                  |
| richards                | 41.2 ms                                                               | 47.6 ms: 1.16x slower                                                  |
| sympy_sum               | 170 ms                                                                | 197 ms: 1.16x slower                                                   |
| logging_simple          | 5.57 us                                                               | 6.63 us: 1.19x slower                                                  |
| tornado_http            | 92.6 ms                                                               | 110 ms: 1.19x slower                                                   |
| logging_format          | 6.17 us                                                               | 7.47 us: 1.21x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (15): fannkuch, xml_etree_parse, bench_mp_pool, scimark_lu, json, nqueens, typing_runtime_protocols, pprint_safe_repr, deepcopy, async_tree_cpu_io_mixed, scimark_fft, pycparser, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.04x