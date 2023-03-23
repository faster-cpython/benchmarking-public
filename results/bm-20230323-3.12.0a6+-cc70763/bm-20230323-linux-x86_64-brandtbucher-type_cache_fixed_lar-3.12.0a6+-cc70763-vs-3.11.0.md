
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache_fixed_lar
- machine: linux-x86_64
- commit hash: cc70763
- commit date: 2023-03-23
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                         |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| tornado_http   | 96.5 ms                                                | 91.2 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                        |
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                                         |
| nbody          | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.04x faster                                                        |
| regex_compile  | 136 ms                                                 | 133 ms: 1.03x faster                                                         |
| regex_effbot   | 3.46 ms                                                | 3.42 ms: 1.01x faster                                                        |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                         |
| json_loads           | 26.1 us                                                | 23.8 us: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 99.9 ms: 1.04x faster                                                        |
| pickle_dict          | 31.2 us                                                | 31.7 us: 1.02x slower                                                        |
| unpickle_list        | 4.99 us                                                | 5.09 us: 1.02x slower                                                        |
| xml_etree_process    | 53.7 ms                                                | 56.2 ms: 1.05x slower                                                        |
| pickle_list          | 4.14 us                                                | 4.36 us: 1.05x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                        |
| pickle               | 9.90 us                                                | 10.6 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.85 ms: 1.03x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.55 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.2 ms: 1.09x faster                                                        |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.01x faster                                                        |
| mako            | 9.83 ms                                                | 10.00 ms: 1.02x slower                                                       |
| django_template | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                        |
| asyncio_tcp             | 883 ms                                                 | 509 ms: 1.73x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                        |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                         |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.05 ms: 1.13x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.30 ms: 1.11x faster                                                        |
| coroutines              | 26.2 ms                                                | 23.7 ms: 1.10x faster                                                        |
| json_loads              | 26.1 us                                                | 23.8 us: 1.10x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 47.2 ms: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                         |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                       |
| coverage                | 99.3 ms                                                | 93.0 ms: 1.07x faster                                                        |
| scimark_fft             | 325 ms                                                 | 305 ms: 1.07x faster                                                         |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.06x faster                                                         |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                        |
| tornado_http            | 96.5 ms                                                | 91.2 ms: 1.06x faster                                                        |
| json                    | 4.87 ms                                                | 4.61 ms: 1.06x faster                                                        |
| html5lib                | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                         |
| deepcopy                | 341 us                                                 | 325 us: 1.05x faster                                                         |
| nqueens                 | 83.8 ms                                                | 79.9 ms: 1.05x faster                                                        |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                                         |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.04x faster                                                        |
| richards                | 46.1 ms                                                | 44.2 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 99.9 ms: 1.04x faster                                                        |
| hexiom                  | 6.34 ms                                                | 6.09 ms: 1.04x faster                                                        |
| gc_traversal            | 3.82 ms                                                | 3.67 ms: 1.04x faster                                                        |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                                         |
| chaos                   | 68.7 ms                                                | 66.2 ms: 1.04x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.6 us: 1.04x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 789 us: 1.03x faster                                                         |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                         |
| spectral_norm           | 98.1 ms                                                | 95.0 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 65.8 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                        |
| regex_compile           | 136 ms                                                 | 133 ms: 1.03x faster                                                         |
| nbody                   | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                                        |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                                         |
| pprint_safe_repr        | 706 ms                                                 | 691 ms: 1.02x faster                                                         |
| sqlglot_optimize        | 52.7 ms                                                | 51.6 ms: 1.02x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.91 us: 1.02x faster                                                        |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.01x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 63.0 ms: 1.01x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                         |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                        |
| regex_effbot            | 3.46 ms                                                | 3.42 ms: 1.01x faster                                                        |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                         |
| crypto_pyaes            | 75.7 ms                                                | 75.0 ms: 1.01x faster                                                        |
| logging_silent          | 98.0 ns                                                | 97.2 ns: 1.01x faster                                                        |
| pyflate                 | 419 ms                                                 | 415 ms: 1.01x faster                                                         |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                         |
| go                      | 140 ms                                                 | 140 ms: 1.00x faster                                                         |
| telco                   | 6.43 ms                                                | 6.49 ms: 1.01x slower                                                        |
| scimark_lu              | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                                         |
| mako                    | 9.83 ms                                                | 10.00 ms: 1.02x slower                                                       |
| pickle_dict             | 31.2 us                                                | 31.7 us: 1.02x slower                                                        |
| thrift                  | 760 us                                                 | 775 us: 1.02x slower                                                         |
| unpickle_list           | 4.99 us                                                | 5.09 us: 1.02x slower                                                        |
| django_template         | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                        |
| mdp                     | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                       |
| unpack_sequence         | 44.5 ns                                                | 45.9 ns: 1.03x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.85 ms: 1.03x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 56.2 ms: 1.05x slower                                                        |
| async_tree_memoization  | 624 ms                                                 | 655 ms: 1.05x slower                                                         |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.05x slower                                                        |
| pickle_list             | 4.14 us                                                | 4.36 us: 1.05x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.06x slower                                                        |
| pickle                  | 9.90 us                                                | 10.6 us: 1.07x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.55 ms: 1.08x slower                                                        |
| async_generators        | 356 ms                                                 | 413 ms: 1.16x slower                                                         |
| dask                    | 365 ms                                                 | 505 ms: 1.38x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (8): djangocms, async_tree_io, sympy_sum, chameleon, bench_mp_pool, async_tree_cpu_io_mixed, unpickle, logging_format
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-cc70763/bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763.json: comprehensions
