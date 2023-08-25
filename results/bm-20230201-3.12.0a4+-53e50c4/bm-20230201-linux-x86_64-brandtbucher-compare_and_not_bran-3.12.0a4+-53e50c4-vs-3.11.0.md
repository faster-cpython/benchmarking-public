
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 53e50c4
- commit date: 2023-02-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.44 ms: 1.00x faster                                                        |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| tornado_http   | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                        |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                        |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                                         |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                        |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                         |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                                         |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                        |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                                        |
| xml_etree_process    | 53.9 ms                                                | 54.1 ms: 1.00x slower                                                        |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.7 ms: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.89 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.44 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                        |
| genshi_text     | 21.6 ms                                                | 20.4 ms: 1.05x faster                                                        |
| mako            | 10.1 ms                                                | 9.69 ms: 1.04x faster                                                        |
| django_template | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 500 ms: 1.84x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                         |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.00 ms: 1.13x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 995 us: 1.11x faster                                                         |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                        |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                        |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                                         |
| richards                | 45.7 ms                                                | 42.1 ms: 1.09x faster                                                        |
| scimark_fft             | 328 ms                                                 | 302 ms: 1.09x faster                                                         |
| hexiom                  | 6.37 ms                                                | 5.89 ms: 1.08x faster                                                        |
| logging_silent          | 101 ns                                                 | 93.7 ns: 1.08x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                         |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                                         |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                                        |
| fannkuch                | 388 ms                                                 | 364 ms: 1.07x faster                                                         |
| chaos                   | 69.2 ms                                                | 65.0 ms: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                        |
| float                   | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                                         |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                                         |
| spectral_norm           | 100 ms                                                 | 94.5 ms: 1.06x faster                                                        |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                       |
| nqueens                 | 83.4 ms                                                | 79.0 ms: 1.06x faster                                                        |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.05x faster                                                        |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                        |
| html5lib                | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                                        |
| logging_format          | 6.68 us                                                | 6.38 us: 1.05x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 65.0 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                         |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.05x faster                                                         |
| pyflate                 | 418 ms                                                 | 400 ms: 1.04x faster                                                         |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                                        |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                         |
| async_generators        | 368 ms                                                 | 353 ms: 1.04x faster                                                         |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                        |
| mako                    | 10.1 ms                                                | 9.69 ms: 1.04x faster                                                        |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                                         |
| coverage                | 100 ms                                                 | 96.1 ms: 1.04x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 787 us: 1.04x faster                                                         |
| pprint_safe_repr        | 701 ms                                                 | 675 ms: 1.04x faster                                                         |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                       |
| telco                   | 6.58 ms                                                | 6.40 ms: 1.03x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 72.9 ms: 1.02x faster                                                        |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                         |
| tornado_http            | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                        |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                         |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                        |
| thrift                  | 756 us                                                 | 744 us: 1.02x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.58 sec: 1.01x faster                                                       |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                        |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                                        |
| django_template         | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.44 ms: 1.00x faster                                                        |
| xml_etree_process       | 53.9 ms                                                | 54.1 ms: 1.00x slower                                                        |
| gc_traversal            | 4.02 ms                                                | 4.05 ms: 1.01x slower                                                        |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                        |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                         |
| unpack_sequence         | 43.1 ns                                                | 43.6 ns: 1.01x slower                                                        |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.7 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.57 us: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 759 ms: 1.03x slower                                                         |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                         |
| generators              | 73.5 ms                                                | 76.5 ms: 1.04x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.89 ms: 1.04x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 666 ms: 1.06x slower                                                         |
| python_startup_no_site  | 6.01 ms                                                | 6.44 ms: 1.07x slower                                                        |
| dask                    | 360 ms                                                 | 497 ms: 1.38x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (8): deepcopy_reduce, pickle_list, bench_mp_pool, coroutines, sqlglot_transpile, djangocms, nbody, async_tree_none
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230201-3.12.0a4+-53e50c4/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
