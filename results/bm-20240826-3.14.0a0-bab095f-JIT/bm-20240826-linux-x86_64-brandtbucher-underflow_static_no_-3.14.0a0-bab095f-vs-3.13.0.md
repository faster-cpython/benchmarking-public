# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_static_no_
- machine: linux-x86_64
- commit hash: bab095f
- commit date: 2024-08-26
- overall geometric mean: 1.01x slower
- HPT reliability: 58.63%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 283 ms: 1.07x slower                                                        |
| docutils       | 2.58 sec                                               | 3.35 sec: 1.30x slower                                                      |
| html5lib       | 64.5 ms                                                | 71.2 ms: 1.10x slower                                                       |
| tornado_http   | 91.5 ms                                                | 102 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                  | 1.14x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                        |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 556 ms: 1.03x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                       |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 522 ms: 1.07x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 903 ms: 1.09x slower                                                        |
| async_tree_io             | 843 ms                                                 | 939 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                       |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                        |
| regex_compile  | 131 ms                                                 | 151 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.1 ms: 1.13x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| tomli_loads          | 2.11 sec                                               | 1.99 sec: 1.06x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 205 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 98.8 ms: 1.03x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 314 us: 1.05x slower                                                        |
| json_loads           | 27.0 us                                                | 28.4 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.60 ms: 1.16x faster                                                       |
| django_template | 34.4 ms                                                | 37.2 ms: 1.08x slower                                                       |
| genshi_text     | 22.9 ms                                                | 24.8 ms: 1.09x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 25.7 us: 1.48x faster                                                       |
| richards                  | 48.1 ms                                                | 37.7 ms: 1.28x faster                                                       |
| deepcopy                  | 352 us                                                 | 278 us: 1.27x faster                                                        |
| richards_super            | 54.4 ms                                                | 43.2 ms: 1.26x faster                                                       |
| scimark_fft               | 369 ms                                                 | 311 ms: 1.18x faster                                                        |
| deepcopy_reduce           | 3.17 us                                                | 2.71 us: 1.17x faster                                                       |
| mako                      | 11.1 ms                                                | 9.60 ms: 1.16x faster                                                       |
| spectral_norm             | 115 ms                                                 | 99.5 ms: 1.16x faster                                                       |
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.42 ms: 1.14x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 77.1 ms: 1.13x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                        |
| xml_etree_process         | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 65.5 ms: 1.11x faster                                                       |
| float                     | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                       |
| telco                     | 8.45 ms                                                | 7.70 ms: 1.10x faster                                                       |
| pathlib                   | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                       |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| regex_effbot              | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 1.99 sec: 1.06x faster                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                      |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.06x faster                                                        |
| nbody                     | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                       |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.05x faster                                                        |
| json_dumps                | 10.4 ms                                                | 9.96 ms: 1.04x faster                                                       |
| unpickle_pure_python      | 213 us                                                 | 205 us: 1.04x faster                                                        |
| pyflate                   | 460 ms                                                 | 442 ms: 1.04x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.66 ms: 1.04x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 98.8 ms: 1.03x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                        |
| regex_v8                  | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 556 ms: 1.03x faster                                                        |
| logging_simple            | 5.66 us                                                | 5.54 us: 1.02x faster                                                       |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| thrift                    | 796 us                                                 | 779 us: 1.02x faster                                                        |
| fannkuch                  | 381 ms                                                 | 373 ms: 1.02x faster                                                        |
| pprint_safe_repr          | 744 ms                                                 | 729 ms: 1.02x faster                                                        |
| scimark_monte_carlo       | 66.3 ms                                                | 65.2 ms: 1.02x faster                                                       |
| regex_dna                 | 220 ms                                                 | 218 ms: 1.01x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.73 sec: 1.01x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| pprint_pformat            | 1.51 sec                                               | 1.52 sec: 1.01x slower                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                       |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                       |
| json                      | 5.20 ms                                                | 5.29 ms: 1.02x slower                                                       |
| coverage                  | 83.7 ms                                                | 85.6 ms: 1.02x slower                                                       |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                        |
| python_startup_no_site    | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 844 us: 1.04x slower                                                        |
| deltablue                 | 3.15 ms                                                | 3.26 ms: 1.04x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 314 us: 1.05x slower                                                        |
| chaos                     | 58.4 ms                                                | 61.2 ms: 1.05x slower                                                       |
| nqueens                   | 80.6 ms                                                | 84.4 ms: 1.05x slower                                                       |
| json_loads                | 27.0 us                                                | 28.4 us: 1.05x slower                                                       |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 522 ms: 1.07x slower                                                        |
| 2to3                      | 265 ms                                                 | 283 ms: 1.07x slower                                                        |
| raytrace                  | 262 ms                                                 | 280 ms: 1.07x slower                                                        |
| django_template           | 34.4 ms                                                | 37.2 ms: 1.08x slower                                                       |
| genshi_text               | 22.9 ms                                                | 24.8 ms: 1.09x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 903 ms: 1.09x slower                                                        |
| html5lib                  | 64.5 ms                                                | 71.2 ms: 1.10x slower                                                       |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                       |
| async_tree_io             | 843 ms                                                 | 939 ms: 1.11x slower                                                        |
| tornado_http              | 91.5 ms                                                | 102 ms: 1.12x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 120 ms: 1.12x slower                                                        |
| hexiom                    | 6.13 ms                                                | 6.92 ms: 1.13x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 61.1 ms: 1.13x slower                                                       |
| sympy_expand              | 462 ms                                                 | 523 ms: 1.13x slower                                                        |
| regex_compile             | 131 ms                                                 | 151 ms: 1.15x slower                                                        |
| genshi_xml                | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| sqlglot_transpile         | 1.57 ms                                                | 1.88 ms: 1.19x slower                                                       |
| sympy_str                 | 274 ms                                                 | 328 ms: 1.20x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.53 ms: 1.21x slower                                                       |
| go                        | 142 ms                                                 | 173 ms: 1.22x slower                                                        |
| sympy_integrate           | 19.9 ms                                                | 24.5 ms: 1.23x slower                                                       |
| docutils                  | 2.58 sec                                               | 3.35 sec: 1.30x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 194 ms: 1.30x slower                                                        |
| pylint                    | 313 ms                                                 | 412 ms: 1.32x slower                                                        |
| generators                | 28.8 ms                                                | 41.1 ms: 1.43x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (6): logging_format, async_tree_cpu_io_mixed_tg, pycparser, bench_mp_pool, asyncio_websockets, logging_silent
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 58.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x