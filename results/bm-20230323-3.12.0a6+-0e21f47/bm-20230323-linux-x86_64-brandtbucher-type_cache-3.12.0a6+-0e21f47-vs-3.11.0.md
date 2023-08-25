
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 0e21f47
- commit date: 2023-03-23
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| chameleon      | 6.47 ms                                                | 6.63 ms: 1.02x slower                                              |
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                             |
| html5lib       | 64.5 ms                                                | 62.4 ms: 1.03x faster                                              |
| tornado_http   | 96.3 ms                                                | 92.3 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.8 ms: 1.07x faster                                              |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                               |
| float          | 77.2 ms                                                | 73.7 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                              |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                               |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                              |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.71 ms: 1.30x faster                                              |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                               |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                               |
| pickle_pure_python   | 306 us                                                 | 292 us: 1.05x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                               |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                              |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                              |
| pickle_list          | 4.11 us                                                | 4.33 us: 1.05x slower                                              |
| unpickle_list        | 4.91 us                                                | 5.28 us: 1.08x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 58.0 ms: 1.08x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 82.1 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.87 ms: 1.04x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 6.55 ms: 1.09x slower                                              |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.9 ms: 1.06x faster                                              |
| mako            | 10.1 ms                                                | 10.0 ms: 1.01x faster                                              |
| genshi_text     | 21.6 ms                                                | 22.0 ms: 1.02x slower                                              |
| django_template | 32.6 ms                                                | 34.0 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.51x faster                                              |
| asyncio_tcp             | 922 ms                                                 | 509 ms: 1.81x faster                                               |
| json_dumps              | 12.6 ms                                                | 9.71 ms: 1.30x faster                                              |
| mypy2                   | 420 ms                                                 | 337 ms: 1.24x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                               |
| coroutines              | 25.5 ms                                                | 22.7 ms: 1.12x faster                                              |
| regex_effbot            | 3.99 ms                                                | 3.57 ms: 1.12x faster                                              |
| deltablue               | 3.67 ms                                                | 3.32 ms: 1.11x faster                                              |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                              |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.07x faster                                              |
| nbody                   | 93.1 ms                                                | 86.8 ms: 1.07x faster                                              |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                               |
| spectral_norm           | 100 ms                                                 | 93.6 ms: 1.07x faster                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.21 ms: 1.07x faster                                              |
| genshi_xml              | 51.8 ms                                                | 48.9 ms: 1.06x faster                                              |
| json                    | 4.94 ms                                                | 4.68 ms: 1.06x faster                                              |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                               |
| logging_silent          | 101 ns                                                 | 96.1 ns: 1.05x faster                                              |
| pickle_pure_python      | 306 us                                                 | 292 us: 1.05x faster                                               |
| float                   | 77.2 ms                                                | 73.7 ms: 1.05x faster                                              |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                              |
| tornado_http            | 96.3 ms                                                | 92.3 ms: 1.04x faster                                              |
| richards                | 45.7 ms                                                | 43.9 ms: 1.04x faster                                              |
| html5lib                | 64.5 ms                                                | 62.4 ms: 1.03x faster                                              |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                               |
| logging_format          | 6.68 us                                                | 6.47 us: 1.03x faster                                              |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                               |
| telco                   | 6.58 ms                                                | 6.40 ms: 1.03x faster                                              |
| chaos                   | 69.2 ms                                                | 67.3 ms: 1.03x faster                                              |
| nqueens                 | 83.4 ms                                                | 81.2 ms: 1.03x faster                                              |
| bench_thread_pool       | 819 us                                                 | 799 us: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                               |
| docutils                | 2.63 sec                                               | 2.57 sec: 1.02x faster                                             |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                               |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 66.7 ms: 1.02x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                             |
| sqlglot_optimize        | 53.1 ms                                                | 52.2 ms: 1.02x faster                                              |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                              |
| sympy_expand            | 475 ms                                                 | 468 ms: 1.01x faster                                               |
| logging_simple          | 6.03 us                                                | 5.95 us: 1.01x faster                                              |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                              |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                              |
| raytrace                | 297 ms                                                 | 293 ms: 1.01x faster                                               |
| sympy_str               | 290 ms                                                 | 287 ms: 1.01x faster                                               |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.01x faster                                              |
| pprint_safe_repr        | 701 ms                                                 | 698 ms: 1.00x faster                                               |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.00x faster                                              |
| sympy_sum               | 167 ms                                                 | 167 ms: 1.00x slower                                               |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.01x slower                                               |
| mdp                     | 2.62 sec                                               | 2.64 sec: 1.01x slower                                             |
| gc_traversal            | 4.02 ms                                                | 4.06 ms: 1.01x slower                                              |
| dulwich_log             | 63.7 ms                                                | 64.6 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 750 ms: 1.01x slower                                               |
| async_tree_none         | 526 ms                                                 | 535 ms: 1.02x slower                                               |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                             |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                               |
| genshi_text             | 21.6 ms                                                | 22.0 ms: 1.02x slower                                              |
| chameleon               | 6.47 ms                                                | 6.63 ms: 1.02x slower                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                              |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                              |
| pyflate                 | 418 ms                                                 | 434 ms: 1.04x slower                                               |
| unpack_sequence         | 43.1 ns                                                | 44.7 ns: 1.04x slower                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.05 us: 1.04x slower                                              |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                              |
| python_startup          | 8.52 ms                                                | 8.87 ms: 1.04x slower                                              |
| django_template         | 32.6 ms                                                | 34.0 ms: 1.04x slower                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.46 ms: 1.04x slower                                              |
| pickle_list             | 4.11 us                                                | 4.33 us: 1.05x slower                                              |
| thrift                  | 756 us                                                 | 804 us: 1.06x slower                                               |
| unpickle_list           | 4.91 us                                                | 5.28 us: 1.08x slower                                              |
| xml_etree_process       | 53.9 ms                                                | 58.0 ms: 1.08x slower                                              |
| async_tree_memoization  | 627 ms                                                 | 676 ms: 1.08x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 82.1 ms: 1.08x slower                                              |
| comprehensions          | 22.4 us                                                | 24.2 us: 1.08x slower                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.55 ms: 1.09x slower                                              |
| async_generators        | 368 ms                                                 | 416 ms: 1.13x slower                                               |
| dask                    | 360 ms                                                 | 515 ms: 1.43x slower                                               |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (5): pathlib, pycparser, fannkuch, bench_mp_pool, unpickle
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
