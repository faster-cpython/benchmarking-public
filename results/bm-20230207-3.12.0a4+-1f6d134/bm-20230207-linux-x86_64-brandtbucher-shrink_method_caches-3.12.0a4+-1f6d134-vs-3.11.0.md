
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 1f6d134
- commit date: 2023-02-07
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.58 ms: 1.02x slower                                                        |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| float          | 77.2 ms                                                | 74.0 ms: 1.04x faster                                                        |
| nbody          | 93.1 ms                                                | 95.8 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                         |
| regex_effbot   | 3.99 ms                                                | 3.76 ms: 1.06x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                        |
| regex_dna      | 204 ms                                                 | 207 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.47 ms: 1.33x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                         |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 292 us: 1.05x faster                                                         |
| pickle_dict          | 31.1 us                                                | 30.0 us: 1.04x faster                                                        |
| pickle_list          | 4.11 us                                                | 4.05 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| pickle               | 10.1 us                                                | 9.96 us: 1.01x faster                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                        |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.94 ms: 1.05x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.45 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.3 ms: 1.09x faster                                                        |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.03x faster                                                        |
| mako            | 10.1 ms                                                | 9.98 ms: 1.01x faster                                                        |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 496 ms: 1.86x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.47 ms: 1.33x faster                                                        |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                         |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                         |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                                        |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                         |
| deltablue               | 3.67 ms                                                | 3.35 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.11 ms: 1.09x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 47.3 ms: 1.09x faster                                                        |
| nqueens                 | 83.4 ms                                                | 76.5 ms: 1.09x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.02 ms: 1.08x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                         |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                         |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.76 ms: 1.06x faster                                                        |
| fannkuch                | 388 ms                                                 | 365 ms: 1.06x faster                                                         |
| sympy_str               | 290 ms                                                 | 274 ms: 1.06x faster                                                         |
| hexiom                  | 6.37 ms                                                | 6.02 ms: 1.06x faster                                                        |
| sympy_sum               | 167 ms                                                 | 157 ms: 1.06x faster                                                         |
| spectral_norm           | 100 ms                                                 | 94.6 ms: 1.06x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.05x faster                                                       |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                         |
| html5lib                | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                        |
| chaos                   | 69.2 ms                                                | 65.9 ms: 1.05x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 292 us: 1.05x faster                                                         |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                                        |
| float                   | 77.2 ms                                                | 74.0 ms: 1.04x faster                                                        |
| async_generators        | 368 ms                                                 | 354 ms: 1.04x faster                                                         |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                       |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                         |
| deepcopy_memo           | 37.0 us                                                | 35.7 us: 1.04x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.88 ms: 1.04x faster                                                        |
| pickle_dict             | 31.1 us                                                | 30.0 us: 1.04x faster                                                        |
| logging_format          | 6.68 us                                                | 6.46 us: 1.04x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 65.8 ms: 1.03x faster                                                        |
| json                    | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                        |
| raytrace                | 297 ms                                                 | 288 ms: 1.03x faster                                                         |
| bench_thread_pool       | 819 us                                                 | 795 us: 1.03x faster                                                         |
| telco                   | 6.58 ms                                                | 6.40 ms: 1.03x faster                                                        |
| richards                | 45.7 ms                                                | 44.6 ms: 1.03x faster                                                        |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 684 ms: 1.02x faster                                                         |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                         |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                         |
| sqlglot_optimize        | 53.1 ms                                                | 52.0 ms: 1.02x faster                                                        |
| thrift                  | 756 us                                                 | 745 us: 1.02x faster                                                         |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                        |
| pyflate                 | 418 ms                                                 | 412 ms: 1.02x faster                                                         |
| pickle_list             | 4.11 us                                                | 4.05 us: 1.01x faster                                                        |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| pickle                  | 10.1 us                                                | 9.96 us: 1.01x faster                                                        |
| logging_silent          | 101 ns                                                 | 99.9 ns: 1.01x faster                                                        |
| mako                    | 10.1 ms                                                | 9.98 ms: 1.01x faster                                                        |
| coroutines              | 25.5 ms                                                | 25.3 ms: 1.01x faster                                                        |
| coverage                | 100 ms                                                 | 99.2 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                        |
| deepcopy                | 342 us                                                 | 343 us: 1.00x slower                                                         |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                                         |
| dulwich_log             | 63.7 ms                                                | 64.5 ms: 1.01x slower                                                        |
| regex_dna               | 204 ms                                                 | 207 ms: 1.01x slower                                                         |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                       |
| chameleon               | 6.47 ms                                                | 6.58 ms: 1.02x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                        |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 753 ms: 1.02x slower                                                         |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                        |
| deepcopy_reduce         | 2.94 us                                                | 3.01 us: 1.02x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                        |
| unpack_sequence         | 43.1 ns                                                | 44.2 ns: 1.03x slower                                                        |
| unpickle_list           | 4.91 us                                                | 5.04 us: 1.03x slower                                                        |
| nbody                   | 93.1 ms                                                | 95.8 ms: 1.03x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.94 ms: 1.05x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 664 ms: 1.06x slower                                                         |
| generators              | 73.5 ms                                                | 78.6 ms: 1.07x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.45 ms: 1.07x slower                                                        |
| dask                    | 360 ms                                                 | 502 ms: 1.39x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (10): sqlalchemy_imperative, sqlalchemy_declarative, sqlglot_normalize, async_tree_none, go, xml_etree_process, tornado_http, bench_mp_pool, djangocms, unpickle
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
