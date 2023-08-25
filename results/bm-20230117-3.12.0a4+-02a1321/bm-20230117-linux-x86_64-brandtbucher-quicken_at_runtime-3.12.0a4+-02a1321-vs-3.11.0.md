
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 02a1321
- commit date: 2023-01-17
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.32 ms: 1.02x faster                                                      |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                     |
| html5lib       | 64.5 ms                                                | 61.5 ms: 1.05x faster                                                      |
| tornado_http   | 96.3 ms                                                | 94.4 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                       |
| float          | 77.2 ms                                                | 76.0 ms: 1.02x faster                                                      |
| nbody          | 93.1 ms                                                | 94.0 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.65 ms: 1.09x faster                                                      |
| regex_compile  | 138 ms                                                 | 130 ms: 1.07x faster                                                       |
| regex_v8       | 22.0 ms                                                | 21.5 ms: 1.02x faster                                                      |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.34 ms: 1.35x faster                                                      |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 209 us: 1.09x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                       |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                                       |
| xml_etree_process    | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                      |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                      |
| pickle_list          | 4.11 us                                                | 4.08 us: 1.01x faster                                                      |
| unpickle_list        | 4.91 us                                                | 4.93 us: 1.00x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.74 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.27 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.2 ms: 1.12x faster                                                      |
| genshi_text    | 21.6 ms                                                | 20.2 ms: 1.07x faster                                                      |
| mako           | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 494 ms: 1.87x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.34 ms: 1.35x faster                                                      |
| logging_silent          | 101 ns                                                 | 89.6 ns: 1.13x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 46.2 ms: 1.12x faster                                                      |
| gc_traversal            | 4.02 ms                                                | 3.59 ms: 1.12x faster                                                      |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 998 us: 1.10x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 209 us: 1.09x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.65 ms: 1.09x faster                                                      |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.09x faster                                                      |
| json                    | 4.94 ms                                                | 4.56 ms: 1.08x faster                                                      |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                                       |
| sympy_str               | 290 ms                                                 | 271 ms: 1.07x faster                                                       |
| chaos                   | 69.2 ms                                                | 64.7 ms: 1.07x faster                                                      |
| nqueens                 | 83.4 ms                                                | 78.0 ms: 1.07x faster                                                      |
| genshi_text             | 21.6 ms                                                | 20.2 ms: 1.07x faster                                                      |
| regex_compile           | 138 ms                                                 | 130 ms: 1.07x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.00 ms: 1.06x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                     |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                     |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.26 ms: 1.05x faster                                                      |
| async_generators        | 368 ms                                                 | 350 ms: 1.05x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                      |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                       |
| html5lib                | 64.5 ms                                                | 61.5 ms: 1.05x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                       |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                      |
| deltablue               | 3.67 ms                                                | 3.50 ms: 1.05x faster                                                      |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 782 us: 1.05x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 293 us: 1.04x faster                                                       |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.81 us: 1.04x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 51.1 ms: 1.04x faster                                                      |
| telco                   | 6.58 ms                                                | 6.34 ms: 1.04x faster                                                      |
| mako                    | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                      |
| crypto_pyaes            | 74.7 ms                                                | 72.0 ms: 1.04x faster                                                      |
| logging_format          | 6.68 us                                                | 6.45 us: 1.04x faster                                                      |
| coverage                | 100 ms                                                 | 96.7 ms: 1.03x faster                                                      |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                      |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                       |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                       |
| spectral_norm           | 100 ms                                                 | 97.5 ms: 1.03x faster                                                      |
| thrift                  | 756 us                                                 | 738 us: 1.02x faster                                                       |
| regex_v8                | 22.0 ms                                                | 21.5 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.32 ms: 1.02x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 62.4 ms: 1.02x faster                                                      |
| tornado_http            | 96.3 ms                                                | 94.4 ms: 1.02x faster                                                      |
| float                   | 77.2 ms                                                | 76.0 ms: 1.02x faster                                                      |
| xml_etree_process       | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                      |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                      |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                       |
| fannkuch                | 388 ms                                                 | 385 ms: 1.01x faster                                                       |
| pickle_list             | 4.11 us                                                | 4.08 us: 1.01x faster                                                      |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                      |
| unpickle_list           | 4.91 us                                                | 4.93 us: 1.00x slower                                                      |
| pyflate                 | 418 ms                                                 | 420 ms: 1.01x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                      |
| raytrace                | 297 ms                                                 | 299 ms: 1.01x slower                                                       |
| unpack_sequence         | 43.1 ns                                                | 43.5 ns: 1.01x slower                                                      |
| nbody                   | 93.1 ms                                                | 94.0 ms: 1.01x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                     |
| async_tree_memoization  | 627 ms                                                 | 637 ms: 1.02x slower                                                       |
| richards                | 45.7 ms                                                | 46.6 ms: 1.02x slower                                                      |
| regex_dna               | 204 ms                                                 | 209 ms: 1.02x slower                                                       |
| generators              | 73.5 ms                                                | 75.2 ms: 1.02x slower                                                      |
| python_startup          | 8.52 ms                                                | 8.74 ms: 1.02x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 69.8 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 763 ms: 1.03x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.27 ms: 1.04x slower                                                      |
| dask                    | 360 ms                                                 | 512 ms: 1.42x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (11): async_tree_none, meteor_contest, pickle, mdp, bench_mp_pool, django_template, coroutines, deepcopy_reduce, sqlglot_transpile, scimark_sor, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230117-3.12.0a4+-02a1321/bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
