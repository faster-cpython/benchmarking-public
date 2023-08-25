
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: b201b6d
- commit date: 2023-03-24
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                        |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| html5lib       | 64.5 ms                                                | 62.6 ms: 1.03x faster                                                        |
| tornado_http   | 96.3 ms                                                | 91.6 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| nbody          | 93.1 ms                                                | 88.6 ms: 1.05x faster                                                        |
| float          | 77.2 ms                                                | 74.4 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.41 ms: 1.17x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.04x faster                                                        |
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                                         |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.73 ms: 1.29x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                         |
| json_loads           | 26.5 us                                                | 24.5 us: 1.08x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.9 ms: 1.04x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 294 us: 1.04x faster                                                         |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.20 us: 1.02x slower                                                        |
| pickle               | 10.1 us                                                | 10.5 us: 1.05x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 81.1 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.65 ms: 1.01x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.34 ms: 1.05x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.5 ms: 1.07x faster                                                        |
| mako            | 10.1 ms                                                | 10.1 ms: 1.00x slower                                                        |
| django_template | 32.6 ms                                                | 33.9 ms: 1.04x slower                                                        |
| genshi_text     | 21.6 ms                                                | 22.5 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.1 ms: 2.52x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 509 ms: 1.81x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.73 ms: 1.29x faster                                                        |
| mypy2                   | 420 ms                                                 | 335 ms: 1.26x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.41 ms: 1.17x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                         |
| deltablue               | 3.67 ms                                                | 3.26 ms: 1.13x faster                                                        |
| spectral_norm           | 100 ms                                                 | 91.1 ms: 1.10x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                        |
| json_loads              | 26.5 us                                                | 24.5 us: 1.08x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.17 ms: 1.08x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                        |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| genshi_xml              | 51.8 ms                                                | 48.5 ms: 1.07x faster                                                        |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.07x faster                                                         |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                                        |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.06x faster                                                         |
| coroutines              | 25.5 ms                                                | 24.1 ms: 1.06x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                       |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| hexiom                  | 6.37 ms                                                | 6.06 ms: 1.05x faster                                                        |
| nbody                   | 93.1 ms                                                | 88.6 ms: 1.05x faster                                                        |
| tornado_http            | 96.3 ms                                                | 91.6 ms: 1.05x faster                                                        |
| logging_silent          | 101 ns                                                 | 96.5 ns: 1.05x faster                                                        |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                                         |
| xml_etree_iterparse     | 104 ms                                                 | 99.9 ms: 1.04x faster                                                        |
| coverage                | 100 ms                                                 | 96.3 ms: 1.04x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 294 us: 1.04x faster                                                         |
| float                   | 77.2 ms                                                | 74.4 ms: 1.04x faster                                                        |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.04x faster                                                        |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| richards                | 45.7 ms                                                | 44.2 ms: 1.04x faster                                                        |
| nqueens                 | 83.4 ms                                                | 80.6 ms: 1.03x faster                                                        |
| chaos                   | 69.2 ms                                                | 66.9 ms: 1.03x faster                                                        |
| html5lib                | 64.5 ms                                                | 62.6 ms: 1.03x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 794 us: 1.03x faster                                                         |
| sqlglot_optimize        | 53.1 ms                                                | 51.6 ms: 1.03x faster                                                        |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                         |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                         |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.93 ms: 1.02x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                                       |
| regex_compile           | 138 ms                                                 | 136 ms: 1.02x faster                                                         |
| sympy_expand            | 475 ms                                                 | 467 ms: 1.02x faster                                                         |
| telco                   | 6.58 ms                                                | 6.48 ms: 1.02x faster                                                        |
| logging_format          | 6.68 us                                                | 6.58 us: 1.02x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                        |
| regex_dna               | 204 ms                                                 | 202 ms: 1.01x faster                                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 67.4 ms: 1.01x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.8 ms: 1.01x faster                                                        |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                         |
| fannkuch                | 388 ms                                                 | 384 ms: 1.01x faster                                                         |
| sympy_str               | 290 ms                                                 | 288 ms: 1.01x faster                                                         |
| mako                    | 10.1 ms                                                | 10.1 ms: 1.00x slower                                                        |
| chameleon               | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                        |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                                         |
| sympy_sum               | 167 ms                                                 | 168 ms: 1.01x slower                                                         |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.1 ms: 1.01x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.65 ms: 1.01x slower                                                        |
| pickle_dict             | 31.1 us                                                | 31.7 us: 1.02x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.20 us: 1.02x slower                                                        |
| pyflate                 | 418 ms                                                 | 427 ms: 1.02x slower                                                         |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                        |
| unpack_sequence         | 43.1 ns                                                | 44.4 ns: 1.03x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 3.04 us: 1.03x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 651 ms: 1.04x slower                                                         |
| django_template         | 32.6 ms                                                | 33.9 ms: 1.04x slower                                                        |
| genshi_text             | 21.6 ms                                                | 22.5 ms: 1.04x slower                                                        |
| pickle                  | 10.1 us                                                | 10.5 us: 1.05x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                        |
| thrift                  | 756 us                                                 | 795 us: 1.05x slower                                                         |
| comprehensions          | 22.4 us                                                | 23.7 us: 1.05x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.34 ms: 1.05x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 81.1 ms: 1.06x slower                                                        |
| async_generators        | 368 ms                                                 | 409 ms: 1.11x slower                                                         |
| dask                    | 360 ms                                                 | 515 ms: 1.43x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (14): scimark_lu, create_gc_cycles, pprint_safe_repr, sqlglot_normalize, pathlib, dulwich_log, bench_mp_pool, djangocms, async_tree_none, unpickle_list, async_tree_cpu_io_mixed, logging_simple, async_tree_io, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
