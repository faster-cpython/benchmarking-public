
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 30483bd
- commit date: 2023-03-24
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                               |
| chameleon      | 6.47 ms                                                | 6.54 ms: 1.01x slower                                              |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                             |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                              |
| tornado_http   | 96.3 ms                                                | 92.2 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.6 ms: 1.06x faster                                              |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                               |
| float          | 77.2 ms                                                | 73.6 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                              |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                               |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                               |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.86 ms: 1.28x faster                                              |
| unpickle_pure_python | 228 us                                                 | 204 us: 1.12x faster                                               |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                              |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.05x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                               |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                              |
| pickle_dict          | 31.1 us                                                | 32.3 us: 1.04x slower                                              |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 56.4 ms: 1.05x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 81.4 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (3): unpickle, pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.85 ms: 1.04x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                              |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.2 ms: 1.07x faster                                              |
| mako            | 10.1 ms                                                | 9.95 ms: 1.01x faster                                              |
| genshi_text     | 21.6 ms                                                | 21.8 ms: 1.01x slower                                              |
| django_template | 32.6 ms                                                | 33.5 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                              |
| asyncio_tcp             | 922 ms                                                 | 510 ms: 1.81x faster                                               |
| json_dumps              | 12.6 ms                                                | 9.86 ms: 1.28x faster                                              |
| mypy2                   | 420 ms                                                 | 336 ms: 1.25x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.53 ms: 1.13x faster                                              |
| unpickle_pure_python    | 228 us                                                 | 204 us: 1.12x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.03 ms: 1.12x faster                                              |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                              |
| deltablue               | 3.67 ms                                                | 3.31 ms: 1.11x faster                                              |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                              |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.10x faster                                               |
| scimark_fft             | 328 ms                                                 | 300 ms: 1.10x faster                                               |
| spectral_norm           | 100 ms                                                 | 91.5 ms: 1.09x faster                                              |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                              |
| genshi_xml              | 51.8 ms                                                | 48.2 ms: 1.07x faster                                              |
| richards                | 45.7 ms                                                | 43.0 ms: 1.06x faster                                              |
| nbody                   | 93.1 ms                                                | 87.6 ms: 1.06x faster                                              |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                              |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.05x faster                                               |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                              |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                              |
| float                   | 77.2 ms                                                | 73.6 ms: 1.05x faster                                              |
| logging_silent          | 101 ns                                                 | 96.6 ns: 1.05x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                               |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.05x faster                                              |
| tornado_http            | 96.3 ms                                                | 92.2 ms: 1.04x faster                                              |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                               |
| chaos                   | 69.2 ms                                                | 67.0 ms: 1.03x faster                                              |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                               |
| nqueens                 | 83.4 ms                                                | 80.9 ms: 1.03x faster                                              |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                             |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                              |
| sqlglot_optimize        | 53.1 ms                                                | 51.7 ms: 1.03x faster                                              |
| bench_thread_pool       | 819 us                                                 | 798 us: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                               |
| raytrace                | 297 ms                                                 | 290 ms: 1.02x faster                                               |
| logging_format          | 6.68 us                                                | 6.54 us: 1.02x faster                                              |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                             |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                               |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                               |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                              |
| fannkuch                | 388 ms                                                 | 381 ms: 1.02x faster                                               |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                               |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                              |
| logging_simple          | 6.03 us                                                | 5.94 us: 1.01x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                               |
| mako                    | 10.1 ms                                                | 9.95 ms: 1.01x faster                                              |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                              |
| pprint_safe_repr        | 701 ms                                                 | 692 ms: 1.01x faster                                               |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 67.4 ms: 1.01x faster                                              |
| crypto_pyaes            | 74.7 ms                                                | 74.1 ms: 1.01x faster                                              |
| dulwich_log             | 63.7 ms                                                | 64.1 ms: 1.01x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                             |
| async_tree_none         | 526 ms                                                 | 531 ms: 1.01x slower                                               |
| chameleon               | 6.47 ms                                                | 6.54 ms: 1.01x slower                                              |
| genshi_text             | 21.6 ms                                                | 21.8 ms: 1.01x slower                                              |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                               |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                              |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                              |
| django_template         | 32.6 ms                                                | 33.5 ms: 1.03x slower                                              |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                              |
| pickle_dict             | 31.1 us                                                | 32.3 us: 1.04x slower                                              |
| mdp                     | 2.62 sec                                               | 2.71 sec: 1.04x slower                                             |
| python_startup          | 8.52 ms                                                | 8.85 ms: 1.04x slower                                              |
| unpickle_list           | 4.91 us                                                | 5.12 us: 1.04x slower                                              |
| xml_etree_process       | 53.9 ms                                                | 56.4 ms: 1.05x slower                                              |
| unpack_sequence         | 43.1 ns                                                | 45.2 ns: 1.05x slower                                              |
| thrift                  | 756 us                                                 | 805 us: 1.06x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 81.4 ms: 1.07x slower                                              |
| async_tree_memoization  | 627 ms                                                 | 670 ms: 1.07x slower                                               |
| comprehensions          | 22.4 us                                                | 24.3 us: 1.08x slower                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                              |
| async_generators        | 368 ms                                                 | 416 ms: 1.13x slower                                               |
| dask                    | 360 ms                                                 | 516 ms: 1.43x slower                                               |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (8): unpickle, pickle_list, deepcopy_reduce, bench_mp_pool, pyflate, sympy_sum, xml_etree_iterparse, async_tree_cpu_io_mixed
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
