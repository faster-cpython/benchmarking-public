
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d71edbd
- commit date: 2023-02-25
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.39 ms: 1.01x faster                                  |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                 |
| html5lib       | 64.5 ms                                                | 61.1 ms: 1.06x faster                                  |
| tornado_http   | 96.3 ms                                                | 94.3 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.9 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| nbody          | 93.1 ms                                                | 96.6 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.65 ms: 1.09x faster                                  |
| regex_compile  | 138 ms                                                 | 131 ms: 1.06x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                  |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.45 ms: 1.33x faster                                  |
| unpickle_pure_python | 228 us                                                 | 195 us: 1.17x faster                                   |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                  |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                  |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                  |
| pickle_list          | 4.11 us                                                | 4.19 us: 1.02x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 55.0 ms: 1.02x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.3 ms: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.01 ms: 1.06x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.3 ms: 1.12x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.4 ms: 1.06x faster                                  |
| mako            | 10.1 ms                                                | 9.89 ms: 1.02x faster                                  |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.6 ms: 2.48x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 502 ms: 1.84x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.45 ms: 1.33x faster                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                   |
| unpickle_pure_python    | 228 us                                                 | 195 us: 1.17x faster                                   |
| deltablue               | 3.67 ms                                                | 3.14 ms: 1.17x faster                                  |
| richards                | 45.7 ms                                                | 40.6 ms: 1.13x faster                                  |
| genshi_xml              | 51.8 ms                                                | 46.3 ms: 1.12x faster                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                   |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| coroutines              | 25.5 ms                                                | 23.0 ms: 1.11x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.65 ms: 1.09x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| json                    | 4.94 ms                                                | 4.54 ms: 1.09x faster                                  |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                   |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                 |
| logging_silent          | 101 ns                                                 | 94.4 ns: 1.07x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                  |
| fannkuch                | 388 ms                                                 | 364 ms: 1.07x faster                                   |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.01 ms: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                  |
| regex_compile           | 138 ms                                                 | 131 ms: 1.06x faster                                   |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.06x faster                                  |
| html5lib                | 64.5 ms                                                | 61.1 ms: 1.06x faster                                  |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.05x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.5 ms: 1.05x faster                                  |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                   |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                  |
| float                   | 77.2 ms                                                | 73.9 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| nqueens                 | 83.4 ms                                                | 80.0 ms: 1.04x faster                                  |
| bench_thread_pool       | 819 us                                                 | 787 us: 1.04x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| spectral_norm           | 100 ms                                                 | 96.4 ms: 1.04x faster                                  |
| scimark_fft             | 328 ms                                                 | 317 ms: 1.04x faster                                   |
| coverage                | 100 ms                                                 | 96.5 ms: 1.04x faster                                  |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                  |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                 |
| chaos                   | 69.2 ms                                                | 67.0 ms: 1.03x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 66.0 ms: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 681 ms: 1.03x faster                                   |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                   |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                   |
| tornado_http            | 96.3 ms                                                | 94.3 ms: 1.02x faster                                  |
| mako                    | 10.1 ms                                                | 9.89 ms: 1.02x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                  |
| unpack_sequence         | 43.1 ns                                                | 42.4 ns: 1.02x faster                                  |
| chameleon               | 6.47 ms                                                | 6.39 ms: 1.01x faster                                  |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.7 ms: 1.01x faster                                  |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.99 us: 1.02x slower                                  |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                 |
| pickle_dict             | 31.1 us                                                | 31.7 us: 1.02x slower                                  |
| thrift                  | 756 us                                                 | 771 us: 1.02x slower                                   |
| async_tree_memoization  | 627 ms                                                 | 640 ms: 1.02x slower                                   |
| pickle_list             | 4.11 us                                                | 4.19 us: 1.02x slower                                  |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                   |
| xml_etree_process       | 53.9 ms                                                | 55.0 ms: 1.02x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.62 ms: 1.03x slower                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                  |
| nbody                   | 93.1 ms                                                | 96.6 ms: 1.04x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.3 ms: 1.05x slower                                  |
| python_startup          | 8.52 ms                                                | 9.01 ms: 1.06x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                  |
| async_generators        | 368 ms                                                 | 420 ms: 1.14x slower                                   |
| dask                    | 360 ms                                                 | 499 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (10): sqlalchemy_declarative, telco, async_tree_none, sqlglot_transpile, sympy_sum, bench_mp_pool, async_tree_cpu_io_mixed, crypto_pyaes, async_tree_io, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
