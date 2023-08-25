
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 57469f4
- commit date: 2023-01-28
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.40 ms: 1.01x faster                                                      |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                     |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                      |
| tornado_http   | 96.3 ms                                                | 94.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                       |
| float          | 77.2 ms                                                | 75.1 ms: 1.03x faster                                                      |
| nbody          | 93.1 ms                                                | 92.3 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.60 ms: 1.11x faster                                                      |
| regex_compile  | 138 ms                                                 | 131 ms: 1.06x faster                                                       |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                      |
| regex_dna      | 204 ms                                                 | 219 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 208 us: 1.10x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 292 us: 1.05x faster                                                       |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                                      |
| pickle_list          | 4.11 us                                                | 4.06 us: 1.01x faster                                                      |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                      |
| pickle               | 10.1 us                                                | 9.98 us: 1.01x faster                                                      |
| xml_etree_process    | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                      |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.07 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.70 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.23 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.4 ms: 1.11x faster                                                      |
| mako            | 10.1 ms                                                | 9.44 ms: 1.07x faster                                                      |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                      |
| django_template | 32.6 ms                                                | 32.4 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 496 ms: 1.86x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.94 ms: 1.14x faster                                                      |
| logging_silent          | 101 ns                                                 | 90.2 ns: 1.12x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 46.4 ms: 1.11x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.60 ms: 1.11x faster                                                      |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                      |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 208 us: 1.10x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.35 ms: 1.10x faster                                                      |
| scimark_fft             | 328 ms                                                 | 302 ms: 1.09x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.0 us: 1.09x faster                                                      |
| sympy_str               | 290 ms                                                 | 270 ms: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                                      |
| gc_traversal            | 4.02 ms                                                | 3.76 ms: 1.07x faster                                                      |
| nqueens                 | 83.4 ms                                                | 78.0 ms: 1.07x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                                     |
| mako                    | 10.1 ms                                                | 9.44 ms: 1.07x faster                                                      |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                       |
| richards                | 45.7 ms                                                | 42.9 ms: 1.07x faster                                                      |
| regex_compile           | 138 ms                                                 | 131 ms: 1.06x faster                                                       |
| deepcopy                | 342 us                                                 | 324 us: 1.05x faster                                                       |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                      |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                      |
| logging_format          | 6.68 us                                                | 6.37 us: 1.05x faster                                                      |
| chaos                   | 69.2 ms                                                | 65.9 ms: 1.05x faster                                                      |
| logging_simple          | 6.03 us                                                | 5.75 us: 1.05x faster                                                      |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                                       |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                      |
| pickle_pure_python      | 306 us                                                 | 292 us: 1.05x faster                                                       |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                      |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.04x faster                                                       |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                                      |
| spectral_norm           | 100 ms                                                 | 96.1 ms: 1.04x faster                                                      |
| async_generators        | 368 ms                                                 | 355 ms: 1.04x faster                                                       |
| telco                   | 6.58 ms                                                | 6.34 ms: 1.04x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.04x faster                                                      |
| hexiom                  | 6.37 ms                                                | 6.16 ms: 1.03x faster                                                      |
| unpack_sequence         | 43.1 ns                                                | 41.7 ns: 1.03x faster                                                      |
| pprint_safe_repr        | 701 ms                                                 | 681 ms: 1.03x faster                                                       |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                       |
| float                   | 77.2 ms                                                | 75.1 ms: 1.03x faster                                                      |
| crypto_pyaes            | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.02x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                     |
| tornado_http            | 96.3 ms                                                | 94.3 ms: 1.02x faster                                                      |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                       |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                       |
| thrift                  | 756 us                                                 | 744 us: 1.02x faster                                                       |
| pickle_list             | 4.11 us                                                | 4.06 us: 1.01x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 67.3 ms: 1.01x faster                                                      |
| chameleon               | 6.47 ms                                                | 6.40 ms: 1.01x faster                                                      |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                      |
| nbody                   | 93.1 ms                                                | 92.3 ms: 1.01x faster                                                      |
| pickle                  | 10.1 us                                                | 9.98 us: 1.01x faster                                                      |
| deepcopy_reduce         | 2.94 us                                                | 2.91 us: 1.01x faster                                                      |
| fannkuch                | 388 ms                                                 | 385 ms: 1.01x faster                                                       |
| django_template         | 32.6 ms                                                | 32.4 ms: 1.01x faster                                                      |
| xml_etree_process       | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                      |
| go                      | 140 ms                                                 | 140 ms: 1.00x slower                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                      |
| generators              | 73.5 ms                                                | 74.4 ms: 1.01x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                      |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                       |
| coroutines              | 25.5 ms                                                | 26.0 ms: 1.02x slower                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                      |
| python_startup          | 8.52 ms                                                | 8.70 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 755 ms: 1.02x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                      |
| regex_v8                | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                      |
| unpickle_list           | 4.91 us                                                | 5.07 us: 1.03x slower                                                      |
| pyflate                 | 418 ms                                                 | 432 ms: 1.03x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.23 ms: 1.04x slower                                                      |
| async_tree_memoization  | 627 ms                                                 | 661 ms: 1.05x slower                                                       |
| regex_dna               | 204 ms                                                 | 219 ms: 1.08x slower                                                       |
| dask                    | 360 ms                                                 | 511 ms: 1.42x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (5): async_tree_none, bench_mp_pool, djangocms, scimark_sor, async_tree_io
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230128-3.12.0a4+-57469f4/bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
