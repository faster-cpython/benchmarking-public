# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 363fca1
- commit date: 2024-07-13
- overall geometric mean: 1.06x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 290 ms: 1.07x slower                                                      |
| docutils       | 2.88 sec                                                              | 7.91 sec: 2.74x slower                                                    |
| html5lib       | 65.4 ms                                                               | 76.3 ms: 1.17x slower                                                     |
| tornado_http   | 93.8 ms                                                               | 95.1 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.36x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 188 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                | 224 ms: 1.01x faster                                                      |
| regex_v8       | 25.5 ms                                                               | 25.4 ms: 1.00x faster                                                     |
| regex_effbot   | 3.84 ms                                                               | 3.86 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 213 us: 1.02x faster                                                      |
| tomli_loads          | 1.93 sec                                                              | 1.90 sec: 1.02x faster                                                    |
| xml_etree_iterparse  | 99.0 ms                                                               | 99.3 ms: 1.00x slower                                                     |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                     |
| xml_etree_generate   | 81.1 ms                                                               | 84.4 ms: 1.04x slower                                                     |
| xml_etree_process    | 57.5 ms                                                               | 59.8 ms: 1.04x slower                                                     |
| pickle_pure_python   | 296 us                                                                | 313 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.08 ms: 1.00x faster                                                     |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.77 ms                                                               | 9.81 ms: 1.00x slower                                                     |
| django_template | 36.1 ms                                                               | 38.6 ms: 1.07x slower                                                     |
| genshi_xml      | 56.9 ms                                                               | 75.1 ms: 1.32x slower                                                     |
| genshi_text     | 25.1 ms                                                               | 34.1 ms: 1.36x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.18x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_lu              | 126 ms                                                                | 117 ms: 1.08x faster                                                      |
| logging_silent          | 108 ns                                                                | 102 ns: 1.06x faster                                                      |
| richards                | 41.5 ms                                                               | 39.3 ms: 1.06x faster                                                     |
| deepcopy_memo           | 28.4 us                                                               | 26.9 us: 1.06x faster                                                     |
| richards_super          | 47.7 ms                                                               | 45.5 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult | 4.37 ms                                                               | 4.20 ms: 1.04x faster                                                     |
| logging_simple          | 5.61 us                                                               | 5.47 us: 1.03x faster                                                     |
| gc_traversal            | 3.64 ms                                                               | 3.55 ms: 1.03x faster                                                     |
| deepcopy_reduce         | 2.76 us                                                               | 2.69 us: 1.02x faster                                                     |
| unpickle_pure_python    | 217 us                                                                | 213 us: 1.02x faster                                                      |
| deepcopy                | 274 us                                                                | 270 us: 1.02x faster                                                      |
| logging_format          | 6.16 us                                                               | 6.06 us: 1.02x faster                                                     |
| scimark_sor             | 131 ms                                                                | 129 ms: 1.02x faster                                                      |
| tomli_loads             | 1.93 sec                                                              | 1.90 sec: 1.02x faster                                                    |
| regex_dna               | 227 ms                                                                | 224 ms: 1.01x faster                                                      |
| coroutines              | 23.5 ms                                                               | 23.2 ms: 1.01x faster                                                     |
| bpe_tokeniser           | 4.82 sec                                                              | 4.75 sec: 1.01x faster                                                    |
| sqlglot_normalize       | 113 ms                                                                | 112 ms: 1.01x faster                                                      |
| pycparser               | 1.19 sec                                                              | 1.17 sec: 1.01x faster                                                    |
| dulwich_log             | 68.0 ms                                                               | 67.3 ms: 1.01x faster                                                     |
| sympy_sum               | 167 ms                                                                | 166 ms: 1.01x faster                                                      |
| spectral_norm           | 101 ms                                                                | 101 ms: 1.01x faster                                                      |
| create_gc_cycles        | 1.77 ms                                                               | 1.75 ms: 1.01x faster                                                     |
| regex_v8                | 25.5 ms                                                               | 25.4 ms: 1.00x faster                                                     |
| python_startup_no_site  | 7.11 ms                                                               | 7.08 ms: 1.00x faster                                                     |
| asyncio_tcp             | 504 ms                                                                | 503 ms: 1.00x faster                                                      |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                    |
| xml_etree_iterparse     | 99.0 ms                                                               | 99.3 ms: 1.00x slower                                                     |
| mako                    | 9.77 ms                                                               | 9.81 ms: 1.00x slower                                                     |
| crypto_pyaes            | 67.0 ms                                                               | 67.4 ms: 1.01x slower                                                     |
| regex_effbot            | 3.84 ms                                                               | 3.86 ms: 1.01x slower                                                     |
| sympy_expand            | 493 ms                                                                | 497 ms: 1.01x slower                                                      |
| pathlib                 | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                     |
| mdp                     | 2.71 sec                                                              | 2.73 sec: 1.01x slower                                                    |
| telco                   | 7.92 ms                                                               | 7.99 ms: 1.01x slower                                                     |
| go                      | 146 ms                                                                | 147 ms: 1.01x slower                                                      |
| meteor_contest          | 108 ms                                                                | 109 ms: 1.01x slower                                                      |
| scimark_fft             | 305 ms                                                                | 309 ms: 1.01x slower                                                      |
| pyflate                 | 446 ms                                                                | 452 ms: 1.01x slower                                                      |
| tornado_http            | 93.8 ms                                                               | 95.1 ms: 1.01x slower                                                     |
| generators              | 29.8 ms                                                               | 30.2 ms: 1.01x slower                                                     |
| pidigits                | 185 ms                                                                | 188 ms: 1.01x slower                                                      |
| hexiom                  | 6.56 ms                                                               | 6.67 ms: 1.02x slower                                                     |
| json_dumps              | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                     |
| dask                    | 363 ms                                                                | 369 ms: 1.02x slower                                                      |
| sympy_str               | 293 ms                                                                | 300 ms: 1.02x slower                                                      |
| pprint_safe_repr        | 716 ms                                                                | 735 ms: 1.03x slower                                                      |
| scimark_monte_carlo     | 60.8 ms                                                               | 62.7 ms: 1.03x slower                                                     |
| pprint_pformat          | 1.46 sec                                                              | 1.51 sec: 1.03x slower                                                    |
| xml_etree_generate      | 81.1 ms                                                               | 84.4 ms: 1.04x slower                                                     |
| xml_etree_process       | 57.5 ms                                                               | 59.8 ms: 1.04x slower                                                     |
| sqlglot_parse           | 1.28 ms                                                               | 1.34 ms: 1.05x slower                                                     |
| sqlglot_transpile       | 1.60 ms                                                               | 1.68 ms: 1.05x slower                                                     |
| pickle_pure_python      | 296 us                                                                | 313 us: 1.06x slower                                                      |
| sqlglot_optimize        | 55.7 ms                                                               | 58.9 ms: 1.06x slower                                                     |
| nqueens                 | 86.2 ms                                                               | 91.4 ms: 1.06x slower                                                     |
| 2to3                    | 272 ms                                                                | 290 ms: 1.07x slower                                                      |
| django_template         | 36.1 ms                                                               | 38.6 ms: 1.07x slower                                                     |
| deltablue               | 3.58 ms                                                               | 3.94 ms: 1.10x slower                                                     |
| sympy_integrate         | 21.9 ms                                                               | 24.5 ms: 1.12x slower                                                     |
| bench_thread_pool       | 833 us                                                                | 958 us: 1.15x slower                                                      |
| pylint                  | 336 ms                                                                | 390 ms: 1.16x slower                                                      |
| html5lib                | 65.4 ms                                                               | 76.3 ms: 1.17x slower                                                     |
| genshi_xml              | 56.9 ms                                                               | 75.1 ms: 1.32x slower                                                     |
| genshi_text             | 25.1 ms                                                               | 34.1 ms: 1.36x slower                                                     |
| docutils                | 2.88 sec                                                              | 7.91 sec: 2.74x slower                                                    |
| raytrace                | 271 ms                                                                | 5.99 sec: 22.10x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.06x slower                                                              |

Benchmark hidden because not significant (23): json, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, thrift, comprehensions, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, chaos, regex_compile, async_tree_none, bench_mp_pool, async_generators, float, json_loads, nbody, typing_runtime_protocols, async_tree_memoization, coverage, fannkuch, async_tree_io, xml_etree_parse

# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x