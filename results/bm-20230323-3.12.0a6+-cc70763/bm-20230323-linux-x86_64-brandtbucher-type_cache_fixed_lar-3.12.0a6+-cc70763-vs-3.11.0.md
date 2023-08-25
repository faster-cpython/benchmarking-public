
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache_fixed_lar
- machine: linux-x86_64
- commit hash: cc70763
- commit date: 2023-03-23
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.38 ms: 1.01x faster                                                        |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| tornado_http   | 96.3 ms                                                | 91.2 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.5 ms: 1.06x faster                                                        |
| nbody          | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                        |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                        |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                         |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.03x faster                                                        |
| regex_dna      | 204 ms                                                 | 206 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                         |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.9 ms: 1.04x faster                                                        |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                        |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                                        |
| unpickle_list        | 4.91 us                                                | 5.09 us: 1.04x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                        |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.36 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.55 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.2 ms: 1.10x faster                                                        |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                        |
| mako            | 10.1 ms                                                | 10.00 ms: 1.01x faster                                                       |
| django_template | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 509 ms: 1.81x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                        |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                         |
| regex_effbot            | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                         |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.30 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.05 ms: 1.11x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 47.2 ms: 1.10x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.67 ms: 1.10x faster                                                        |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                                         |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                        |
| coroutines              | 25.5 ms                                                | 23.7 ms: 1.08x faster                                                        |
| coverage                | 100 ms                                                 | 93.0 ms: 1.08x faster                                                        |
| scimark_fft             | 328 ms                                                 | 305 ms: 1.07x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                                         |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                         |
| float                   | 77.2 ms                                                | 72.5 ms: 1.06x faster                                                        |
| nbody                   | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                        |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                         |
| tornado_http            | 96.3 ms                                                | 91.2 ms: 1.06x faster                                                        |
| deepcopy                | 342 us                                                 | 325 us: 1.05x faster                                                         |
| spectral_norm           | 100 ms                                                 | 95.0 ms: 1.05x faster                                                        |
| html5lib                | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| hexiom                  | 6.37 ms                                                | 6.09 ms: 1.05x faster                                                        |
| chaos                   | 69.2 ms                                                | 66.2 ms: 1.04x faster                                                        |
| nqueens                 | 83.4 ms                                                | 79.9 ms: 1.04x faster                                                        |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 99.9 ms: 1.04x faster                                                        |
| logging_silent          | 101 ns                                                 | 97.2 ns: 1.04x faster                                                        |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                         |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                         |
| bench_thread_pool       | 819 us                                                 | 789 us: 1.04x faster                                                         |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                                         |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.03x faster                                                        |
| richards                | 45.7 ms                                                | 44.2 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 65.8 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 51.6 ms: 1.03x faster                                                        |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                         |
| logging_format          | 6.68 us                                                | 6.50 us: 1.03x faster                                                        |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                         |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.91 us: 1.02x faster                                                        |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| chameleon               | 6.47 ms                                                | 6.38 ms: 1.01x faster                                                        |
| telco                   | 6.58 ms                                                | 6.49 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 691 ms: 1.01x faster                                                         |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                         |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                        |
| mako                    | 10.1 ms                                                | 10.00 ms: 1.01x faster                                                       |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                         |
| pyflate                 | 418 ms                                                 | 415 ms: 1.01x faster                                                         |
| crypto_pyaes            | 74.7 ms                                                | 75.0 ms: 1.00x slower                                                        |
| regex_dna               | 204 ms                                                 | 206 ms: 1.01x slower                                                         |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                        |
| pickle_dict             | 31.1 us                                                | 31.7 us: 1.02x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                        |
| thrift                  | 756 us                                                 | 775 us: 1.02x slower                                                         |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.03x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                                        |
| unpickle_list           | 4.91 us                                                | 5.09 us: 1.04x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 655 ms: 1.04x slower                                                         |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                                        |
| pickle                  | 10.1 us                                                | 10.6 us: 1.05x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                        |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.36 us: 1.06x slower                                                        |
| unpack_sequence         | 43.1 ns                                                | 45.9 ns: 1.06x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.55 ms: 1.09x slower                                                        |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                                         |
| dask                    | 360 ms                                                 | 505 ms: 1.40x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (7): scimark_lu, djangocms, go, async_tree_cpu_io_mixed, async_tree_io, bench_mp_pool, deepcopy_reduce
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
