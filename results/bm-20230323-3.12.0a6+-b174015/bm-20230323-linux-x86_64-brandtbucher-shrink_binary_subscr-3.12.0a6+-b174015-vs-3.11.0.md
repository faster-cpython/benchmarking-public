
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: b174015
- commit date: 2023-03-23
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                         |
| chameleon      | 6.47 ms                                                | 6.52 ms: 1.01x slower                                                        |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                       |
| html5lib       | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                        |
| tornado_http   | 96.3 ms                                                | 91.4 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.5 ms: 1.05x faster                                                        |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| float          | 77.2 ms                                                | 74.0 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                        |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                         |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                        |
| regex_dna      | 204 ms                                                 | 211 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.68 ms: 1.30x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                         |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 100.0 ms: 1.04x faster                                                       |
| pickle_dict          | 31.1 us                                                | 31.1 us: 1.00x faster                                                        |
| unpickle_list        | 4.91 us                                                | 5.03 us: 1.03x slower                                                        |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 57.2 ms: 1.06x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.37 us: 1.06x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 82.1 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.7 ms: 1.09x faster                                                        |
| mako            | 10.1 ms                                                | 9.85 ms: 1.02x faster                                                        |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.1 ms: 2.53x faster                                                        |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                                         |
| json_dumps              | 12.6 ms                                                | 9.68 ms: 1.30x faster                                                        |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                         |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                        |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                         |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                        |
| coroutines              | 25.5 ms                                                | 23.0 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.14 ms: 1.09x faster                                                        |
| json                    | 4.94 ms                                                | 4.55 ms: 1.09x faster                                                        |
| genshi_xml              | 51.8 ms                                                | 47.7 ms: 1.09x faster                                                        |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 1.02 ms: 1.08x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                        |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                         |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.07x faster                                                         |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                         |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                         |
| richards                | 45.7 ms                                                | 42.9 ms: 1.07x faster                                                        |
| spectral_norm           | 100 ms                                                 | 94.5 ms: 1.06x faster                                                        |
| hexiom                  | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                        |
| tornado_http            | 96.3 ms                                                | 91.4 ms: 1.05x faster                                                        |
| nbody                   | 93.1 ms                                                | 88.5 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                         |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                         |
| logging_format          | 6.68 us                                                | 6.38 us: 1.05x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.04x faster                                                        |
| float                   | 77.2 ms                                                | 74.0 ms: 1.04x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                                        |
| coverage                | 100 ms                                                 | 96.1 ms: 1.04x faster                                                        |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                                         |
| xml_etree_iterparse     | 104 ms                                                 | 100.0 ms: 1.04x faster                                                       |
| html5lib                | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                         |
| chaos                   | 69.2 ms                                                | 66.9 ms: 1.03x faster                                                        |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                         |
| logging_silent          | 101 ns                                                 | 97.9 ns: 1.03x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.90 ms: 1.03x faster                                                        |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                         |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                         |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                       |
| mako                    | 10.1 ms                                                | 9.85 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                        |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                         |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                         |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                       |
| unpack_sequence         | 43.1 ns                                                | 42.4 ns: 1.02x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.5 ms: 1.02x faster                                                        |
| telco                   | 6.58 ms                                                | 6.49 ms: 1.02x faster                                                        |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                         |
| nqueens                 | 83.4 ms                                                | 82.6 ms: 1.01x faster                                                        |
| pyflate                 | 418 ms                                                 | 416 ms: 1.01x faster                                                         |
| pickle_dict             | 31.1 us                                                | 31.1 us: 1.00x faster                                                        |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                        |
| chameleon               | 6.47 ms                                                | 6.52 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 746 ms: 1.01x slower                                                         |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.01x slower                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 69.1 ms: 1.01x slower                                                        |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                        |
| mdp                     | 2.62 sec                                               | 2.68 sec: 1.02x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.03 us: 1.03x slower                                                        |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                        |
| regex_dna               | 204 ms                                                 | 211 ms: 1.04x slower                                                         |
| python_startup          | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                        |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                        |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                         |
| comprehensions          | 22.4 us                                                | 23.7 us: 1.05x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 57.2 ms: 1.06x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.37 us: 1.06x slower                                                        |
| thrift                  | 756 us                                                 | 812 us: 1.07x slower                                                         |
| xml_etree_generate      | 76.2 ms                                                | 82.1 ms: 1.08x slower                                                        |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                        |
| async_generators        | 368 ms                                                 | 409 ms: 1.11x slower                                                         |
| dask                    | 360 ms                                                 | 512 ms: 1.42x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (14): unpickle, genshi_text, pathlib, sqlalchemy_declarative, dulwich_log, create_gc_cycles, async_tree_none, bench_mp_pool, sympy_sum, go, async_tree_io, deepcopy_reduce, djangocms, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
