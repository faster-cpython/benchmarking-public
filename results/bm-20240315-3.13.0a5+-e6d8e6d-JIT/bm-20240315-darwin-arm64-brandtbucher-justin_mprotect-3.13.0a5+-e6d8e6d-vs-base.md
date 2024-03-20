# Results vs. base

- fork: brandtbucher
- ref: justin_mprotect
- machine: darwin-arm64
- commit hash: e6d8e6d
- commit date: 2024-03-15
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                 | 183 ms: 1.02x faster                                                    |
| chameleon      | 4.87 ms                                                                | 4.84 ms: 1.01x faster                                                   |
| docutils       | 1.53 sec                                                               | 1.52 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager | 70.4 ms                                                                | 70.0 ms: 1.01x faster                                                   |
| async_tree_io    | 710 ms                                                                 | 706 ms: 1.00x faster                                                    |
| async_tree_io_tg | 675 ms                                                                 | 673 ms: 1.00x faster                                                    |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (13): async_tree_eager_io, async_tree_memoization, async_tree_none, async_tree_eager_memoization, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                                 | 282 ms: 1.00x faster                                                    |
| nbody          | 70.2 ms                                                                | 70.4 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                                | 2.63 ms: 1.00x faster                                                   |
| regex_v8       | 17.2 ms                                                                | 17.3 ms: 1.00x slower                                                   |
| regex_dna      | 152 ms                                                                 | 153 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|--------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads        | 1.36 sec                                                               | 1.33 sec: 1.02x faster                                                  |
| xml_etree_generate | 56.8 ms                                                                | 55.8 ms: 1.02x faster                                                   |
| pickle             | 7.29 us                                                                | 7.24 us: 1.01x faster                                                   |
| pickle_dict        | 18.2 us                                                                | 18.1 us: 1.01x faster                                                   |
| xml_etree_process  | 39.0 ms                                                                | 38.8 ms: 1.00x faster                                                   |
| json_dumps         | 6.47 ms                                                                | 6.49 ms: 1.00x slower                                                   |
| pickle_pure_python | 196 us                                                                 | 198 us: 1.01x slower                                                    |
| unpickle_list      | 3.05 us                                                                | 3.11 us: 1.02x slower                                                   |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (6): unpickle_pure_python, unpickle, json_loads, pickle_list, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 16.7 ms                                                                | 15.2 ms: 1.10x faster                                                   |
| python_startup         | 18.5 ms                                                                | 16.8 ms: 1.10x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.10x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 36.9 ms                                                                | 34.2 ms: 1.08x faster                                                   |
| genshi_text    | 15.8 ms                                                                | 15.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark               | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| fannkuch                | 311 ms                                                                 | 256 ms: 1.21x faster                                                    |
| richards                | 37.5 ms                                                                | 33.3 ms: 1.12x faster                                                   |
| richards_super          | 41.5 ms                                                                | 37.1 ms: 1.12x faster                                                   |
| python_startup_no_site  | 16.7 ms                                                                | 15.2 ms: 1.10x faster                                                   |
| python_startup          | 18.5 ms                                                                | 16.8 ms: 1.10x faster                                                   |
| asyncio_tcp             | 440 ms                                                                 | 408 ms: 1.08x faster                                                    |
| genshi_xml              | 36.9 ms                                                                | 34.2 ms: 1.08x faster                                                   |
| go                      | 115 ms                                                                 | 110 ms: 1.04x faster                                                    |
| bench_mp_pool           | 53.2 ms                                                                | 51.3 ms: 1.04x faster                                                   |
| pyflate                 | 343 ms                                                                 | 331 ms: 1.04x faster                                                    |
| hexiom                  | 5.13 ms                                                                | 4.97 ms: 1.03x faster                                                   |
| pprint_safe_repr        | 519 ms                                                                 | 504 ms: 1.03x faster                                                    |
| 2to3                    | 187 ms                                                                 | 183 ms: 1.02x faster                                                    |
| pprint_pformat          | 1.06 sec                                                               | 1.04 sec: 1.02x faster                                                  |
| sqlglot_transpile       | 1.02 ms                                                                | 1.00 ms: 1.02x faster                                                   |
| sqlglot_parse           | 831 us                                                                 | 814 us: 1.02x faster                                                    |
| telco                   | 4.58 ms                                                                | 4.49 ms: 1.02x faster                                                   |
| tomli_loads             | 1.36 sec                                                               | 1.33 sec: 1.02x faster                                                  |
| xml_etree_generate      | 56.8 ms                                                                | 55.8 ms: 1.02x faster                                                   |
| deepcopy_reduce         | 2.00 us                                                                | 1.97 us: 1.02x faster                                                   |
| pycparser               | 727 ms                                                                 | 717 ms: 1.01x faster                                                    |
| logging_simple          | 3.50 us                                                                | 3.45 us: 1.01x faster                                                   |
| sqlglot_optimize        | 35.4 ms                                                                | 35.0 ms: 1.01x faster                                                   |
| scimark_lu              | 85.7 ms                                                                | 84.9 ms: 1.01x faster                                                   |
| deepcopy                | 231 us                                                                 | 229 us: 1.01x faster                                                    |
| logging_format          | 3.79 us                                                                | 3.76 us: 1.01x faster                                                   |
| mdp                     | 1.62 sec                                                               | 1.61 sec: 1.01x faster                                                  |
| scimark_sparse_mat_mult | 3.15 ms                                                                | 3.13 ms: 1.01x faster                                                   |
| crypto_pyaes            | 47.7 ms                                                                | 47.4 ms: 1.01x faster                                                   |
| raytrace                | 192 ms                                                                 | 190 ms: 1.01x faster                                                    |
| comprehensions          | 12.6 us                                                                | 12.5 us: 1.01x faster                                                   |
| meteor_contest          | 75.2 ms                                                                | 74.7 ms: 1.01x faster                                                   |
| pickle                  | 7.29 us                                                                | 7.24 us: 1.01x faster                                                   |
| genshi_text             | 15.8 ms                                                                | 15.7 ms: 1.01x faster                                                   |
| sympy_str               | 145 ms                                                                 | 144 ms: 1.01x faster                                                    |
| async_tree_eager        | 70.4 ms                                                                | 70.0 ms: 1.01x faster                                                   |
| sympy_integrate         | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                   |
| chaos                   | 40.4 ms                                                                | 40.1 ms: 1.01x faster                                                   |
| chameleon               | 4.87 ms                                                                | 4.84 ms: 1.01x faster                                                   |
| nqueens                 | 64.2 ms                                                                | 63.8 ms: 1.01x faster                                                   |
| async_generators        | 313 ms                                                                 | 311 ms: 1.01x faster                                                    |
| docutils                | 1.53 sec                                                               | 1.52 sec: 1.01x faster                                                  |
| pickle_dict             | 18.2 us                                                                | 18.1 us: 1.01x faster                                                   |
| async_tree_io           | 710 ms                                                                 | 706 ms: 1.00x faster                                                    |
| pidigits                | 283 ms                                                                 | 282 ms: 1.00x faster                                                    |
| xml_etree_process       | 39.0 ms                                                                | 38.8 ms: 1.00x faster                                                   |
| scimark_fft             | 200 ms                                                                 | 199 ms: 1.00x faster                                                    |
| scimark_sor             | 111 ms                                                                 | 111 ms: 1.00x faster                                                    |
| async_tree_io_tg        | 675 ms                                                                 | 673 ms: 1.00x faster                                                    |
| sympy_expand            | 249 ms                                                                 | 248 ms: 1.00x faster                                                    |
| regex_effbot            | 2.63 ms                                                                | 2.63 ms: 1.00x faster                                                   |
| logging_silent          | 72.3 ns                                                                | 72.2 ns: 1.00x faster                                                   |
| regex_v8                | 17.2 ms                                                                | 17.3 ms: 1.00x slower                                                   |
| nbody                   | 70.2 ms                                                                | 70.4 ms: 1.00x slower                                                   |
| thrift                  | 461 us                                                                 | 463 us: 1.00x slower                                                    |
| json_dumps              | 6.47 ms                                                                | 6.49 ms: 1.00x slower                                                   |
| deepcopy_memo           | 26.2 us                                                                | 26.2 us: 1.00x slower                                                   |
| regex_dna               | 152 ms                                                                 | 153 ms: 1.01x slower                                                    |
| pickle_pure_python      | 196 us                                                                 | 198 us: 1.01x slower                                                    |
| sqlite_synth            | 1.58 us                                                                | 1.59 us: 1.01x slower                                                   |
| coroutines              | 18.1 ms                                                                | 18.3 ms: 1.01x slower                                                   |
| scimark_monte_carlo     | 44.2 ms                                                                | 44.9 ms: 1.01x slower                                                   |
| unpickle_list           | 3.05 us                                                                | 3.11 us: 1.02x slower                                                   |
| coverage                | 47.9 ms                                                                | 48.9 ms: 1.02x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (45): async_tree_eager_io, dask, html5lib, pathlib, async_tree_memoization, async_tree_none, async_tree_eager_memoization, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, asyncio_tcp_ssl, async_tree_eager_io_tg, sympy_sum, mako, unpickle_pure_python, async_tree_eager_cpu_io_mixed_tg, pylint, spectral_norm, unpack_sequence, async_tree_cpu_io_mixed, unpickle, dulwich_log, deltablue, async_tree_cpu_io_mixed_tg, json, gc_traversal, json_loads, async_tree_eager_tg, bench_thread_pool, django_template, async_tree_eager_memoization_tg, generators, async_tree_none_tg, float, asyncio_websockets, mypy2, sqlglot_normalize, create_gc_cycles, gunicorn, pickle_list, regex_compile, typing_runtime_protocols, xml_etree_parse, xml_etree_iterparse, aiohttp, tornado_http


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.80x