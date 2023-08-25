
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 933012e
- commit date: 2023-01-18
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.37 ms: 1.02x faster                                                       |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                      |
| html5lib       | 64.5 ms                                                | 59.8 ms: 1.08x faster                                                       |
| tornado_http   | 96.3 ms                                                | 94.3 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.3 ms: 1.07x faster                                                       |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| nbody          | 93.1 ms                                                | 94.1 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                       |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                       |
| regex_dna      | 204 ms                                                 | 207 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.17x faster                                                        |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 280 us: 1.09x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| xml_etree_process    | 53.9 ms                                                | 54.1 ms: 1.00x slower                                                       |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.21 us: 1.02x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 78.5 ms: 1.03x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.09 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.39 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.0 ms: 1.12x faster                                                       |
| genshi_text     | 21.6 ms                                                | 20.0 ms: 1.08x faster                                                       |
| mako            | 10.1 ms                                                | 9.50 ms: 1.06x faster                                                       |
| django_template | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 497 ms: 1.86x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.17x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.51 ms: 1.14x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.96 ms: 1.14x faster                                                       |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 46.0 ms: 1.12x faster                                                       |
| logging_silent          | 101 ns                                                 | 90.4 ns: 1.12x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.06 ms: 1.11x faster                                                       |
| aiohttp                 | 1.10 ms                                                | 991 us: 1.11x faster                                                        |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                       |
| chaos                   | 69.2 ms                                                | 63.3 ms: 1.09x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 280 us: 1.09x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                                      |
| scimark_fft             | 328 ms                                                 | 301 ms: 1.09x faster                                                        |
| richards                | 45.7 ms                                                | 42.2 ms: 1.08x faster                                                       |
| logging_format          | 6.68 us                                                | 6.18 us: 1.08x faster                                                       |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| nqueens                 | 83.4 ms                                                | 77.2 ms: 1.08x faster                                                       |
| html5lib                | 64.5 ms                                                | 59.8 ms: 1.08x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                       |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.08x faster                                                        |
| genshi_text             | 21.6 ms                                                | 20.0 ms: 1.08x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.62 us: 1.07x faster                                                       |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.44 sec: 1.07x faster                                                      |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                                       |
| float                   | 77.2 ms                                                | 72.3 ms: 1.07x faster                                                       |
| json                    | 4.94 ms                                                | 4.64 ms: 1.07x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.07x faster                                                       |
| mako                    | 10.1 ms                                                | 9.50 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                      |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                      |
| async_generators        | 368 ms                                                 | 349 ms: 1.05x faster                                                        |
| deepcopy                | 342 us                                                 | 325 us: 1.05x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 779 us: 1.05x faster                                                        |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                        |
| pyflate                 | 418 ms                                                 | 399 ms: 1.05x faster                                                        |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| coverage                | 100 ms                                                 | 96.1 ms: 1.04x faster                                                       |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                                        |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                       |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.1 ms                                                | 65.9 ms: 1.03x faster                                                       |
| spectral_norm           | 100 ms                                                 | 97.4 ms: 1.03x faster                                                       |
| telco                   | 6.58 ms                                                | 6.42 ms: 1.03x faster                                                       |
| thrift                  | 756 us                                                 | 739 us: 1.02x faster                                                        |
| tornado_http            | 96.3 ms                                                | 94.3 ms: 1.02x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.37 ms: 1.02x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                                       |
| django_template         | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 74.1 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                                       |
| xml_etree_process       | 53.9 ms                                                | 54.1 ms: 1.00x slower                                                       |
| nbody                   | 93.1 ms                                                | 94.1 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| regex_dna               | 204 ms                                                 | 207 ms: 1.01x slower                                                        |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 751 ms: 1.02x slower                                                        |
| coroutines              | 25.5 ms                                                | 26.0 ms: 1.02x slower                                                       |
| async_tree_memoization  | 627 ms                                                 | 639 ms: 1.02x slower                                                        |
| unpack_sequence         | 43.1 ns                                                | 44.0 ns: 1.02x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| pickle_list             | 4.11 us                                                | 4.21 us: 1.02x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 78.5 ms: 1.03x slower                                                       |
| generators              | 73.5 ms                                                | 76.0 ms: 1.04x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.09 us: 1.04x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.39 ms: 1.06x slower                                                       |
| dask                    | 360 ms                                                 | 496 ms: 1.38x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (6): djangocms, sqlglot_transpile, bench_mp_pool, async_tree_none, sqlglot_parse, unpickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-933012e/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
