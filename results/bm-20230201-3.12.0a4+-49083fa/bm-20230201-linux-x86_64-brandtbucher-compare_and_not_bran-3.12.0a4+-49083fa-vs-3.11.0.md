
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 49083fa
- commit date: 2023-02-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                         |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                        |
| tornado_http   | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.7 ms: 1.06x faster                                                        |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                         |
| nbody          | 93.1 ms                                                | 94.4 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                        |
| regex_compile  | 138 ms                                                 | 128 ms: 1.07x faster                                                         |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                        |
| regex_dna      | 204 ms                                                 | 217 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.33 ms: 1.35x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                         |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                         |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                        |
| xml_etree_process    | 53.9 ms                                                | 54.0 ms: 1.00x slower                                                        |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                         |
| pickle_dict          | 31.1 us                                                | 32.2 us: 1.03x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.31 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.88 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.43 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.3 ms: 1.12x faster                                                        |
| genshi_text    | 21.6 ms                                                | 20.6 ms: 1.04x faster                                                        |
| mako           | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 494 ms: 1.86x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.33 ms: 1.35x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.98 ms: 1.13x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                         |
| genshi_xml              | 51.8 ms                                                | 46.3 ms: 1.12x faster                                                        |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 996 us: 1.10x faster                                                         |
| richards                | 45.7 ms                                                | 41.5 ms: 1.10x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                        |
| logging_silent          | 101 ns                                                 | 92.7 ns: 1.09x faster                                                        |
| nqueens                 | 83.4 ms                                                | 76.6 ms: 1.09x faster                                                        |
| scimark_fft             | 328 ms                                                 | 302 ms: 1.09x faster                                                         |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.08x faster                                                         |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| hexiom                  | 6.37 ms                                                | 5.92 ms: 1.08x faster                                                        |
| regex_compile           | 138 ms                                                 | 128 ms: 1.07x faster                                                         |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                         |
| spectral_norm           | 100 ms                                                 | 93.4 ms: 1.07x faster                                                        |
| chaos                   | 69.2 ms                                                | 64.7 ms: 1.07x faster                                                        |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                         |
| deepcopy                | 342 us                                                 | 321 us: 1.07x faster                                                         |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                         |
| json                    | 4.94 ms                                                | 4.64 ms: 1.06x faster                                                        |
| float                   | 77.2 ms                                                | 72.7 ms: 1.06x faster                                                        |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                        |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                       |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                        |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 781 us: 1.05x faster                                                         |
| logging_format          | 6.68 us                                                | 6.38 us: 1.05x faster                                                        |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.05x faster                                                         |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                         |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                                        |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 50.9 ms: 1.04x faster                                                        |
| async_generators        | 368 ms                                                 | 353 ms: 1.04x faster                                                         |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                                         |
| pprint_safe_repr        | 701 ms                                                 | 674 ms: 1.04x faster                                                         |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.04x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.03x faster                                                       |
| mako                    | 10.1 ms                                                | 9.75 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 66.1 ms: 1.03x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                         |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.88 us: 1.02x faster                                                        |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                        |
| tornado_http            | 96.3 ms                                                | 94.9 ms: 1.01x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                                        |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                         |
| xml_etree_process       | 53.9 ms                                                | 54.0 ms: 1.00x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.71 ms: 1.01x slower                                                        |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| nbody                   | 93.1 ms                                                | 94.4 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 753 ms: 1.02x slower                                                         |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 641 ms: 1.02x slower                                                         |
| unpickle_list           | 4.91 us                                                | 5.02 us: 1.02x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                         |
| pickle_dict             | 31.1 us                                                | 32.2 us: 1.03x slower                                                        |
| coroutines              | 25.5 ms                                                | 26.4 ms: 1.03x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.88 ms: 1.04x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.31 us: 1.05x slower                                                        |
| generators              | 73.5 ms                                                | 77.3 ms: 1.05x slower                                                        |
| regex_dna               | 204 ms                                                 | 217 ms: 1.06x slower                                                         |
| gc_traversal            | 4.02 ms                                                | 4.27 ms: 1.06x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.43 ms: 1.07x slower                                                        |
| dask                    | 360 ms                                                 | 507 ms: 1.41x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (9): meteor_contest, unpack_sequence, django_template, async_tree_none, chameleon, bench_mp_pool, thrift, coverage, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230201-3.12.0a4+-49083fa/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
