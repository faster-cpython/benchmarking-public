
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: fd42c63
- commit date: 2023-03-09
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                        |
| docutils       | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                       |
| html5lib       | 64.5 ms                                                | 62.8 ms: 1.03x faster                                                        |
| tornado_http   | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.7 ms: 1.03x faster                                                        |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                         |
| nbody          | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                        |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                                         |
| regex_dna      | 204 ms                                                 | 199 ms: 1.02x faster                                                         |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.42 ms: 1.34x faster                                                        |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 207 us: 1.10x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.06x faster                                                         |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                                        |
| pickle_list          | 4.11 us                                                | 4.07 us: 1.01x faster                                                        |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                        |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 81.9 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.9 ms: 1.08x faster                                                        |
| mako            | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                        |
| django_template | 32.6 ms                                                | 33.5 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.9 ms: 2.37x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.42 ms: 1.34x faster                                                        |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.28 ms: 1.12x faster                                                        |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 207 us: 1.10x faster                                                         |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                        |
| coroutines              | 25.5 ms                                                | 23.5 ms: 1.08x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 47.9 ms: 1.08x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                        |
| scimark_sor             | 118 ms                                                 | 110 ms: 1.08x faster                                                         |
| json                    | 4.94 ms                                                | 4.60 ms: 1.07x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 35.0 us: 1.06x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.06x faster                                                         |
| spectral_norm           | 100 ms                                                 | 95.6 ms: 1.05x faster                                                        |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.04x faster                                                        |
| logging_format          | 6.68 us                                                | 6.41 us: 1.04x faster                                                        |
| richards                | 45.7 ms                                                | 43.8 ms: 1.04x faster                                                        |
| logging_silent          | 101 ns                                                 | 97.2 ns: 1.04x faster                                                        |
| chaos                   | 69.2 ms                                                | 66.6 ms: 1.04x faster                                                        |
| coverage                | 100 ms                                                 | 96.5 ms: 1.04x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                                        |
| float                   | 77.2 ms                                                | 74.7 ms: 1.03x faster                                                        |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                                         |
| raytrace                | 297 ms                                                 | 287 ms: 1.03x faster                                                         |
| bench_thread_pool       | 819 us                                                 | 795 us: 1.03x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| logging_simple          | 6.03 us                                                | 5.87 us: 1.03x faster                                                        |
| html5lib                | 64.5 ms                                                | 62.8 ms: 1.03x faster                                                        |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                         |
| regex_compile           | 138 ms                                                 | 135 ms: 1.03x faster                                                         |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                                        |
| regex_dna               | 204 ms                                                 | 199 ms: 1.02x faster                                                         |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                         |
| crypto_pyaes            | 74.7 ms                                                | 73.1 ms: 1.02x faster                                                        |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                                         |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| docutils                | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                        |
| deepcopy                | 342 us                                                 | 337 us: 1.02x faster                                                         |
| pyflate                 | 418 ms                                                 | 412 ms: 1.02x faster                                                         |
| tornado_http            | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                        |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                        |
| pickle_list             | 4.11 us                                                | 4.07 us: 1.01x faster                                                        |
| unpack_sequence         | 43.1 ns                                                | 42.7 ns: 1.01x faster                                                        |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                        |
| scimark_fft             | 328 ms                                                 | 326 ms: 1.01x faster                                                         |
| sympy_str               | 290 ms                                                 | 288 ms: 1.01x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.00x faster                                                        |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                                        |
| nbody                   | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                        |
| sqlalchemy_declarative  | 138 ms                                                 | 140 ms: 1.01x slower                                                         |
| thrift                  | 756 us                                                 | 765 us: 1.01x slower                                                         |
| mako                    | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.99 us: 1.02x slower                                                        |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                        |
| django_template         | 32.6 ms                                                | 33.5 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.62 ms: 1.03x slower                                                        |
| scimark_lu              | 110 ms                                                 | 113 ms: 1.03x slower                                                         |
| xml_etree_process       | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.46 ms: 1.04x slower                                                        |
| gc_traversal            | 4.02 ms                                                | 4.19 ms: 1.04x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 655 ms: 1.04x slower                                                         |
| python_startup          | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 81.9 ms: 1.07x slower                                                        |
| comprehensions          | 22.4 us                                                | 24.2 us: 1.08x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                        |
| async_generators        | 368 ms                                                 | 420 ms: 1.14x slower                                                         |
| dask                    | 360 ms                                                 | 513 ms: 1.42x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (14): unpickle, nqueens, async_tree_io, async_tree_none, dulwich_log, go, bench_mp_pool, xml_etree_iterparse, sympy_sum, djangocms, scimark_monte_carlo, genshi_text, sqlalchemy_imperative, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
