# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 190fbfa
- commit date: 2024-07-14
- overall geometric mean: 1.02x slower
- HPT reliability: 98.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 273 ms: 1.00x slower                                                      |
| docutils       | 2.88 sec                                                              | 2.98 sec: 1.03x slower                                                    |
| html5lib       | 65.4 ms                                                               | 71.6 ms: 1.10x slower                                                     |
| tornado_http   | 93.8 ms                                                               | 98.3 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg | 850 ms                                                                | 867 ms: 1.02x slower                                                      |
| async_tree_io    | 842 ms                                                                | 910 ms: 1.08x slower                                                      |
| Geometric mean   | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 79.5 ms                                                               | 77.0 ms: 1.03x faster                                                     |
| pidigits       | 185 ms                                                                | 188 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                               | 23.7 ms: 1.08x faster                                                     |
| regex_effbot   | 3.84 ms                                                               | 3.61 ms: 1.06x faster                                                     |
| regex_dna      | 227 ms                                                                | 219 ms: 1.04x faster                                                      |
| regex_compile  | 135 ms                                                                | 132 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 215 us: 1.01x faster                                                      |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| xml_etree_process    | 57.5 ms                                                               | 58.6 ms: 1.02x slower                                                     |
| pickle_pure_python   | 296 us                                                                | 304 us: 1.03x slower                                                      |
| xml_etree_generate   | 81.1 ms                                                               | 84.3 ms: 1.04x slower                                                     |
| xml_etree_iterparse  | 99.0 ms                                                               | 103 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.77 ms                                                               | 9.96 ms: 1.02x slower                                                     |
| genshi_text     | 25.1 ms                                                               | 27.7 ms: 1.11x slower                                                     |
| genshi_xml      | 56.9 ms                                                               | 63.3 ms: 1.11x slower                                                     |
| django_template | 36.1 ms                                                               | 40.4 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.09x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                | 25.5 ms                                                               | 23.7 ms: 1.08x faster                                                     |
| deepcopy_memo           | 28.4 us                                                               | 26.6 us: 1.07x faster                                                     |
| regex_effbot            | 3.84 ms                                                               | 3.61 ms: 1.06x faster                                                     |
| richards                | 41.5 ms                                                               | 39.1 ms: 1.06x faster                                                     |
| deepcopy                | 274 us                                                                | 258 us: 1.06x faster                                                      |
| scimark_lu              | 126 ms                                                                | 119 ms: 1.06x faster                                                      |
| logging_silent          | 108 ns                                                                | 102 ns: 1.06x faster                                                      |
| richards_super          | 47.7 ms                                                               | 45.3 ms: 1.05x faster                                                     |
| pycparser               | 1.19 sec                                                              | 1.13 sec: 1.05x faster                                                    |
| deltablue               | 3.58 ms                                                               | 3.42 ms: 1.05x faster                                                     |
| go                      | 146 ms                                                                | 140 ms: 1.04x faster                                                      |
| scimark_sor             | 131 ms                                                                | 127 ms: 1.04x faster                                                      |
| regex_dna               | 227 ms                                                                | 219 ms: 1.04x faster                                                      |
| chaos                   | 57.8 ms                                                               | 56.0 ms: 1.03x faster                                                     |
| nbody                   | 79.5 ms                                                               | 77.0 ms: 1.03x faster                                                     |
| deepcopy_reduce         | 2.76 us                                                               | 2.68 us: 1.03x faster                                                     |
| regex_compile           | 135 ms                                                                | 132 ms: 1.03x faster                                                      |
| dulwich_log             | 68.0 ms                                                               | 66.7 ms: 1.02x faster                                                     |
| bpe_tokeniser           | 4.82 sec                                                              | 4.73 sec: 1.02x faster                                                    |
| meteor_contest          | 108 ms                                                                | 106 ms: 1.01x faster                                                      |
| logging_simple          | 5.61 us                                                               | 5.54 us: 1.01x faster                                                     |
| logging_format          | 6.16 us                                                               | 6.09 us: 1.01x faster                                                     |
| sympy_expand            | 493 ms                                                                | 489 ms: 1.01x faster                                                      |
| json                    | 5.15 ms                                                               | 5.10 ms: 1.01x faster                                                     |
| hexiom                  | 6.56 ms                                                               | 6.52 ms: 1.01x faster                                                     |
| unpickle_pure_python    | 217 us                                                                | 215 us: 1.01x faster                                                      |
| raytrace                | 271 ms                                                                | 269 ms: 1.01x faster                                                      |
| spectral_norm           | 101 ms                                                                | 101 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 113 ms                                                                | 113 ms: 1.01x faster                                                      |
| create_gc_cycles        | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                     |
| crypto_pyaes            | 67.0 ms                                                               | 66.7 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult | 4.37 ms                                                               | 4.36 ms: 1.00x faster                                                     |
| python_startup_no_site  | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| 2to3                    | 272 ms                                                                | 273 ms: 1.00x slower                                                      |
| python_startup          | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                    |
| pyflate                 | 446 ms                                                                | 449 ms: 1.01x slower                                                      |
| telco                   | 7.92 ms                                                               | 8.00 ms: 1.01x slower                                                     |
| thrift                  | 799 us                                                                | 807 us: 1.01x slower                                                      |
| mdp                     | 2.71 sec                                                              | 2.74 sec: 1.01x slower                                                    |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| sqlglot_transpile       | 1.60 ms                                                               | 1.62 ms: 1.01x slower                                                     |
| pidigits                | 185 ms                                                                | 188 ms: 1.01x slower                                                      |
| mako                    | 9.77 ms                                                               | 9.96 ms: 1.02x slower                                                     |
| async_tree_io_tg        | 850 ms                                                                | 867 ms: 1.02x slower                                                      |
| xml_etree_process       | 57.5 ms                                                               | 58.6 ms: 1.02x slower                                                     |
| sympy_str               | 293 ms                                                                | 300 ms: 1.02x slower                                                      |
| gc_traversal            | 3.64 ms                                                               | 3.73 ms: 1.02x slower                                                     |
| scimark_fft             | 305 ms                                                                | 313 ms: 1.02x slower                                                      |
| pickle_pure_python      | 296 us                                                                | 304 us: 1.03x slower                                                      |
| asyncio_tcp             | 504 ms                                                                | 518 ms: 1.03x slower                                                      |
| sqlglot_optimize        | 55.7 ms                                                               | 57.3 ms: 1.03x slower                                                     |
| bench_thread_pool       | 833 us                                                                | 857 us: 1.03x slower                                                      |
| docutils                | 2.88 sec                                                              | 2.98 sec: 1.03x slower                                                    |
| xml_etree_generate      | 81.1 ms                                                               | 84.3 ms: 1.04x slower                                                     |
| scimark_monte_carlo     | 60.8 ms                                                               | 63.4 ms: 1.04x slower                                                     |
| xml_etree_iterparse     | 99.0 ms                                                               | 103 ms: 1.04x slower                                                      |
| tornado_http            | 93.8 ms                                                               | 98.3 ms: 1.05x slower                                                     |
| dask                    | 363 ms                                                                | 384 ms: 1.06x slower                                                      |
| async_tree_io           | 842 ms                                                                | 910 ms: 1.08x slower                                                      |
| pylint                  | 336 ms                                                                | 368 ms: 1.09x slower                                                      |
| html5lib                | 65.4 ms                                                               | 71.6 ms: 1.10x slower                                                     |
| genshi_text             | 25.1 ms                                                               | 27.7 ms: 1.11x slower                                                     |
| genshi_xml              | 56.9 ms                                                               | 63.3 ms: 1.11x slower                                                     |
| django_template         | 36.1 ms                                                               | 40.4 ms: 1.12x slower                                                     |
| async_generators        | 455 ms                                                                | 514 ms: 1.13x slower                                                      |
| nqueens                 | 86.2 ms                                                               | 97.5 ms: 1.13x slower                                                     |
| sympy_integrate         | 21.9 ms                                                               | 25.3 ms: 1.15x slower                                                     |
| coroutines              | 23.5 ms                                                               | 27.6 ms: 1.17x slower                                                     |
| generators              | 29.8 ms                                                               | 56.1 ms: 1.88x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (21): comprehensions, coverage, sqlglot_parse, json_loads, pprint_safe_repr, asyncio_websockets, async_tree_cpu_io_mixed, xml_etree_parse, pathlib, async_tree_cpu_io_mixed_tg, tomli_loads, pprint_pformat, float, bench_mp_pool, typing_runtime_protocols, sympy_sum, async_tree_none, fannkuch, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 98.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x