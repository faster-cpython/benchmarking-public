
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: ba16621
- commit date: 2022-12-17
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                     |
| chameleon      | 6.47 ms                                                | 6.26 ms: 1.03x faster                                                    |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.04x faster                                                   |
| html5lib       | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.0 ms: 1.07x faster                                                    |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                     |
| nbody          | 93.1 ms                                                | 94.1 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                    |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.04x faster                                                    |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.39 ms: 1.34x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                     |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                    |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                    |
| xml_etree_process    | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                    |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                     |
| unpickle_list        | 4.91 us                                                | 5.09 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (3): pickle_list, xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.51 ms: 1.00x faster                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.09 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.9 ms: 1.10x faster                                                    |
| mako            | 10.1 ms                                                | 9.42 ms: 1.07x faster                                                    |
| genshi_text     | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                    |
| django_template | 32.6 ms                                                | 32.2 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.39 ms: 1.34x faster                                                    |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                     |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                    |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                    |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.01 ms: 1.12x faster                                                    |
| deepcopy_memo           | 37.0 us                                                | 33.2 us: 1.11x faster                                                    |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                    |
| genshi_xml              | 51.8 ms                                                | 46.9 ms: 1.10x faster                                                    |
| logging_silent          | 101 ns                                                 | 91.9 ns: 1.10x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                                   |
| richards                | 45.7 ms                                                | 42.0 ms: 1.09x faster                                                    |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                     |
| html5lib                | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                    |
| nqueens                 | 83.4 ms                                                | 77.4 ms: 1.08x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| float                   | 77.2 ms                                                | 72.0 ms: 1.07x faster                                                    |
| mako                    | 10.1 ms                                                | 9.42 ms: 1.07x faster                                                    |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                   |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                                    |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                     |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                                     |
| genshi_text             | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                    |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                     |
| async_generators        | 368 ms                                                 | 348 ms: 1.06x faster                                                     |
| deepcopy                | 342 us                                                 | 323 us: 1.06x faster                                                     |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.06x faster                                                    |
| sqlglot_optimize        | 53.1 ms                                                | 50.3 ms: 1.06x faster                                                    |
| bench_thread_pool       | 819 us                                                 | 777 us: 1.05x faster                                                     |
| spectral_norm           | 100 ms                                                 | 95.1 ms: 1.05x faster                                                    |
| pprint_safe_repr        | 701 ms                                                 | 669 ms: 1.05x faster                                                     |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.05x faster                                                     |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                     |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                     |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.04x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                     |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.04x faster                                                    |
| chameleon               | 6.47 ms                                                | 6.26 ms: 1.03x faster                                                    |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 66.0 ms: 1.03x faster                                                    |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                     |
| chaos                   | 69.2 ms                                                | 67.3 ms: 1.03x faster                                                    |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                                     |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                                    |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                     |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                     |
| json                    | 4.94 ms                                                | 4.81 ms: 1.03x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                   |
| unpack_sequence         | 43.1 ns                                                | 42.1 ns: 1.02x faster                                                    |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                                    |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                     |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                     |
| django_template         | 32.6 ms                                                | 32.2 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                                    |
| xml_etree_process       | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                    |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                    |
| coroutines              | 25.5 ms                                                | 25.3 ms: 1.01x faster                                                    |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                                    |
| python_startup          | 8.52 ms                                                | 8.51 ms: 1.00x faster                                                    |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                     |
| coverage                | 100 ms                                                 | 101 ms: 1.01x slower                                                     |
| nbody                   | 93.1 ms                                                | 94.1 ms: 1.01x slower                                                    |
| crypto_pyaes            | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                    |
| async_tree_none         | 526 ms                                                 | 533 ms: 1.01x slower                                                     |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.09 ms: 1.01x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                                    |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed | 739 ms                                                 | 758 ms: 1.03x slower                                                     |
| unpickle_list           | 4.91 us                                                | 5.09 us: 1.04x slower                                                    |
| generators              | 73.5 ms                                                | 77.0 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (8): thrift, pickle_list, sqlglot_parse, xml_etree_generate, bench_mp_pool, pickle, async_tree_memoization, djangocms
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221217-3.12.0a3+-ba16621/bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
