# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.20x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 290 ms: 1.10x slower                                       |
| chameleon      | 6.85 ms                                                | 7.87 ms: 1.15x slower                                      |
| docutils       | 2.58 sec                                               | 2.95 sec: 1.14x slower                                     |
| html5lib       | 64.5 ms                                                | 70.5 ms: 1.09x slower                                      |
| tornado_http   | 91.5 ms                                                | 102 ms: 1.12x slower                                       |
| Geometric mean | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 510 ms: 1.04x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.90 sec: 1.06x slower                                     |
| async_generators           | 433 ms                                                 | 476 ms: 1.10x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 838 ms: 1.46x slower                                       |
| async_tree_none            | 354 ms                                                 | 533 ms: 1.51x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 702 ms: 1.51x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 848 ms: 1.56x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 704 ms: 1.59x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 537 ms: 1.68x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.49 sec: 1.77x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.50 sec: 1.82x slower                                     |
| Geometric mean             | (ref)                                                  | 1.37x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                       |
| float          | 78.5 ms                                                | 88.3 ms: 1.12x slower                                      |
| nbody          | 85.7 ms                                                | 105 ms: 1.23x slower                                       |
| Geometric mean | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.52 ms: 1.10x faster                                      |
| regex_v8       | 25.3 ms                                                | 23.7 ms: 1.06x faster                                      |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                       |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 11.6 us                                                | 10.6 us: 1.10x faster                                      |
| pickle_list          | 5.01 us                                                | 4.87 us: 1.03x faster                                      |
| pickle_dict          | 33.2 us                                                | 33.2 us: 1.00x slower                                      |
| unpickle_list        | 4.96 us                                                | 4.99 us: 1.00x slower                                      |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                      |
| unpickle             | 14.9 us                                                | 15.8 us: 1.06x slower                                      |
| pickle_pure_python   | 300 us                                                 | 318 us: 1.06x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.24 sec: 1.06x slower                                     |
| xml_etree_generate   | 87.0 ms                                                | 94.2 ms: 1.08x slower                                      |
| xml_etree_process    | 60.4 ms                                                | 65.4 ms: 1.08x slower                                      |
| json_loads           | 27.0 us                                                | 29.3 us: 1.09x slower                                      |
| unpickle_pure_python | 213 us                                                 | 234 us: 1.10x slower                                       |
| xml_etree_parse      | 156 ms                                                 | 172 ms: 1.10x slower                                       |
| xml_etree_iterparse  | 102 ms                                                 | 114 ms: 1.11x slower                                       |
| Geometric mean       | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 12.1 ms: 1.14x slower                                      |
| python_startup_no_site | 6.99 ms                                                | 10.5 ms: 1.50x slower                                      |
| Geometric mean         | (ref)                                                  | 1.31x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.08x slower                                      |
| mako            | 11.1 ms                                                | 12.0 ms: 1.08x slower                                      |
| django_template | 34.4 ms                                                | 37.3 ms: 1.08x slower                                      |
| genshi_xml      | 50.3 ms                                                | 55.0 ms: 1.09x slower                                      |
| Geometric mean  | (ref)                                                  | 1.08x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 124 us: 1.29x faster                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.26 ms: 1.28x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.52 ms: 1.10x faster                                      |
| pickle                     | 11.6 us                                                | 10.6 us: 1.10x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.52 ms: 1.08x faster                                      |
| regex_v8                   | 25.3 ms                                                | 23.7 ms: 1.06x faster                                      |
| pickle_list                | 5.01 us                                                | 4.87 us: 1.03x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.5 ms: 1.02x faster                                      |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                       |
| pickle_dict                | 33.2 us                                                | 33.2 us: 1.00x slower                                      |
| unpickle_list              | 4.96 us                                                | 4.99 us: 1.00x slower                                      |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                       |
| pyflate                    | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| crypto_pyaes               | 73.0 ms                                                | 74.5 ms: 1.02x slower                                      |
| json                       | 5.20 ms                                                | 5.33 ms: 1.03x slower                                      |
| richards                   | 48.1 ms                                                | 49.6 ms: 1.03x slower                                      |
| richards_super             | 54.4 ms                                                | 56.0 ms: 1.03x slower                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.27 us: 1.03x slower                                      |
| deepcopy                   | 352 us                                                 | 368 us: 1.04x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 510 ms: 1.04x slower                                       |
| scimark_lu                 | 115 ms                                                 | 120 ms: 1.05x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                       |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                      |
| go                         | 142 ms                                                 | 149 ms: 1.06x slower                                       |
| nqueens                    | 80.6 ms                                                | 85.2 ms: 1.06x slower                                      |
| unpickle                   | 14.9 us                                                | 15.8 us: 1.06x slower                                      |
| scimark_fft                | 369 ms                                                 | 391 ms: 1.06x slower                                       |
| regex_compile              | 131 ms                                                 | 139 ms: 1.06x slower                                       |
| pickle_pure_python         | 300 us                                                 | 318 us: 1.06x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.24 sec: 1.06x slower                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.90 sec: 1.06x slower                                     |
| sqlglot_optimize           | 53.9 ms                                                | 57.3 ms: 1.06x slower                                      |
| mdp                        | 2.74 sec                                               | 2.93 sec: 1.07x slower                                     |
| pprint_safe_repr           | 744 ms                                                 | 796 ms: 1.07x slower                                       |
| pylint                     | 313 ms                                                 | 335 ms: 1.07x slower                                       |
| meteor_contest             | 108 ms                                                 | 115 ms: 1.07x slower                                       |
| pycparser                  | 1.19 sec                                               | 1.29 sec: 1.08x slower                                     |
| genshi_text                | 22.9 ms                                                | 24.6 ms: 1.08x slower                                      |
| comprehensions             | 16.4 us                                                | 17.7 us: 1.08x slower                                      |
| telco                      | 8.45 ms                                                | 9.10 ms: 1.08x slower                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.42 ms: 1.08x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.08x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.23 ms: 1.08x slower                                      |
| mako                       | 11.1 ms                                                | 12.0 ms: 1.08x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.64 sec: 1.08x slower                                     |
| django_template            | 34.4 ms                                                | 37.3 ms: 1.08x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 94.2 ms: 1.08x slower                                      |
| xml_etree_process          | 60.4 ms                                                | 65.4 ms: 1.08x slower                                      |
| hexiom                     | 6.13 ms                                                | 6.64 ms: 1.08x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.71 ms: 1.08x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.33 ms: 1.08x slower                                      |
| dulwich_log                | 63.0 ms                                                | 68.4 ms: 1.09x slower                                      |
| json_loads                 | 27.0 us                                                | 29.3 us: 1.09x slower                                      |
| logging_silent             | 102 ns                                                 | 111 ns: 1.09x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 55.0 ms: 1.09x slower                                      |
| html5lib                   | 64.5 ms                                                | 70.5 ms: 1.09x slower                                      |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.09x slower                                       |
| 2to3                       | 265 ms                                                 | 290 ms: 1.10x slower                                       |
| unpickle_pure_python       | 213 us                                                 | 234 us: 1.10x slower                                       |
| async_generators           | 433 ms                                                 | 476 ms: 1.10x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 172 ms: 1.10x slower                                       |
| sqlite_synth               | 2.85 us                                                | 3.15 us: 1.10x slower                                      |
| logging_simple             | 5.66 us                                                | 6.26 us: 1.10x slower                                      |
| pathlib                    | 17.1 ms                                                | 18.9 ms: 1.11x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 114 ms: 1.11x slower                                       |
| logging_format             | 6.25 us                                                | 6.96 us: 1.11x slower                                      |
| raytrace                   | 262 ms                                                 | 291 ms: 1.11x slower                                       |
| deepcopy_memo              | 38.0 us                                                | 42.4 us: 1.11x slower                                      |
| tornado_http               | 91.5 ms                                                | 102 ms: 1.12x slower                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 74.0 ms: 1.12x slower                                      |
| chaos                      | 58.4 ms                                                | 65.2 ms: 1.12x slower                                      |
| generators                 | 28.8 ms                                                | 32.3 ms: 1.12x slower                                      |
| float                      | 78.5 ms                                                | 88.3 ms: 1.12x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.56 ms: 1.13x slower                                      |
| docutils                   | 2.58 sec                                               | 2.95 sec: 1.14x slower                                     |
| python_startup             | 10.6 ms                                                | 12.1 ms: 1.14x slower                                      |
| chameleon                  | 6.85 ms                                                | 7.87 ms: 1.15x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.16x slower                                      |
| nbody                      | 85.7 ms                                                | 105 ms: 1.23x slower                                       |
| sympy_str                  | 274 ms                                                 | 342 ms: 1.25x slower                                       |
| flaskblogging              | 9.11 ms                                                | 12.6 ms: 1.39x slower                                      |
| sympy_expand               | 462 ms                                                 | 644 ms: 1.40x slower                                       |
| sympy_sum                  | 150 ms                                                 | 216 ms: 1.44x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 838 ms: 1.46x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 10.5 ms: 1.50x slower                                      |
| async_tree_none            | 354 ms                                                 | 533 ms: 1.51x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 702 ms: 1.51x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 848 ms: 1.56x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 704 ms: 1.59x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 537 ms: 1.68x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.49 sec: 1.77x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.50 sec: 1.82x slower                                     |
| bench_thread_pool          | 815 us                                                 | 2.54 ms: 3.11x slower                                      |
| coverage                   | 83.7 ms                                                | 690 ms: 8.24x slower                                       |
| thrift                     | 796 us                                                 | 9.30 ms: 11.67x slower                                     |
| fannkuch                   | 381 ms                                                 | 4.97 sec: 13.05x slower                                    |
| Geometric mean             | (ref)                                                  | 1.20x slower                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, djangocms, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.09x