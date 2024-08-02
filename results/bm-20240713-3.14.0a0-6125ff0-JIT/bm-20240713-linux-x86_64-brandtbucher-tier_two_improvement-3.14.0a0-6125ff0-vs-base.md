# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6125ff0
- commit date: 2024-07-13
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 275 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                              | 2.89 sec: 1.01x slower                                                      |
| html5lib       | 64.7 ms                                                               | 65.2 ms: 1.01x slower                                                       |
| tornado_http   | 92.4 ms                                                               | 93.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.80 ms: 1.01x faster                                                       |
| regex_dna      | 222 ms                                                                | 219 ms: 1.01x faster                                                        |
| regex_compile  | 134 ms                                                                | 136 ms: 1.01x slower                                                        |
| regex_v8       | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                       |
| json_loads           | 28.1 us                                                               | 27.9 us: 1.01x faster                                                       |
| tomli_loads          | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                                      |
| unpickle_pure_python | 215 us                                                                | 217 us: 1.01x slower                                                        |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| pickle_pure_python   | 293 us                                                                | 298 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.11 ms: 1.00x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.79 ms: 1.00x slower                                                       |
| django_template | 35.1 ms                                                               | 35.7 ms: 1.02x slower                                                       |
| genshi_xml      | 58.0 ms                                                               | 59.3 ms: 1.02x slower                                                       |
| genshi_text     | 24.9 ms                                                               | 26.2 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| bpe_tokeniser           | 4.84 sec                                                              | 4.60 sec: 1.05x faster                                                      |
| deepcopy_reduce         | 2.78 us                                                               | 2.72 us: 1.02x faster                                                       |
| crypto_pyaes            | 67.8 ms                                                               | 66.6 ms: 1.02x faster                                                       |
| regex_effbot            | 3.86 ms                                                               | 3.80 ms: 1.01x faster                                                       |
| json                    | 5.19 ms                                                               | 5.12 ms: 1.01x faster                                                       |
| regex_dna               | 222 ms                                                                | 219 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 710 ms                                                                | 701 ms: 1.01x faster                                                        |
| meteor_contest          | 107 ms                                                                | 105 ms: 1.01x faster                                                        |
| xml_etree_process       | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                       |
| json_loads              | 28.1 us                                                               | 27.9 us: 1.01x faster                                                       |
| asyncio_websockets      | 557 ms                                                                | 554 ms: 1.01x faster                                                        |
| gc_traversal            | 3.74 ms                                                               | 3.73 ms: 1.00x faster                                                       |
| pidigits                | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| create_gc_cycles        | 1.76 ms                                                               | 1.76 ms: 1.00x faster                                                       |
| python_startup_no_site  | 7.10 ms                                                               | 7.11 ms: 1.00x slower                                                       |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| mako                    | 9.76 ms                                                               | 9.79 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| deepcopy_memo           | 28.4 us                                                               | 28.5 us: 1.00x slower                                                       |
| coverage                | 92.4 ms                                                               | 93.0 ms: 1.01x slower                                                       |
| dulwich_log             | 67.1 ms                                                               | 67.5 ms: 1.01x slower                                                       |
| html5lib                | 64.7 ms                                                               | 65.2 ms: 1.01x slower                                                       |
| docutils                | 2.87 sec                                                              | 2.89 sec: 1.01x slower                                                      |
| tornado_http            | 92.4 ms                                                               | 93.3 ms: 1.01x slower                                                       |
| spectral_norm           | 104 ms                                                                | 105 ms: 1.01x slower                                                        |
| sqlglot_parse           | 1.27 ms                                                               | 1.29 ms: 1.01x slower                                                       |
| tomli_loads             | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                                      |
| pathlib                 | 16.2 ms                                                               | 16.4 ms: 1.01x slower                                                       |
| hexiom                  | 6.48 ms                                                               | 6.55 ms: 1.01x slower                                                       |
| unpickle_pure_python    | 215 us                                                                | 217 us: 1.01x slower                                                        |
| sympy_str               | 292 ms                                                                | 296 ms: 1.01x slower                                                        |
| go                      | 145 ms                                                                | 147 ms: 1.01x slower                                                        |
| regex_compile           | 134 ms                                                                | 136 ms: 1.01x slower                                                        |
| json_dumps              | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| pickle_pure_python      | 293 us                                                                | 298 us: 1.01x slower                                                        |
| 2to3                    | 271 ms                                                                | 275 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.60 ms                                                               | 1.62 ms: 1.02x slower                                                       |
| django_template         | 35.1 ms                                                               | 35.7 ms: 1.02x slower                                                       |
| regex_v8                | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                                       |
| async_generators        | 452 ms                                                                | 459 ms: 1.02x slower                                                        |
| fannkuch                | 361 ms                                                                | 368 ms: 1.02x slower                                                        |
| deltablue               | 3.52 ms                                                               | 3.59 ms: 1.02x slower                                                       |
| sympy_sum               | 165 ms                                                                | 168 ms: 1.02x slower                                                        |
| sympy_expand            | 492 ms                                                                | 502 ms: 1.02x slower                                                        |
| raytrace                | 266 ms                                                                | 271 ms: 1.02x slower                                                        |
| genshi_xml              | 58.0 ms                                                               | 59.3 ms: 1.02x slower                                                       |
| scimark_lu              | 124 ms                                                                | 127 ms: 1.02x slower                                                        |
| sqlglot_optimize        | 55.0 ms                                                               | 56.3 ms: 1.02x slower                                                       |
| sympy_integrate         | 21.8 ms                                                               | 22.4 ms: 1.03x slower                                                       |
| logging_simple          | 5.42 us                                                               | 5.56 us: 1.03x slower                                                       |
| asyncio_tcp             | 488 ms                                                                | 503 ms: 1.03x slower                                                        |
| logging_format          | 5.94 us                                                               | 6.12 us: 1.03x slower                                                       |
| sqlglot_normalize       | 111 ms                                                                | 115 ms: 1.03x slower                                                        |
| scimark_fft             | 309 ms                                                                | 319 ms: 1.03x slower                                                        |
| richards                | 41.8 ms                                                               | 43.9 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult | 4.28 ms                                                               | 4.49 ms: 1.05x slower                                                       |
| genshi_text             | 24.9 ms                                                               | 26.2 ms: 1.05x slower                                                       |
| richards_super          | 47.5 ms                                                               | 50.2 ms: 1.06x slower                                                       |
| mdp                     | 2.52 sec                                                              | 2.68 sec: 1.06x slower                                                      |
| generators              | 29.5 ms                                                               | 38.6 ms: 1.31x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (31): xml_etree_parse, telco, pyflate, logging_silent, thrift, typing_runtime_protocols, coroutines, pprint_pformat, xml_etree_generate, nbody, xml_etree_iterparse, bench_thread_pool, bench_mp_pool, comprehensions, nqueens, dask, scimark_sor, float, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed_tg, scimark_monte_carlo, pycparser, chaos, deepcopy, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x