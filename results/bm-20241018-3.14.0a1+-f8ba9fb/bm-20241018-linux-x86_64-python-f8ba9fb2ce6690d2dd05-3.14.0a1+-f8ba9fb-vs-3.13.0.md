# Results vs. 3.13.0

- fork: python
- ref: f8ba9fb2ce6690d2dd05
- machine: linux-x86_64
- commit hash: f8ba9fb
- commit date: 2024-10-18
- overall geometric mean: 1.02x slower
- HPT reliability: 68.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                   |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                 |
| html5lib       | 64.5 ms                                                | 63.6 ms: 1.02x faster                                                  |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                   |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                                   |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                 |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 563 ms: 1.04x slower                                                   |
| async_tree_io_tg           | 825 ms                                                 | 975 ms: 1.18x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (5): async_generators, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| float          | 78.5 ms                                                | 79.9 ms: 1.02x slower                                                  |
| nbody          | 85.7 ms                                                | 93.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                  |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                   |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                  |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                | 26.4 us: 1.02x faster                                                  |
| unpickle             | 14.9 us                                                | 14.6 us: 1.02x faster                                                  |
| xml_etree_process    | 60.4 ms                                                | 59.7 ms: 1.01x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                  |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 155 ms: 1.01x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| pickle_dict          | 33.2 us                                                | 33.9 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                   |
| pickle_list          | 5.01 us                                                | 5.21 us: 1.04x slower                                                  |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| unpickle_list        | 4.96 us                                                | 5.57 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                  |
| python_startup         | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                  |
| genshi_text     | 22.9 ms                                                | 23.2 ms: 1.01x slower                                                  |
| genshi_xml      | 50.3 ms                                                | 51.2 ms: 1.02x slower                                                  |
| mako            | 11.1 ms                                                | 11.7 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 264 us: 1.34x faster                                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                   |
| deepcopy_memo              | 38.0 us                                                | 31.1 us: 1.22x faster                                                  |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 3.17 us                                                | 2.74 us: 1.16x faster                                                  |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                   |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                  |
| json                       | 5.20 ms                                                | 4.87 ms: 1.07x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                                   |
| telco                      | 8.45 ms                                                | 8.02 ms: 1.05x faster                                                  |
| richards                   | 48.1 ms                                                | 45.7 ms: 1.05x faster                                                  |
| richards_super             | 54.4 ms                                                | 52.0 ms: 1.05x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.63 sec: 1.04x faster                                                 |
| 2to3                       | 265 ms                                                 | 254 ms: 1.04x faster                                                   |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                  |
| thrift                     | 796 us                                                 | 775 us: 1.03x faster                                                   |
| sympy_str                  | 274 ms                                                 | 266 ms: 1.03x faster                                                   |
| json_loads                 | 27.0 us                                                | 26.4 us: 1.02x faster                                                  |
| sympy_expand               | 462 ms                                                 | 452 ms: 1.02x faster                                                   |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 729 ms: 1.02x faster                                                   |
| django_template            | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                  |
| unpickle                   | 14.9 us                                                | 14.6 us: 1.02x faster                                                  |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                 |
| html5lib                   | 64.5 ms                                                | 63.6 ms: 1.02x faster                                                  |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 59.7 ms: 1.01x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                  |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                                   |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                  |
| logging_format             | 6.25 us                                                | 6.21 us: 1.01x faster                                                  |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                  |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 155 ms: 1.01x faster                                                   |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.05 ms: 1.00x slower                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                  |
| scimark_lu                 | 115 ms                                                 | 116 ms: 1.01x slower                                                   |
| dulwich_log                | 63.0 ms                                                | 63.4 ms: 1.01x slower                                                  |
| crypto_pyaes               | 73.0 ms                                                | 73.8 ms: 1.01x slower                                                  |
| coverage                   | 83.7 ms                                                | 84.8 ms: 1.01x slower                                                  |
| genshi_text                | 22.9 ms                                                | 23.2 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                  |
| nqueens                    | 80.6 ms                                                | 81.7 ms: 1.01x slower                                                  |
| scimark_fft                | 369 ms                                                 | 374 ms: 1.02x slower                                                   |
| genshi_xml                 | 50.3 ms                                                | 51.2 ms: 1.02x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                  |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                   |
| float                      | 78.5 ms                                                | 79.9 ms: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.02x slower                                                   |
| sqlite_synth               | 2.85 us                                                | 2.91 us: 1.02x slower                                                  |
| pyflate                    | 460 ms                                                 | 470 ms: 1.02x slower                                                   |
| pickle_dict                | 33.2 us                                                | 33.9 us: 1.02x slower                                                  |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.82 sec: 1.03x slower                                                 |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                   |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 68.6 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 563 ms: 1.04x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 846 us: 1.04x slower                                                   |
| hexiom                     | 6.13 ms                                                | 6.37 ms: 1.04x slower                                                  |
| pickle_list                | 5.01 us                                                | 5.21 us: 1.04x slower                                                  |
| pickle_pure_python         | 300 us                                                 | 313 us: 1.04x slower                                                   |
| chaos                      | 58.4 ms                                                | 61.0 ms: 1.04x slower                                                  |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                   |
| unpack_sequence            | 42.4 ns                                                | 44.6 ns: 1.05x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.32 ms: 1.05x slower                                                  |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.06x slower                                                  |
| nbody                      | 85.7 ms                                                | 93.0 ms: 1.08x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| fannkuch                   | 381 ms                                                 | 414 ms: 1.09x slower                                                   |
| python_startup             | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                  |
| unpickle_list              | 4.96 us                                                | 5.57 us: 1.12x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 975 ms: 1.18x slower                                                   |
| gc_traversal               | 3.81 ms                                                | 4.73 ms: 1.24x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 2.70 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 78.0 ms: 3.25x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (8): async_generators, meteor_contest, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg, tomli_loads, async_tree_io, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241018-3.14.0a1+-f8ba9fb/bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb.json: sphinx

# HPT report

- Reliability score: 68.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x