
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 697dc1e
- commit date: 2023-01-15
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.35 ms: 1.02x faster                                                       |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                      |
| html5lib       | 64.5 ms                                                | 60.4 ms: 1.07x faster                                                       |
| tornado_http   | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.5 ms: 1.08x faster                                                       |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| nbody          | 93.1 ms                                                | 94.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                       |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                       |
| regex_dna      | 204 ms                                                 | 211 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.34 ms: 1.35x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.16x faster                                                        |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 279 us: 1.10x faster                                                        |
| pickle_dict          | 31.1 us                                                | 29.9 us: 1.04x faster                                                       |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                                       |
| pickle_list          | 4.11 us                                                | 4.06 us: 1.01x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 157 ms: 1.01x faster                                                        |
| xml_etree_process    | 53.9 ms                                                | 54.1 ms: 1.00x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 78.8 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 109 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.68 ms: 1.02x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.22 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.1 ms: 1.12x faster                                                       |
| genshi_text     | 21.6 ms                                                | 20.1 ms: 1.07x faster                                                       |
| mako            | 10.1 ms                                                | 9.63 ms: 1.05x faster                                                       |
| django_template | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 485 ms: 1.90x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.34 ms: 1.35x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.16x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 46.1 ms: 1.12x faster                                                       |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                        |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                       |
| aiohttp                 | 1.10 ms                                                | 999 us: 1.10x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 279 us: 1.10x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                       |
| richards                | 45.7 ms                                                | 42.0 ms: 1.09x faster                                                       |
| float                   | 77.2 ms                                                | 71.5 ms: 1.08x faster                                                       |
| logging_silent          | 101 ns                                                 | 93.8 ns: 1.08x faster                                                       |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                       |
| json                    | 4.94 ms                                                | 4.59 ms: 1.08x faster                                                       |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                        |
| genshi_text             | 21.6 ms                                                | 20.1 ms: 1.07x faster                                                       |
| html5lib                | 64.5 ms                                                | 60.4 ms: 1.07x faster                                                       |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.65 us: 1.07x faster                                                       |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                                        |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.07x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                      |
| nqueens                 | 83.4 ms                                                | 78.5 ms: 1.06x faster                                                       |
| async_generators        | 368 ms                                                 | 348 ms: 1.06x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 774 us: 1.06x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                                      |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                      |
| hexiom                  | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 50.2 ms: 1.06x faster                                                       |
| chaos                   | 69.2 ms                                                | 65.5 ms: 1.06x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.81 ms: 1.06x faster                                                       |
| deepcopy                | 342 us                                                 | 324 us: 1.06x faster                                                        |
| telco                   | 6.58 ms                                                | 6.26 ms: 1.05x faster                                                       |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                      |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                        |
| mako                    | 10.1 ms                                                | 9.63 ms: 1.05x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| spectral_norm           | 100 ms                                                 | 96.0 ms: 1.04x faster                                                       |
| coverage                | 100 ms                                                 | 96.0 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                       |
| pickle_dict             | 31.1 us                                                | 29.9 us: 1.04x faster                                                       |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                       |
| pyflate                 | 418 ms                                                 | 404 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.03x faster                                                       |
| tornado_http            | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                       |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.1 ms: 1.03x faster                                                       |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 66.4 ms: 1.03x faster                                                       |
| coroutines              | 25.5 ms                                                | 24.9 ms: 1.02x faster                                                       |
| thrift                  | 756 us                                                 | 742 us: 1.02x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.35 ms: 1.02x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 73.3 ms: 1.02x faster                                                       |
| django_template         | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                       |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 2.94 us                                                | 2.89 us: 1.02x faster                                                       |
| pickle_list             | 4.11 us                                                | 4.06 us: 1.01x faster                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.01x faster                                                       |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 157 ms: 1.01x faster                                                        |
| xml_etree_process       | 53.9 ms                                                | 54.1 ms: 1.00x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 751 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| nbody                   | 93.1 ms                                                | 94.8 ms: 1.02x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.68 ms: 1.02x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                       |
| generators              | 73.5 ms                                                | 75.9 ms: 1.03x slower                                                       |
| regex_dna               | 204 ms                                                 | 211 ms: 1.03x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 78.8 ms: 1.03x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.22 ms: 1.04x slower                                                       |
| unpack_sequence         | 43.1 ns                                                | 44.9 ns: 1.04x slower                                                       |
| async_tree_memoization  | 627 ms                                                 | 655 ms: 1.04x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 109 ms: 1.05x slower                                                        |
| dask                    | 360 ms                                                 | 492 ms: 1.37x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, async_tree_none, sqlglot_parse, bench_mp_pool, djangocms, pickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230115-3.12.0a4+-697dc1e/bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
