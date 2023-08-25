
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 9e5a8e4
- commit date: 2022-12-22
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.02x faster                                                     |
| chameleon      | 6.47 ms                                                | 6.52 ms: 1.01x slower                                                    |
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                   |
| html5lib       | 64.5 ms                                                | 60.4 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                    |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                     |
| nbody          | 93.1 ms                                                | 96.6 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                    |
| regex_compile  | 138 ms                                                 | 131 ms: 1.06x faster                                                     |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                    |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                     |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                    |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                     |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                    |
| xml_etree_process    | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                    |
| pickle_list          | 4.11 us                                                | 4.09 us: 1.00x faster                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                     |
| unpickle_list        | 4.91 us                                                | 5.03 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.55 ms: 1.00x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.13 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                    |
| mako            | 10.1 ms                                                | 9.37 ms: 1.08x faster                                                    |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.04x faster                                                    |
| django_template | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.43 ms: 1.33x faster                                                    |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                     |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                    |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.14x faster                                                     |
| regex_effbot            | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                    |
| deepcopy_memo           | 37.0 us                                                | 33.2 us: 1.11x faster                                                    |
| logging_silent          | 101 ns                                                 | 90.9 ns: 1.11x faster                                                    |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                    |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                    |
| mako                    | 10.1 ms                                                | 9.37 ms: 1.08x faster                                                    |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                     |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.20 ms: 1.07x faster                                                    |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                                    |
| html5lib                | 64.5 ms                                                | 60.4 ms: 1.07x faster                                                    |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                   |
| logging_format          | 6.68 us                                                | 6.28 us: 1.06x faster                                                    |
| logging_simple          | 6.03 us                                                | 5.68 us: 1.06x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                     |
| nqueens                 | 83.4 ms                                                | 78.7 ms: 1.06x faster                                                    |
| hexiom                  | 6.37 ms                                                | 6.02 ms: 1.06x faster                                                    |
| regex_compile           | 138 ms                                                 | 131 ms: 1.06x faster                                                     |
| pprint_safe_repr        | 701 ms                                                 | 665 ms: 1.05x faster                                                     |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 780 us: 1.05x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.4 ms: 1.05x faster                                                    |
| async_generators        | 368 ms                                                 | 352 ms: 1.05x faster                                                     |
| pyflate                 | 418 ms                                                 | 399 ms: 1.05x faster                                                     |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                                    |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                                     |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.04x faster                                                    |
| telco                   | 6.58 ms                                                | 6.31 ms: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                     |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                     |
| chaos                   | 69.2 ms                                                | 67.0 ms: 1.03x faster                                                    |
| spectral_norm           | 100 ms                                                 | 97.1 ms: 1.03x faster                                                    |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                     |
| coroutines              | 25.5 ms                                                | 24.9 ms: 1.02x faster                                                    |
| dulwich_log             | 63.7 ms                                                | 62.2 ms: 1.02x faster                                                    |
| pickle_dict             | 31.1 us                                                | 30.4 us: 1.02x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                    |
| django_template         | 32.6 ms                                                | 32.0 ms: 1.02x faster                                                    |
| 2to3                    | 259 ms                                                 | 255 ms: 1.02x faster                                                     |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                                     |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                     |
| xml_etree_process       | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 2.94 us                                                | 2.91 us: 1.01x faster                                                    |
| unpack_sequence         | 43.1 ns                                                | 42.6 ns: 1.01x faster                                                    |
| pickle_list             | 4.11 us                                                | 4.09 us: 1.00x faster                                                    |
| python_startup          | 8.52 ms                                                | 8.55 ms: 1.00x slower                                                    |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                                     |
| chameleon               | 6.47 ms                                                | 6.52 ms: 1.01x slower                                                    |
| docutils                | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                   |
| thrift                  | 756 us                                                 | 763 us: 1.01x slower                                                     |
| crypto_pyaes            | 74.7 ms                                                | 75.8 ms: 1.02x slower                                                    |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                    |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                                    |
| python_startup_no_site  | 6.01 ms                                                | 6.13 ms: 1.02x slower                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                     |
| unpickle_list           | 4.91 us                                                | 5.03 us: 1.02x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                                    |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                                   |
| async_tree_none         | 526 ms                                                 | 541 ms: 1.03x slower                                                     |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                     |
| nbody                   | 93.1 ms                                                | 96.6 ms: 1.04x slower                                                    |
| coverage                | 100 ms                                                 | 104 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed | 739 ms                                                 | 769 ms: 1.04x slower                                                     |
| mdp                     | 2.62 sec                                               | 2.73 sec: 1.04x slower                                                   |
| generators              | 73.5 ms                                                | 76.8 ms: 1.05x slower                                                    |
| json                    | 4.94 ms                                                | 5.17 ms: 1.05x slower                                                    |
| async_tree_memoization  | 627 ms                                                 | 683 ms: 1.09x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (9): meteor_contest, scimark_monte_carlo, richards, sympy_sum, bench_mp_pool, xml_etree_generate, pickle, unpickle, djangocms
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221222-3.12.0a3+-9e5a8e4/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4.json: mypy


# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
