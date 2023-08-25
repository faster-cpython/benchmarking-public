
# Results vs. 3.11.0

- fork: python
- ref: dff8e5dc8d0758d1f9c5
- machine: linux-x86_64
- commit hash: dff8e5d
- commit date: 2023-04-27
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.77%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                                   |
| chameleon      | 6.47 ms                                                | 6.90 ms: 1.07x slower                                                  |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                 |
| tornado_http   | 96.3 ms                                                | 105 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| nbody          | 93.1 ms                                                | 88.9 ms: 1.05x faster                                                  |
| float          | 77.2 ms                                                | 81.6 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.79 ms: 1.05x faster                                                  |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.1 ms: 1.24x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                   |
| json_loads           | 26.5 us                                                | 25.9 us: 1.02x faster                                                  |
| unpickle_list        | 4.91 us                                                | 4.86 us: 1.01x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 316 us: 1.03x slower                                                   |
| pickle_dict          | 31.1 us                                                | 32.3 us: 1.04x slower                                                  |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                  |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.7 ms: 1.11x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.64 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.07 ms: 1.06x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.66 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 50.2 ms: 1.03x faster                                                  |
| genshi_text     | 21.6 ms                                                | 22.4 ms: 1.04x slower                                                  |
| mako            | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                  |
| django_template | 32.6 ms                                                | 35.1 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.7 ms: 2.39x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                   |
| json_dumps              | 12.6 ms                                                | 10.1 ms: 1.24x faster                                                  |
| mypy2                   | 420 ms                                                 | 349 ms: 1.20x faster                                                   |
| coroutines              | 25.5 ms                                                | 22.3 ms: 1.14x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 216 us: 1.06x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.79 ms: 1.05x faster                                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| nbody                   | 93.1 ms                                                | 88.9 ms: 1.05x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                 |
| richards                | 45.7 ms                                                | 43.7 ms: 1.05x faster                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.04x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                                  |
| fannkuch                | 388 ms                                                 | 373 ms: 1.04x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.54 ms: 1.04x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 50.2 ms: 1.03x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.65 ms: 1.03x faster                                                  |
| nqueens                 | 83.4 ms                                                | 81.3 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                  |
| json_loads              | 26.5 us                                                | 25.9 us: 1.02x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.95 ms: 1.02x faster                                                  |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                   |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                 |
| unpickle_list           | 4.91 us                                                | 4.86 us: 1.01x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                                 |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 749 ms: 1.01x slower                                                   |
| bench_thread_pool       | 819 us                                                 | 830 us: 1.01x slower                                                   |
| coverage                | 100 ms                                                 | 101 ms: 1.01x slower                                                   |
| logging_silent          | 101 ns                                                 | 103 ns: 1.02x slower                                                   |
| raytrace                | 297 ms                                                 | 304 ms: 1.02x slower                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.49 sec: 1.03x slower                                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.62 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 54.6 ms: 1.03x slower                                                  |
| docutils                | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                 |
| sqlglot_normalize       | 108 ms                                                 | 111 ms: 1.03x slower                                                   |
| 2to3                    | 259 ms                                                 | 267 ms: 1.03x slower                                                   |
| comprehensions          | 22.4 us                                                | 23.2 us: 1.03x slower                                                  |
| pickle_pure_python      | 306 us                                                 | 316 us: 1.03x slower                                                   |
| async_tree_memoization  | 627 ms                                                 | 650 ms: 1.04x slower                                                   |
| logging_format          | 6.68 us                                                | 6.93 us: 1.04x slower                                                  |
| logging_simple          | 6.03 us                                                | 6.26 us: 1.04x slower                                                  |
| djangocms               | 32.4 us                                                | 33.7 us: 1.04x slower                                                  |
| pickle_dict             | 31.1 us                                                | 32.3 us: 1.04x slower                                                  |
| genshi_text             | 21.6 ms                                                | 22.4 ms: 1.04x slower                                                  |
| sympy_integrate         | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                  |
| pprint_safe_repr        | 701 ms                                                 | 731 ms: 1.04x slower                                                   |
| telco                   | 6.58 ms                                                | 6.89 ms: 1.05x slower                                                  |
| regex_compile           | 138 ms                                                 | 145 ms: 1.05x slower                                                   |
| deepcopy_memo           | 37.0 us                                                | 38.9 us: 1.05x slower                                                  |
| crypto_pyaes            | 74.7 ms                                                | 78.5 ms: 1.05x slower                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 146 ms: 1.05x slower                                                   |
| float                   | 77.2 ms                                                | 81.6 ms: 1.06x slower                                                  |
| thrift                  | 756 us                                                 | 801 us: 1.06x slower                                                   |
| sympy_expand            | 475 ms                                                 | 503 ms: 1.06x slower                                                   |
| spectral_norm           | 100 ms                                                 | 106 ms: 1.06x slower                                                   |
| mako                    | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                  |
| python_startup          | 8.52 ms                                                | 9.07 ms: 1.06x slower                                                  |
| scimark_sor             | 118 ms                                                 | 126 ms: 1.06x slower                                                   |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                                  |
| chameleon               | 6.47 ms                                                | 6.90 ms: 1.07x slower                                                  |
| sympy_str               | 290 ms                                                 | 309 ms: 1.07x slower                                                   |
| dulwich_log             | 63.7 ms                                                | 68.0 ms: 1.07x slower                                                  |
| deepcopy                | 342 us                                                 | 366 us: 1.07x slower                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 72.8 ms: 1.07x slower                                                  |
| meteor_contest          | 107 ms                                                 | 114 ms: 1.07x slower                                                   |
| django_template         | 32.6 ms                                                | 35.1 ms: 1.08x slower                                                  |
| pyflate                 | 418 ms                                                 | 450 ms: 1.08x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.73 us: 1.08x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.18 us: 1.08x slower                                                  |
| sympy_sum               | 167 ms                                                 | 180 ms: 1.08x slower                                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.4 ms: 1.08x slower                                                  |
| unpickle                | 13.7 us                                                | 14.8 us: 1.08x slower                                                  |
| tornado_http            | 96.3 ms                                                | 105 ms: 1.09x slower                                                   |
| xml_etree_process       | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                  |
| scimark_fft             | 328 ms                                                 | 359 ms: 1.09x slower                                                   |
| unpack_sequence         | 43.1 ns                                                | 47.3 ns: 1.10x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.66 ms: 1.11x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 84.7 ms: 1.11x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.64 us: 1.13x slower                                                  |
| async_generators        | 368 ms                                                 | 440 ms: 1.19x slower                                                   |
| dask                    | 360 ms                                                 | 538 ms: 1.50x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (10): chaos, xml_etree_iterparse, bench_mp_pool, regex_v8, regex_dna, scimark_lu, async_tree_none, html5lib, json, pylint
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.77% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
