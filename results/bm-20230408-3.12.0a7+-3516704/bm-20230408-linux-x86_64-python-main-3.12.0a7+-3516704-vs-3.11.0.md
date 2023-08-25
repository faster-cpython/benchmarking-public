
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.51 ms: 1.01x slower                                  |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                 |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                  |
| tornado_http   | 96.3 ms                                                | 94.0 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.6 ms: 1.08x faster                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| float          | 77.2 ms                                                | 73.6 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.36 ms: 1.19x faster                                  |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.54 ms: 1.32x faster                                  |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                   |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.07 us: 1.03x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 55.9 ms: 1.04x slower                                  |
| pickle_list          | 4.11 us                                                | 4.29 us: 1.04x slower                                  |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 81.2 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.82 ms: 1.04x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.8 ms: 1.08x faster                                  |
| mako            | 10.1 ms                                                | 9.97 ms: 1.01x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.0 ms: 2.54x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.54 ms: 1.32x faster                                  |
| mypy2                   | 420 ms                                                 | 336 ms: 1.25x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.36 ms: 1.19x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.21 ms: 1.16x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.49 ms: 1.14x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                   |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.99 ms: 1.13x faster                                  |
| coroutines              | 25.5 ms                                                | 22.8 ms: 1.12x faster                                  |
| gc_traversal            | 4.02 ms                                                | 3.65 ms: 1.10x faster                                  |
| scimark_fft             | 328 ms                                                 | 298 ms: 1.10x faster                                   |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.09x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.08x faster                                  |
| genshi_xml              | 51.8 ms                                                | 47.8 ms: 1.08x faster                                  |
| nbody                   | 93.1 ms                                                | 86.6 ms: 1.08x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| logging_silent          | 101 ns                                                 | 94.3 ns: 1.07x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                  |
| logging_simple          | 6.03 us                                                | 5.65 us: 1.07x faster                                  |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                  |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                 |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                   |
| spectral_norm           | 100 ms                                                 | 94.5 ms: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.32 us: 1.06x faster                                  |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.06x faster                                   |
| scimark_lu              | 110 ms                                                 | 104 ms: 1.06x faster                                   |
| deepcopy                | 342 us                                                 | 324 us: 1.05x faster                                   |
| chaos                   | 69.2 ms                                                | 65.7 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                  |
| float                   | 77.2 ms                                                | 73.6 ms: 1.05x faster                                  |
| json                    | 4.94 ms                                                | 4.71 ms: 1.05x faster                                  |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                   |
| richards                | 45.7 ms                                                | 43.6 ms: 1.05x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                  |
| bench_thread_pool       | 819 us                                                 | 786 us: 1.04x faster                                   |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                   |
| nqueens                 | 83.4 ms                                                | 80.5 ms: 1.04x faster                                  |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                   |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                 |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| comprehensions          | 22.4 us                                                | 21.8 us: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                   |
| regex_compile           | 138 ms                                                 | 135 ms: 1.03x faster                                   |
| coverage                | 100 ms                                                 | 97.6 ms: 1.03x faster                                  |
| tornado_http            | 96.3 ms                                                | 94.0 ms: 1.02x faster                                  |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 66.7 ms: 1.02x faster                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                 |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                  |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.01x faster                                   |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                  |
| mako                    | 10.1 ms                                                | 9.97 ms: 1.01x faster                                  |
| genshi_text             | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| telco                   | 6.58 ms                                                | 6.52 ms: 1.01x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 697 ms: 1.01x faster                                   |
| pathlib                 | 18.2 ms                                                | 18.3 ms: 1.00x slower                                  |
| pyflate                 | 418 ms                                                 | 420 ms: 1.00x slower                                   |
| chameleon               | 6.47 ms                                                | 6.51 ms: 1.01x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 43.5 ns: 1.01x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 139 ms: 1.01x slower                                   |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 637 ms: 1.01x slower                                   |
| pickle_dict             | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| thrift                  | 756 us                                                 | 779 us: 1.03x slower                                   |
| unpickle_list           | 4.91 us                                                | 5.07 us: 1.03x slower                                  |
| python_startup          | 8.52 ms                                                | 8.82 ms: 1.04x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 55.9 ms: 1.04x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                  |
| pickle_list             | 4.11 us                                                | 4.29 us: 1.04x slower                                  |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 81.2 ms: 1.06x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.51 ms: 1.08x slower                                  |
| async_generators        | 368 ms                                                 | 412 ms: 1.12x slower                                   |
| dask                    | 360 ms                                                 | 502 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (11): async_tree_none, djangocms, dulwich_log, bench_mp_pool, mdp, async_tree_cpu_io_mixed, regex_dna, async_tree_io, regex_v8, sqlalchemy_imperative, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
