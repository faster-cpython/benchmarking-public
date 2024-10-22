# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                       |
| chameleon      | 6.85 ms                                                | 6.93 ms: 1.01x slower                                      |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                     |
| html5lib       | 64.5 ms                                                | 67.3 ms: 1.04x slower                                      |
| tornado_http   | 91.5 ms                                                | 96.9 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                       |
| asyncio_websockets         | 555 ms                                                 | 553 ms: 1.00x faster                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                     |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 710 ms: 1.24x slower                                       |
| async_tree_none            | 354 ms                                                 | 438 ms: 1.24x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 576 ms: 1.24x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 565 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 723 ms: 1.33x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 448 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.20 sec: 1.46x slower                                     |
| Geometric mean             | (ref)                                                  | 1.19x slower                                               |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| float          | 78.5 ms                                                | 85.3 ms: 1.09x slower                                      |
| nbody          | 85.7 ms                                                | 103 ms: 1.20x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.59 ms: 1.08x faster                                      |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                       |
| regex_v8       | 25.3 ms                                                | 25.2 ms: 1.00x faster                                      |
| regex_compile  | 131 ms                                                 | 138 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.4 ms: 1.03x faster                                      |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| xml_etree_generate   | 87.0 ms                                                | 86.0 ms: 1.01x faster                                      |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                       |
| json_loads           | 27.0 us                                                | 27.5 us: 1.02x slower                                      |
| unpickle             | 14.9 us                                                | 15.3 us: 1.03x slower                                      |
| pickle_dict          | 33.2 us                                                | 34.2 us: 1.03x slower                                      |
| tomli_loads          | 2.11 sec                                               | 2.21 sec: 1.05x slower                                     |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| unpickle_pure_python | 213 us                                                 | 230 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (4): json_dumps, pickle_list, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.2 ms: 1.04x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 8.84 ms: 1.26x slower                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                      |
| genshi_text     | 22.9 ms                                                | 23.4 ms: 1.02x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.7 ms: 1.05x slower                                      |
| mako            | 11.1 ms                                                | 12.1 ms: 1.09x slower                                      |
| Geometric mean  | (ref)                                                  | 1.04x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 111 us: 1.43x faster                                       |
| mypy2                      | 1.07 sec                                               | 865 ms: 1.23x faster                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.48 ms: 1.09x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.59 ms: 1.08x faster                                      |
| richards                   | 48.1 ms                                                | 45.3 ms: 1.06x faster                                      |
| richards_super             | 54.4 ms                                                | 51.7 ms: 1.05x faster                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.03 us: 1.05x faster                                      |
| python_startup             | 10.6 ms                                                | 10.2 ms: 1.04x faster                                      |
| xml_etree_process          | 60.4 ms                                                | 58.4 ms: 1.03x faster                                      |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                       |
| json                       | 5.20 ms                                                | 5.07 ms: 1.02x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.72 ms: 1.02x faster                                      |
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                       |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                       |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                     |
| xml_etree_generate         | 87.0 ms                                                | 86.0 ms: 1.01x faster                                      |
| thrift                     | 796 us                                                 | 789 us: 1.01x faster                                       |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                     |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                       |
| deepcopy                   | 352 us                                                 | 350 us: 1.01x faster                                       |
| sqlite_synth               | 2.85 us                                                | 2.83 us: 1.01x faster                                      |
| pickle_pure_python         | 300 us                                                 | 298 us: 1.01x faster                                       |
| django_template            | 34.4 ms                                                | 34.2 ms: 1.01x faster                                      |
| asyncio_websockets         | 555 ms                                                 | 553 ms: 1.00x faster                                       |
| regex_v8                   | 25.3 ms                                                | 25.2 ms: 1.00x faster                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                     |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x slower                                       |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                      |
| chameleon                  | 6.85 ms                                                | 6.93 ms: 1.01x slower                                      |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.01x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 38.5 us: 1.01x slower                                      |
| scimark_lu                 | 115 ms                                                 | 117 ms: 1.02x slower                                       |
| json_loads                 | 27.0 us                                                | 27.5 us: 1.02x slower                                      |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                     |
| genshi_text                | 22.9 ms                                                | 23.4 ms: 1.02x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                      |
| logging_simple             | 5.66 us                                                | 5.81 us: 1.03x slower                                      |
| unpickle                   | 14.9 us                                                | 15.3 us: 1.03x slower                                      |
| flaskblogging              | 9.11 ms                                                | 9.37 ms: 1.03x slower                                      |
| djangocms                  | 31.9 us                                                | 32.8 us: 1.03x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.18 ms: 1.03x slower                                      |
| bench_thread_pool          | 815 us                                                 | 839 us: 1.03x slower                                       |
| pickle_dict                | 33.2 us                                                | 34.2 us: 1.03x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 55.7 ms: 1.03x slower                                      |
| sympy_str                  | 274 ms                                                 | 283 ms: 1.03x slower                                       |
| gunicorn                   | 1.23 ms                                                | 1.27 ms: 1.03x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 20.6 ms: 1.03x slower                                      |
| logging_format             | 6.25 us                                                | 6.47 us: 1.03x slower                                      |
| pprint_safe_repr           | 744 ms                                                 | 770 ms: 1.04x slower                                       |
| html5lib                   | 64.5 ms                                                | 67.3 ms: 1.04x slower                                      |
| 2to3                       | 265 ms                                                 | 277 ms: 1.05x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 52.7 ms: 1.05x slower                                      |
| go                         | 142 ms                                                 | 148 ms: 1.05x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.21 sec: 1.05x slower                                     |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| sympy_expand               | 462 ms                                                 | 484 ms: 1.05x slower                                       |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                       |
| regex_compile              | 131 ms                                                 | 138 ms: 1.05x slower                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.30 ms: 1.05x slower                                      |
| tornado_http               | 91.5 ms                                                | 96.9 ms: 1.06x slower                                      |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.06x slower                                       |
| raytrace                   | 262 ms                                                 | 279 ms: 1.07x slower                                       |
| deltablue                  | 3.15 ms                                                | 3.37 ms: 1.07x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 230 us: 1.08x slower                                       |
| crypto_pyaes               | 73.0 ms                                                | 78.6 ms: 1.08x slower                                      |
| pathlib                    | 17.1 ms                                                | 18.4 ms: 1.08x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.63 sec: 1.08x slower                                     |
| float                      | 78.5 ms                                                | 85.3 ms: 1.09x slower                                      |
| mako                       | 11.1 ms                                                | 12.1 ms: 1.09x slower                                      |
| dulwich_log                | 63.0 ms                                                | 68.7 ms: 1.09x slower                                      |
| bpe_tokeniser              | 4.69 sec                                               | 5.15 sec: 1.10x slower                                     |
| pyflate                    | 460 ms                                                 | 507 ms: 1.10x slower                                       |
| fannkuch                   | 381 ms                                                 | 420 ms: 1.10x slower                                       |
| comprehensions             | 16.4 us                                                | 18.3 us: 1.12x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 74.5 ms: 1.12x slower                                      |
| nqueens                    | 80.6 ms                                                | 91.0 ms: 1.13x slower                                      |
| coverage                   | 83.7 ms                                                | 94.7 ms: 1.13x slower                                      |
| spectral_norm              | 115 ms                                                 | 132 ms: 1.15x slower                                       |
| chaos                      | 58.4 ms                                                | 69.5 ms: 1.19x slower                                      |
| nbody                      | 85.7 ms                                                | 103 ms: 1.20x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 710 ms: 1.24x slower                                       |
| async_tree_none            | 354 ms                                                 | 438 ms: 1.24x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 576 ms: 1.24x slower                                       |
| unpack_sequence            | 42.4 ns                                                | 52.6 ns: 1.24x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 8.84 ms: 1.26x slower                                      |
| hexiom                     | 6.13 ms                                                | 7.76 ms: 1.27x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 565 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 723 ms: 1.33x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 448 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.20 sec: 1.46x slower                                     |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (9): pylint, telco, json_dumps, pickle_list, bench_mp_pool, unpickle_list, scimark_fft, xml_etree_parse, coroutines
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x