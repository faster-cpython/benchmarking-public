
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0fd3891
- commit date: 2023-04-22
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| chameleon      | 6.47 ms                                                | 6.93 ms: 1.07x slower                                  |
| docutils       | 2.63 sec                                               | 2.70 sec: 1.03x slower                                 |
| tornado_http   | 96.3 ms                                                | 104 ms: 1.08x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.4 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| float          | 77.2 ms                                                | 80.4 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.26 ms: 1.22x faster                                  |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                  |
| regex_compile  | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                  |
| json_loads           | 26.5 us                                                | 24.8 us: 1.07x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                   |
| unpickle_pure_python | 228 us                                                 | 219 us: 1.04x faster                                   |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                   |
| pickle               | 10.1 us                                                | 10.5 us: 1.05x slower                                  |
| pickle_list          | 4.11 us                                                | 4.39 us: 1.07x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.24 us: 1.07x slower                                  |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 58.6 ms: 1.09x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 83.2 ms: 1.09x slower                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.05 ms: 1.06x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.65 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 50.7 ms: 1.02x faster                                  |
| mako            | 10.1 ms                                                | 10.5 ms: 1.04x slower                                  |
| genshi_text     | 21.6 ms                                                | 22.7 ms: 1.05x slower                                  |
| django_template | 32.6 ms                                                | 34.7 ms: 1.06x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-linux-x86_64-python-main-3.12.0a7+-0fd3891 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.2 ms: 2.36x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 511 ms: 1.80x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.75 ms: 1.29x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.26 ms: 1.22x faster                                  |
| mypy2                   | 420 ms                                                 | 360 ms: 1.17x faster                                   |
| coroutines              | 25.5 ms                                                | 22.3 ms: 1.14x faster                                  |
| json_loads              | 26.5 us                                                | 24.8 us: 1.07x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.31 ms: 1.07x faster                                  |
| nbody                   | 93.1 ms                                                | 88.4 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 152 ms: 1.04x faster                                   |
| unpickle_pure_python    | 228 us                                                 | 219 us: 1.04x faster                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.63 ms: 1.04x faster                                  |
| richards                | 45.7 ms                                                | 44.0 ms: 1.04x faster                                  |
| json                    | 4.94 ms                                                | 4.75 ms: 1.04x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                  |
| nqueens                 | 83.4 ms                                                | 81.2 ms: 1.03x faster                                  |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.02x faster                                 |
| gc_traversal            | 4.02 ms                                                | 3.93 ms: 1.02x faster                                  |
| genshi_xml              | 51.8 ms                                                | 50.7 ms: 1.02x faster                                  |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                   |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                   |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                  |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                 |
| deltablue               | 3.67 ms                                                | 3.64 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.34 ms: 1.00x faster                                  |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| raytrace                | 297 ms                                                 | 300 ms: 1.01x slower                                   |
| regex_v8                | 22.0 ms                                                | 22.3 ms: 1.01x slower                                  |
| coverage                | 100 ms                                                 | 101 ms: 1.01x slower                                   |
| pickle_pure_python      | 306 us                                                 | 311 us: 1.02x slower                                   |
| pprint_pformat          | 1.46 sec                                               | 1.48 sec: 1.02x slower                                 |
| bench_thread_pool       | 819 us                                                 | 836 us: 1.02x slower                                   |
| logging_simple          | 6.03 us                                                | 6.17 us: 1.02x slower                                  |
| sqlglot_optimize        | 53.1 ms                                                | 54.5 ms: 1.03x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 111 ms: 1.03x slower                                   |
| docutils                | 2.63 sec                                               | 2.70 sec: 1.03x slower                                 |
| deepcopy_memo           | 37.0 us                                                | 38.0 us: 1.03x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 646 ms: 1.03x slower                                   |
| 2to3                    | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| logging_format          | 6.68 us                                                | 6.91 us: 1.03x slower                                  |
| telco                   | 6.58 ms                                                | 6.83 ms: 1.04x slower                                  |
| djangocms               | 32.4 us                                                | 33.6 us: 1.04x slower                                  |
| comprehensions          | 22.4 us                                                | 23.3 us: 1.04x slower                                  |
| regex_compile           | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| float                   | 77.2 ms                                                | 80.4 ms: 1.04x slower                                  |
| sympy_integrate         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                  |
| mako                    | 10.1 ms                                                | 10.5 ms: 1.04x slower                                  |
| sympy_expand            | 475 ms                                                 | 496 ms: 1.04x slower                                   |
| meteor_contest          | 107 ms                                                 | 111 ms: 1.05x slower                                   |
| pickle                  | 10.1 us                                                | 10.5 us: 1.05x slower                                  |
| spectral_norm           | 100 ms                                                 | 105 ms: 1.05x slower                                   |
| scimark_sor             | 118 ms                                                 | 124 ms: 1.05x slower                                   |
| pprint_safe_repr        | 701 ms                                                 | 737 ms: 1.05x slower                                   |
| deepcopy                | 342 us                                                 | 360 us: 1.05x slower                                   |
| thrift                  | 756 us                                                 | 796 us: 1.05x slower                                   |
| genshi_text             | 21.6 ms                                                | 22.7 ms: 1.05x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.66 us: 1.06x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 78.9 ms: 1.06x slower                                  |
| python_startup          | 8.52 ms                                                | 9.05 ms: 1.06x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.06x slower                                   |
| django_template         | 32.6 ms                                                | 34.7 ms: 1.06x slower                                  |
| dulwich_log             | 63.7 ms                                                | 67.8 ms: 1.06x slower                                  |
| pickle_list             | 4.11 us                                                | 4.39 us: 1.07x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.24 us: 1.07x slower                                  |
| chameleon               | 6.47 ms                                                | 6.93 ms: 1.07x slower                                  |
| sympy_str               | 290 ms                                                 | 311 ms: 1.07x slower                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.2 ms: 1.07x slower                                  |
| scimark_fft             | 328 ms                                                 | 353 ms: 1.08x slower                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 73.3 ms: 1.08x slower                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.86 ms: 1.08x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.18 us: 1.08x slower                                  |
| tornado_http            | 96.3 ms                                                | 104 ms: 1.08x slower                                   |
| sympy_sum               | 167 ms                                                 | 181 ms: 1.09x slower                                   |
| unpickle                | 13.7 us                                                | 14.9 us: 1.09x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 58.6 ms: 1.09x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 83.2 ms: 1.09x slower                                  |
| pyflate                 | 418 ms                                                 | 459 ms: 1.10x slower                                   |
| unpack_sequence         | 43.1 ns                                                | 47.4 ns: 1.10x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.65 ms: 1.11x slower                                  |
| async_generators        | 368 ms                                                 | 445 ms: 1.21x slower                                   |
| dask                    | 360 ms                                                 | 539 ms: 1.50x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (9): async_tree_none, bench_mp_pool, async_tree_io, chaos, scimark_lu, pylint, logging_silent, async_tree_cpu_io_mixed, html5lib
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.80% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
