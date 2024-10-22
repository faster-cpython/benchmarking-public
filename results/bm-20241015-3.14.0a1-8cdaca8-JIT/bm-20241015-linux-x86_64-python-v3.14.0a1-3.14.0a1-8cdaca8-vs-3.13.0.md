# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.03x slower
- HPT reliability: 70.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                       |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                     |
| html5lib       | 64.5 ms                                                | 63.7 ms: 1.01x faster                                      |
| tornado_http   | 91.5 ms                                                | 94.3 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                       |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                       |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                       |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 559 ms: 1.03x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.04x slower                                      |
| async_generators           | 433 ms                                                 | 478 ms: 1.10x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 966 ms: 1.17x slower                                       |
| Geometric mean             | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 81.3 ms: 1.06x faster                                      |
| float          | 78.5 ms                                                | 75.4 ms: 1.04x faster                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                       |
| regex_v8       | 25.3 ms                                                | 26.4 ms: 1.04x slower                                      |
| regex_compile  | 131 ms                                                 | 140 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.6 ms: 1.11x faster                                      |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                     |
| xml_etree_process    | 60.4 ms                                                | 55.5 ms: 1.09x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 102 ms                                                 | 99.9 ms: 1.02x faster                                      |
| json_loads           | 27.0 us                                                | 26.9 us: 1.00x faster                                      |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                       |
| pickle_pure_python   | 300 us                                                 | 310 us: 1.03x slower                                       |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| pickle_list          | 5.01 us                                                | 5.20 us: 1.04x slower                                      |
| pickle_dict          | 33.2 us                                                | 35.8 us: 1.08x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.59 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                      |
| python_startup         | 10.6 ms                                                | 11.9 ms: 1.13x slower                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                      |
| django_template | 34.4 ms                                                | 37.2 ms: 1.08x slower                                      |
| genshi_text     | 22.9 ms                                                | 25.2 ms: 1.10x slower                                      |
| genshi_xml      | 50.3 ms                                                | 58.9 ms: 1.17x slower                                      |
| Geometric mean  | (ref)                                                  | 1.06x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 273 us: 1.29x faster                                       |
| deepcopy_memo              | 38.0 us                                                | 29.4 us: 1.29x faster                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                       |
| richards                   | 48.1 ms                                                | 41.0 ms: 1.17x faster                                      |
| scimark_fft                | 369 ms                                                 | 319 ms: 1.16x faster                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                      |
| richards_super             | 54.4 ms                                                | 48.0 ms: 1.13x faster                                      |
| xml_etree_generate         | 87.0 ms                                                | 78.6 ms: 1.11x faster                                      |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                     |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                      |
| telco                      | 8.45 ms                                                | 7.68 ms: 1.10x faster                                      |
| xml_etree_process          | 60.4 ms                                                | 55.5 ms: 1.09x faster                                      |
| crypto_pyaes               | 73.0 ms                                                | 67.5 ms: 1.08x faster                                      |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                     |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.72 ms: 1.06x faster                                      |
| go                         | 142 ms                                                 | 133 ms: 1.06x faster                                       |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.44 sec: 1.06x faster                                     |
| nbody                      | 85.7 ms                                                | 81.3 ms: 1.06x faster                                      |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                      |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                       |
| json                       | 5.20 ms                                                | 4.95 ms: 1.05x faster                                      |
| logging_silent             | 102 ns                                                 | 98.0 ns: 1.04x faster                                      |
| float                      | 78.5 ms                                                | 75.4 ms: 1.04x faster                                      |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 64.1 ms: 1.03x faster                                      |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                     |
| pyflate                    | 460 ms                                                 | 446 ms: 1.03x faster                                       |
| pprint_safe_repr           | 744 ms                                                 | 726 ms: 1.03x faster                                       |
| xml_etree_iterparse        | 102 ms                                                 | 99.9 ms: 1.02x faster                                      |
| logging_format             | 6.25 us                                                | 6.13 us: 1.02x faster                                      |
| html5lib                   | 64.5 ms                                                | 63.7 ms: 1.01x faster                                      |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                       |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                       |
| fannkuch                   | 381 ms                                                 | 377 ms: 1.01x faster                                       |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| logging_simple             | 5.66 us                                                | 5.63 us: 1.01x faster                                      |
| json_loads                 | 27.0 us                                                | 26.9 us: 1.00x faster                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x slower                                       |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                       |
| pycparser                  | 1.19 sec                                               | 1.20 sec: 1.01x slower                                     |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                      |
| chaos                      | 58.4 ms                                                | 59.1 ms: 1.01x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.10 ms: 1.02x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                     |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 559 ms: 1.03x slower                                       |
| tornado_http               | 91.5 ms                                                | 94.3 ms: 1.03x slower                                      |
| pickle_pure_python         | 300 us                                                 | 310 us: 1.03x slower                                       |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.04x slower                                      |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.04x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| pickle_list                | 5.01 us                                                | 5.20 us: 1.04x slower                                      |
| regex_v8                   | 25.3 ms                                                | 26.4 ms: 1.04x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.29 ms: 1.05x slower                                      |
| 2to3                       | 265 ms                                                 | 277 ms: 1.05x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                      |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                       |
| dulwich_log                | 63.0 ms                                                | 66.5 ms: 1.06x slower                                      |
| regex_compile              | 131 ms                                                 | 140 ms: 1.07x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.07x slower                                       |
| nqueens                    | 80.6 ms                                                | 86.7 ms: 1.08x slower                                      |
| bench_thread_pool          | 815 us                                                 | 877 us: 1.08x slower                                       |
| pickle_dict                | 33.2 us                                                | 35.8 us: 1.08x slower                                      |
| django_template            | 34.4 ms                                                | 37.2 ms: 1.08x slower                                      |
| sympy_expand               | 462 ms                                                 | 502 ms: 1.09x slower                                       |
| genshi_text                | 22.9 ms                                                | 25.2 ms: 1.10x slower                                      |
| async_generators           | 433 ms                                                 | 478 ms: 1.10x slower                                       |
| sympy_str                  | 274 ms                                                 | 303 ms: 1.11x slower                                       |
| sqlglot_optimize           | 53.9 ms                                                | 60.2 ms: 1.12x slower                                      |
| unpickle_list              | 4.96 us                                                | 5.59 us: 1.13x slower                                      |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                     |
| python_startup             | 10.6 ms                                                | 11.9 ms: 1.13x slower                                      |
| hexiom                     | 6.13 ms                                                | 7.03 ms: 1.15x slower                                      |
| gc_traversal               | 3.81 ms                                                | 4.40 ms: 1.15x slower                                      |
| genshi_xml                 | 50.3 ms                                                | 58.9 ms: 1.17x slower                                      |
| async_tree_io_tg           | 825 ms                                                 | 966 ms: 1.17x slower                                       |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.18x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 23.6 ms: 1.19x slower                                      |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                       |
| generators                 | 28.8 ms                                                | 35.4 ms: 1.23x slower                                      |
| create_gc_cycles           | 1.61 ms                                                | 2.67 ms: 1.66x slower                                      |
| unpack_sequence            | 42.4 ns                                                | 110 ns: 2.60x slower                                       |
| bench_mp_pool              | 24.0 ms                                                | 84.2 ms: 3.51x slower                                      |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (6): unpickle, scimark_lu, sqlite_synth, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 70.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x