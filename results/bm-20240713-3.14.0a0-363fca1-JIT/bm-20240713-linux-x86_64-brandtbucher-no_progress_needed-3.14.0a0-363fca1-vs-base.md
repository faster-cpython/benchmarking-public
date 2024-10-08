# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 363fca1
- commit date: 2024-07-13
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 290 ms: 1.07x slower                                                      |
| docutils       | 2.87 sec                                                              | 7.91 sec: 2.76x slower                                                    |
| html5lib       | 64.7 ms                                                               | 76.3 ms: 1.18x slower                                                     |
| tornado_http   | 92.4 ms                                                               | 95.1 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.38x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 70.0 ms                                                               | 70.5 ms: 1.01x slower                                                     |
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                               | 25.4 ms: 1.00x slower                                                     |
| regex_dna      | 222 ms                                                                | 224 ms: 1.01x slower                                                      |
| regex_compile  | 134 ms                                                                | 135 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 28.1 us                                                               | 27.6 us: 1.02x faster                                                     |
| tomli_loads          | 1.92 sec                                                              | 1.90 sec: 1.01x faster                                                    |
| unpickle_pure_python | 215 us                                                                | 213 us: 1.01x faster                                                      |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| xml_etree_generate   | 81.6 ms                                                               | 84.4 ms: 1.03x slower                                                     |
| xml_etree_process    | 57.5 ms                                                               | 59.8 ms: 1.04x slower                                                     |
| pickle_pure_python   | 293 us                                                                | 313 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.08 ms: 1.00x faster                                                     |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.81 ms: 1.00x slower                                                     |
| django_template | 35.1 ms                                                               | 38.6 ms: 1.10x slower                                                     |
| genshi_xml      | 58.0 ms                                                               | 75.1 ms: 1.30x slower                                                     |
| genshi_text     | 24.9 ms                                                               | 34.1 ms: 1.37x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.18x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_lu              | 124 ms                                                                | 117 ms: 1.06x faster                                                      |
| richards                | 41.8 ms                                                               | 39.3 ms: 1.06x faster                                                     |
| deepcopy_memo           | 28.4 us                                                               | 26.9 us: 1.06x faster                                                     |
| gc_traversal            | 3.74 ms                                                               | 3.55 ms: 1.05x faster                                                     |
| logging_silent          | 107 ns                                                                | 102 ns: 1.05x faster                                                      |
| richards_super          | 47.5 ms                                                               | 45.5 ms: 1.04x faster                                                     |
| spectral_norm           | 104 ms                                                                | 101 ms: 1.04x faster                                                      |
| deepcopy_reduce         | 2.78 us                                                               | 2.69 us: 1.03x faster                                                     |
| json_loads              | 28.1 us                                                               | 27.6 us: 1.02x faster                                                     |
| bpe_tokeniser           | 4.84 sec                                                              | 4.75 sec: 1.02x faster                                                    |
| scimark_sparse_mat_mult | 4.28 ms                                                               | 4.20 ms: 1.02x faster                                                     |
| json                    | 5.19 ms                                                               | 5.11 ms: 1.02x faster                                                     |
| tomli_loads             | 1.92 sec                                                              | 1.90 sec: 1.01x faster                                                    |
| telco                   | 8.08 ms                                                               | 7.99 ms: 1.01x faster                                                     |
| coroutines              | 23.4 ms                                                               | 23.2 ms: 1.01x faster                                                     |
| pathlib                 | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                                     |
| unpickle_pure_python    | 215 us                                                                | 213 us: 1.01x faster                                                      |
| create_gc_cycles        | 1.76 ms                                                               | 1.75 ms: 1.00x faster                                                     |
| python_startup_no_site  | 7.10 ms                                                               | 7.08 ms: 1.00x faster                                                     |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| dulwich_log             | 67.1 ms                                                               | 67.3 ms: 1.00x slower                                                     |
| mako                    | 9.76 ms                                                               | 9.81 ms: 1.00x slower                                                     |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                    |
| regex_v8                | 25.3 ms                                                               | 25.4 ms: 1.00x slower                                                     |
| sympy_sum               | 165 ms                                                                | 166 ms: 1.00x slower                                                      |
| float                   | 70.0 ms                                                               | 70.5 ms: 1.01x slower                                                     |
| json_dumps              | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| logging_simple          | 5.42 us                                                               | 5.47 us: 1.01x slower                                                     |
| pidigits                | 186 ms                                                                | 188 ms: 1.01x slower                                                      |
| async_generators        | 452 ms                                                                | 456 ms: 1.01x slower                                                      |
| sympy_expand            | 492 ms                                                                | 497 ms: 1.01x slower                                                      |
| regex_dna               | 222 ms                                                                | 224 ms: 1.01x slower                                                      |
| coverage                | 92.4 ms                                                               | 93.4 ms: 1.01x slower                                                     |
| regex_compile           | 134 ms                                                                | 135 ms: 1.01x slower                                                      |
| pyflate                 | 444 ms                                                                | 452 ms: 1.02x slower                                                      |
| fannkuch                | 361 ms                                                                | 367 ms: 1.02x slower                                                      |
| go                      | 145 ms                                                                | 147 ms: 1.02x slower                                                      |
| dask                    | 362 ms                                                                | 369 ms: 1.02x slower                                                      |
| meteor_contest          | 107 ms                                                                | 109 ms: 1.02x slower                                                      |
| logging_format          | 5.94 us                                                               | 6.06 us: 1.02x slower                                                     |
| generators              | 29.5 ms                                                               | 30.2 ms: 1.02x slower                                                     |
| scimark_monte_carlo     | 61.1 ms                                                               | 62.7 ms: 1.03x slower                                                     |
| tornado_http            | 92.4 ms                                                               | 95.1 ms: 1.03x slower                                                     |
| sympy_str               | 292 ms                                                                | 300 ms: 1.03x slower                                                      |
| hexiom                  | 6.48 ms                                                               | 6.67 ms: 1.03x slower                                                     |
| asyncio_tcp             | 488 ms                                                                | 503 ms: 1.03x slower                                                      |
| pprint_safe_repr        | 710 ms                                                                | 735 ms: 1.03x slower                                                      |
| xml_etree_generate      | 81.6 ms                                                               | 84.4 ms: 1.03x slower                                                     |
| xml_etree_process       | 57.5 ms                                                               | 59.8 ms: 1.04x slower                                                     |
| pprint_pformat          | 1.45 sec                                                              | 1.51 sec: 1.04x slower                                                    |
| sqlglot_parse           | 1.27 ms                                                               | 1.34 ms: 1.05x slower                                                     |
| sqlglot_transpile       | 1.60 ms                                                               | 1.68 ms: 1.05x slower                                                     |
| pickle_pure_python      | 293 us                                                                | 313 us: 1.06x slower                                                      |
| 2to3                    | 271 ms                                                                | 290 ms: 1.07x slower                                                      |
| nqueens                 | 85.5 ms                                                               | 91.4 ms: 1.07x slower                                                     |
| sqlglot_optimize        | 55.0 ms                                                               | 58.9 ms: 1.07x slower                                                     |
| mdp                     | 2.52 sec                                                              | 2.73 sec: 1.08x slower                                                    |
| django_template         | 35.1 ms                                                               | 38.6 ms: 1.10x slower                                                     |
| deltablue               | 3.52 ms                                                               | 3.94 ms: 1.12x slower                                                     |
| sympy_integrate         | 21.8 ms                                                               | 24.5 ms: 1.12x slower                                                     |
| bench_thread_pool       | 832 us                                                                | 958 us: 1.15x slower                                                      |
| pylint                  | 334 ms                                                                | 390 ms: 1.17x slower                                                      |
| html5lib                | 64.7 ms                                                               | 76.3 ms: 1.18x slower                                                     |
| genshi_xml              | 58.0 ms                                                               | 75.1 ms: 1.30x slower                                                     |
| genshi_text             | 24.9 ms                                                               | 34.1 ms: 1.37x slower                                                     |
| docutils                | 2.87 sec                                                              | 7.91 sec: 2.76x slower                                                    |
| raytrace                | 266 ms                                                                | 5.99 sec: 22.56x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.07x slower                                                              |

Benchmark hidden because not significant (24): deepcopy, pycparser, crypto_pyaes, thrift, chaos, typing_runtime_protocols, nbody, xml_etree_parse, asyncio_websockets, xml_etree_iterparse, bench_mp_pool, scimark_fft, regex_effbot, comprehensions, sqlglot_normalize, async_tree_memoization_tg, scimark_sor, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_memoization

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x