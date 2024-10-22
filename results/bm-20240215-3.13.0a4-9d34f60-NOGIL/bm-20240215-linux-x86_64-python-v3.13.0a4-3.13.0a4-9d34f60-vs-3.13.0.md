# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 296 ms: 1.12x slower                                       |
| chameleon      | 6.85 ms                                                | 8.24 ms: 1.20x slower                                      |
| docutils       | 2.58 sec                                               | 3.07 sec: 1.19x slower                                     |
| html5lib       | 64.5 ms                                                | 67.9 ms: 1.05x slower                                      |
| tornado_http   | 91.5 ms                                                | 98.6 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.13x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io              | 843 ms                                                 | 796 ms: 1.06x faster                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 458 ms: 1.01x faster                                       |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 508 ms: 1.04x slower                                       |
| async_tree_none            | 354 ms                                                 | 377 ms: 1.07x slower                                       |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 476 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 646 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 612 ms: 1.13x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 377 ms: 1.18x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 78.5 ms                                                | 74.2 ms: 1.06x faster                                      |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| nbody          | 85.7 ms                                                | 104 ms: 1.21x slower                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.60 ms: 1.08x faster                                      |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                      |
| regex_dna      | 220 ms                                                 | 232 ms: 1.06x slower                                       |
| regex_compile  | 131 ms                                                 | 141 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 151 ms: 1.03x faster                                       |
| pickle_list          | 5.01 us                                                | 4.88 us: 1.03x faster                                      |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| xml_etree_generate   | 87.0 ms                                                | 90.5 ms: 1.04x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.21 us: 1.05x slower                                      |
| tomli_loads          | 2.11 sec                                               | 2.23 sec: 1.06x slower                                     |
| pickle_pure_python   | 300 us                                                 | 333 us: 1.11x slower                                       |
| unpickle_pure_python | 213 us                                                 | 237 us: 1.11x slower                                       |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                      |
| xml_etree_process    | 60.4 ms                                                | 71.1 ms: 1.18x slower                                      |
| json_loads           | 27.0 us                                                | 32.2 us: 1.19x slower                                      |
| unpickle             | 14.9 us                                                | 18.0 us: 1.21x slower                                      |
| pickle_dict          | 33.2 us                                                | 41.2 us: 1.24x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 166 ms: 1.62x slower                                       |
| Geometric mean       | (ref)                                                  | 1.13x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 12.0 ms: 1.14x slower                                      |
| python_startup_no_site | 6.99 ms                                                | 10.0 ms: 1.44x slower                                      |
| Geometric mean         | (ref)                                                  | 1.28x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 54.7 ms: 1.09x slower                                      |
| django_template | 34.4 ms                                                | 39.1 ms: 1.14x slower                                      |
| genshi_text     | 22.9 ms                                                | 26.1 ms: 1.14x slower                                      |
| mako            | 11.1 ms                                                | 16.3 ms: 1.47x slower                                      |
| Geometric mean  | (ref)                                                  | 1.20x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.61 ms                                                | 1.03 ms: 1.56x faster                                      |
| mypy2                      | 1.07 sec                                               | 696 ms: 1.53x faster                                       |
| gc_traversal               | 3.81 ms                                                | 2.57 ms: 1.48x faster                                      |
| typing_runtime_protocols   | 159 us                                                 | 122 us: 1.31x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.60 ms: 1.08x faster                                      |
| async_tree_io              | 843 ms                                                 | 796 ms: 1.06x faster                                       |
| float                      | 78.5 ms                                                | 74.2 ms: 1.06x faster                                      |
| pylint                     | 313 ms                                                 | 296 ms: 1.06x faster                                       |
| xml_etree_parse            | 156 ms                                                 | 151 ms: 1.03x faster                                       |
| pickle_list                | 5.01 us                                                | 4.88 us: 1.03x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.4 ms: 1.02x faster                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 458 ms: 1.01x faster                                       |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                      |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                      |
| richards                   | 48.1 ms                                                | 49.2 ms: 1.02x slower                                      |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                       |
| scimark_fft                | 369 ms                                                 | 380 ms: 1.03x slower                                       |
| pyflate                    | 460 ms                                                 | 474 ms: 1.03x slower                                       |
| richards_super             | 54.4 ms                                                | 56.3 ms: 1.03x slower                                      |
| crypto_pyaes               | 73.0 ms                                                | 75.5 ms: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                     |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 90.5 ms: 1.04x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 508 ms: 1.04x slower                                       |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.25 ms: 1.04x slower                                      |
| scimark_lu                 | 115 ms                                                 | 121 ms: 1.05x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.21 us: 1.05x slower                                      |
| nqueens                    | 80.6 ms                                                | 84.7 ms: 1.05x slower                                      |
| html5lib                   | 64.5 ms                                                | 67.9 ms: 1.05x slower                                      |
| regex_dna                  | 220 ms                                                 | 232 ms: 1.06x slower                                       |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.06x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.23 sec: 1.06x slower                                     |
| async_tree_none            | 354 ms                                                 | 377 ms: 1.07x slower                                       |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 797 ms: 1.07x slower                                       |
| regex_compile              | 131 ms                                                 | 141 ms: 1.07x slower                                       |
| meteor_contest             | 108 ms                                                 | 115 ms: 1.07x slower                                       |
| telco                      | 8.45 ms                                                | 9.09 ms: 1.08x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 476 ms: 1.08x slower                                       |
| tornado_http               | 91.5 ms                                                | 98.6 ms: 1.08x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 116 ms: 1.08x slower                                       |
| hexiom                     | 6.13 ms                                                | 6.62 ms: 1.08x slower                                      |
| generators                 | 28.8 ms                                                | 31.2 ms: 1.08x slower                                      |
| genshi_xml                 | 50.3 ms                                                | 54.7 ms: 1.09x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.64 sec: 1.09x slower                                     |
| go                         | 142 ms                                                 | 154 ms: 1.09x slower                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.46 us: 1.09x slower                                      |
| dulwich_log                | 63.0 ms                                                | 69.0 ms: 1.10x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 59.3 ms: 1.10x slower                                      |
| deepcopy                   | 352 us                                                 | 390 us: 1.11x slower                                       |
| pickle_pure_python         | 300 us                                                 | 333 us: 1.11x slower                                       |
| aiohttp                    | 1.14 ms                                                | 1.27 ms: 1.11x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 237 us: 1.11x slower                                       |
| sqlite_synth               | 2.85 us                                                | 3.17 us: 1.11x slower                                      |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                      |
| pathlib                    | 17.1 ms                                                | 19.0 ms: 1.11x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 74.0 ms: 1.12x slower                                      |
| json                       | 5.20 ms                                                | 5.81 ms: 1.12x slower                                      |
| logging_silent             | 102 ns                                                 | 114 ns: 1.12x slower                                       |
| 2to3                       | 265 ms                                                 | 296 ms: 1.12x slower                                       |
| gunicorn                   | 1.23 ms                                                | 1.37 ms: 1.12x slower                                      |
| fannkuch                   | 381 ms                                                 | 428 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 646 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 612 ms: 1.13x slower                                       |
| comprehensions             | 16.4 us                                                | 18.5 us: 1.13x slower                                      |
| chaos                      | 58.4 ms                                                | 66.2 ms: 1.13x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.78 ms: 1.13x slower                                      |
| logging_simple             | 5.66 us                                                | 6.43 us: 1.13x slower                                      |
| django_template            | 34.4 ms                                                | 39.1 ms: 1.14x slower                                      |
| python_startup             | 10.6 ms                                                | 12.0 ms: 1.14x slower                                      |
| raytrace                   | 262 ms                                                 | 298 ms: 1.14x slower                                       |
| genshi_text                | 22.9 ms                                                | 26.1 ms: 1.14x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.44 ms: 1.14x slower                                      |
| logging_format             | 6.25 us                                                | 7.18 us: 1.15x slower                                      |
| xml_etree_process          | 60.4 ms                                                | 71.1 ms: 1.18x slower                                      |
| async_tree_none_tg         | 320 ms                                                 | 377 ms: 1.18x slower                                       |
| docutils                   | 2.58 sec                                               | 3.07 sec: 1.19x slower                                     |
| json_loads                 | 27.0 us                                                | 32.2 us: 1.19x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 23.8 ms: 1.20x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 45.6 us: 1.20x slower                                      |
| chameleon                  | 6.85 ms                                                | 8.24 ms: 1.20x slower                                      |
| unpickle                   | 14.9 us                                                | 18.0 us: 1.21x slower                                      |
| nbody                      | 85.7 ms                                                | 104 ms: 1.21x slower                                       |
| pickle_dict                | 33.2 us                                                | 41.2 us: 1.24x slower                                      |
| sympy_str                  | 274 ms                                                 | 354 ms: 1.29x slower                                       |
| deltablue                  | 3.15 ms                                                | 4.16 ms: 1.32x slower                                      |
| mdp                        | 2.74 sec                                               | 3.64 sec: 1.33x slower                                     |
| sympy_expand               | 462 ms                                                 | 623 ms: 1.35x slower                                       |
| sympy_sum                  | 150 ms                                                 | 211 ms: 1.41x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 10.0 ms: 1.44x slower                                      |
| mako                       | 11.1 ms                                                | 16.3 ms: 1.47x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 166 ms: 1.62x slower                                       |
| flaskblogging              | 9.11 ms                                                | 18.7 ms: 2.05x slower                                      |
| bench_thread_pool          | 815 us                                                 | 2.42 ms: 2.98x slower                                      |
| coverage                   | 83.7 ms                                                | 712 ms: 8.50x slower                                       |
| thrift                     | 796 us                                                 | 9.43 ms: 11.84x slower                                     |
| Geometric mean             | (ref)                                                  | 1.15x slower                                               |

Benchmark hidden because not significant (3): pycparser, async_tree_io_tg, asyncio_websockets
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, djangocms, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.07x