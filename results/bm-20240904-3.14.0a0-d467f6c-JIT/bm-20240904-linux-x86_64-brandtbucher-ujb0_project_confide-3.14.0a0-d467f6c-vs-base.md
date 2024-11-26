# Results vs. base

- fork: brandtbucher
- ref: ujb0_project_confide
- machine: linux-x86_64
- commit hash: d467f6c
- commit date: 2024-09-04
- overall geometric mean: 1.043x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 294 ms: 1.07x slower                                                        |
| docutils       | 3.04 sec                                                              | 3.52 sec: 1.16x slower                                                      |
| html5lib       | 63.4 ms                                                               | 74.3 ms: 1.17x slower                                                       |
| tornado_http   | 94.7 ms                                                               | 118 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets      | 556 ms                                                                | 560 ms: 1.01x slower                                                        |
| async_generators        | 454 ms                                                                | 457 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                      |
| async_tree_cpu_io_mixed | 561 ms                                                                | 572 ms: 1.02x slower                                                        |
| coroutines              | 23.0 ms                                                               | 23.8 ms: 1.03x slower                                                       |
| async_tree_io           | 924 ms                                                                | 961 ms: 1.04x slower                                                        |
| async_tree_none_tg      | 307 ms                                                                | 321 ms: 1.04x slower                                                        |
| async_tree_none         | 325 ms                                                                | 341 ms: 1.05x slower                                                        |
| asyncio_tcp             | 499 ms                                                                | 530 ms: 1.06x slower                                                        |
| async_tree_memoization  | 395 ms                                                                | 427 ms: 1.08x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.03x slower                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 82.0 ms                                                               | 79.9 ms: 1.03x faster                                                       |
| float          | 70.4 ms                                                               | 68.7 ms: 1.03x faster                                                       |
| pidigits       | 187 ms                                                                | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                | 218 ms: 1.04x slower                                                        |
| regex_effbot   | 3.51 ms                                                               | 3.65 ms: 1.04x slower                                                       |
| regex_compile  | 142 ms                                                                | 152 ms: 1.07x slower                                                        |
| regex_v8       | 23.9 ms                                                               | 26.1 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 193 us: 1.10x faster                                                        |
| json_dumps           | 9.98 ms                                                               | 9.72 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.6 ms: 1.01x slower                                                       |
| pickle_pure_python   | 302 us                                                                | 310 us: 1.03x slower                                                        |
| xml_etree_generate   | 77.7 ms                                                               | 80.1 ms: 1.03x slower                                                       |
| json_loads           | 28.6 us                                                               | 29.6 us: 1.04x slower                                                       |
| tomli_loads          | 1.92 sec                                                              | 2.15 sec: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.16 ms: 1.00x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 22.7 ms: 1.13x faster                                                       |
| mako            | 9.79 ms                                                               | 9.58 ms: 1.02x faster                                                       |
| django_template | 35.6 ms                                                               | 40.5 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text             | 25.7 ms                                                               | 22.7 ms: 1.13x faster                                                       |
| unpickle_pure_python    | 213 us                                                                | 193 us: 1.10x faster                                                        |
| scimark_monte_carlo     | 62.5 ms                                                               | 57.9 ms: 1.08x faster                                                       |
| logging_silent          | 103 ns                                                                | 98.3 ns: 1.05x faster                                                       |
| pprint_safe_repr        | 728 ms                                                                | 695 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult | 4.47 ms                                                               | 4.34 ms: 1.03x faster                                                       |
| json_dumps              | 9.98 ms                                                               | 9.72 ms: 1.03x faster                                                       |
| deepcopy_memo           | 27.0 us                                                               | 26.3 us: 1.03x faster                                                       |
| nbody                   | 82.0 ms                                                               | 79.9 ms: 1.03x faster                                                       |
| float                   | 70.4 ms                                                               | 68.7 ms: 1.03x faster                                                       |
| scimark_fft             | 314 ms                                                                | 307 ms: 1.02x faster                                                        |
| pprint_pformat          | 1.49 sec                                                              | 1.46 sec: 1.02x faster                                                      |
| mako                    | 9.79 ms                                                               | 9.58 ms: 1.02x faster                                                       |
| nqueens                 | 85.7 ms                                                               | 84.5 ms: 1.01x faster                                                       |
| crypto_pyaes            | 66.6 ms                                                               | 66.0 ms: 1.01x faster                                                       |
| pidigits                | 187 ms                                                                | 186 ms: 1.01x faster                                                        |
| scimark_lu              | 109 ms                                                                | 108 ms: 1.01x faster                                                        |
| comprehensions          | 16.7 us                                                               | 16.6 us: 1.01x faster                                                       |
| python_startup_no_site  | 7.14 ms                                                               | 7.16 ms: 1.00x slower                                                       |
| asyncio_websockets      | 556 ms                                                                | 560 ms: 1.01x slower                                                        |
| async_generators        | 454 ms                                                                | 457 ms: 1.01x slower                                                        |
| python_startup          | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 97.7 ms                                                               | 98.6 ms: 1.01x slower                                                       |
| mdp                     | 2.56 sec                                                              | 2.59 sec: 1.01x slower                                                      |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.83 sec: 1.01x slower                                                      |
| meteor_contest          | 106 ms                                                                | 108 ms: 1.02x slower                                                        |
| fannkuch                | 372 ms                                                                | 380 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 561 ms                                                                | 572 ms: 1.02x slower                                                        |
| bpe_tokeniser           | 4.43 sec                                                              | 4.53 sec: 1.02x slower                                                      |
| generators              | 33.3 ms                                                               | 34.1 ms: 1.02x slower                                                       |
| chaos                   | 58.6 ms                                                               | 59.9 ms: 1.02x slower                                                       |
| telco                   | 7.63 ms                                                               | 7.82 ms: 1.02x slower                                                       |
| coverage                | 85.6 ms                                                               | 87.9 ms: 1.03x slower                                                       |
| pickle_pure_python      | 302 us                                                                | 310 us: 1.03x slower                                                        |
| thrift                  | 789 us                                                                | 810 us: 1.03x slower                                                        |
| raytrace                | 276 ms                                                                | 284 ms: 1.03x slower                                                        |
| xml_etree_generate      | 77.7 ms                                                               | 80.1 ms: 1.03x slower                                                       |
| scimark_sor             | 116 ms                                                                | 120 ms: 1.03x slower                                                        |
| coroutines              | 23.0 ms                                                               | 23.8 ms: 1.03x slower                                                       |
| json_loads              | 28.6 us                                                               | 29.6 us: 1.04x slower                                                       |
| create_gc_cycles        | 1.75 ms                                                               | 1.81 ms: 1.04x slower                                                       |
| regex_dna               | 210 ms                                                                | 218 ms: 1.04x slower                                                        |
| bench_mp_pool           | 24.0 ms                                                               | 24.9 ms: 1.04x slower                                                       |
| async_tree_io           | 924 ms                                                                | 961 ms: 1.04x slower                                                        |
| regex_effbot            | 3.51 ms                                                               | 3.65 ms: 1.04x slower                                                       |
| async_tree_none_tg      | 307 ms                                                                | 321 ms: 1.04x slower                                                        |
| richards_super          | 45.0 ms                                                               | 47.1 ms: 1.05x slower                                                       |
| async_tree_none         | 325 ms                                                                | 341 ms: 1.05x slower                                                        |
| go                      | 170 ms                                                                | 181 ms: 1.06x slower                                                        |
| asyncio_tcp             | 499 ms                                                                | 530 ms: 1.06x slower                                                        |
| gc_traversal            | 3.58 ms                                                               | 3.82 ms: 1.07x slower                                                       |
| 2to3                    | 276 ms                                                                | 294 ms: 1.07x slower                                                        |
| richards                | 38.6 ms                                                               | 41.4 ms: 1.07x slower                                                       |
| hexiom                  | 6.89 ms                                                               | 7.40 ms: 1.07x slower                                                       |
| regex_compile           | 142 ms                                                                | 152 ms: 1.07x slower                                                        |
| pyflate                 | 450 ms                                                                | 484 ms: 1.08x slower                                                        |
| async_tree_memoization  | 395 ms                                                                | 427 ms: 1.08x slower                                                        |
| logging_simple          | 5.54 us                                                               | 6.00 us: 1.08x slower                                                       |
| logging_format          | 6.04 us                                                               | 6.59 us: 1.09x slower                                                       |
| regex_v8                | 23.9 ms                                                               | 26.1 ms: 1.09x slower                                                       |
| bench_thread_pool       | 817 us                                                                | 893 us: 1.09x slower                                                        |
| sqlglot_normalize       | 113 ms                                                                | 125 ms: 1.10x slower                                                        |
| sympy_expand            | 504 ms                                                                | 559 ms: 1.11x slower                                                        |
| deltablue               | 3.18 ms                                                               | 3.56 ms: 1.12x slower                                                       |
| tomli_loads             | 1.92 sec                                                              | 2.15 sec: 1.12x slower                                                      |
| django_template         | 35.6 ms                                                               | 40.5 ms: 1.14x slower                                                       |
| pycparser               | 1.18 sec                                                              | 1.35 sec: 1.15x slower                                                      |
| sympy_str               | 299 ms                                                                | 345 ms: 1.15x slower                                                        |
| docutils                | 3.04 sec                                                              | 3.52 sec: 1.16x slower                                                      |
| sqlglot_optimize        | 58.1 ms                                                               | 67.6 ms: 1.16x slower                                                       |
| html5lib                | 63.4 ms                                                               | 74.3 ms: 1.17x slower                                                       |
| sympy_integrate         | 22.8 ms                                                               | 27.5 ms: 1.21x slower                                                       |
| tornado_http            | 94.7 ms                                                               | 118 ms: 1.24x slower                                                        |
| sympy_sum               | 171 ms                                                                | 217 ms: 1.27x slower                                                        |
| pylint                  | 372 ms                                                                | 483 ms: 1.30x slower                                                        |
| sqlglot_transpile       | 1.69 ms                                                               | 2.19 ms: 1.30x slower                                                       |
| sqlglot_parse           | 1.34 ms                                                               | 1.75 ms: 1.31x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.04x slower                                                                |

Benchmark hidden because not significant (12): deepcopy, xml_etree_parse, deepcopy_reduce, json, spectral_norm, typing_runtime_protocols, xml_etree_process, pathlib, genshi_xml, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.043x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.12x