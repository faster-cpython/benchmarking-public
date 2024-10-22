# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: f2327f4
- commit date: 2024-09-18
- overall geometric mean: 1.01x slower
- HPT reliability: 88.49%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 282 ms: 1.07x slower                                                        |
| docutils       | 2.58 sec                                               | 3.20 sec: 1.24x slower                                                      |
| html5lib       | 64.5 ms                                                | 66.5 ms: 1.03x slower                                                       |
| tornado_http   | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| async_tree_none            | 354 ms                                                 | 360 ms: 1.02x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 605 ms: 1.05x slower                                                        |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 513 ms: 1.10x slower                                                        |
| async_tree_io              | 843 ms                                                 | 941 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 666 ms: 1.23x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 1.02 sec: 1.23x slower                                                      |
| async_tree_none_tg         | 320 ms                                                 | 401 ms: 1.25x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x slower                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                       |
| nbody          | 85.7 ms                                                | 81.1 ms: 1.06x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                       |
| regex_v8       | 25.3 ms                                                | 25.2 ms: 1.00x faster                                                       |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                        |
| regex_compile  | 131 ms                                                 | 138 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.4 ms: 1.12x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 54.2 ms: 1.12x faster                                                       |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| pickle               | 11.6 us                                                | 11.5 us: 1.00x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.00x slower                                                        |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                                        |
| pickle_list          | 5.01 us                                                | 5.09 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                        |
| pickle_dict          | 33.2 us                                                | 35.1 us: 1.06x slower                                                       |
| unpickle_list        | 4.96 us                                                | 5.41 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                       |
| django_template | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 26.0 ms: 1.13x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.9 us: 1.41x faster                                                       |
| deepcopy                   | 352 us                                                 | 250 us: 1.41x faster                                                        |
| richards                   | 48.1 ms                                                | 39.5 ms: 1.22x faster                                                       |
| scimark_fft                | 369 ms                                                 | 308 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.19x faster                                                       |
| richards_super             | 54.4 ms                                                | 45.6 ms: 1.19x faster                                                       |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.42 ms: 1.14x faster                                                       |
| go                         | 142 ms                                                 | 126 ms: 1.13x faster                                                        |
| xml_etree_generate         | 87.0 ms                                                | 77.4 ms: 1.12x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 54.2 ms: 1.12x faster                                                       |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 66.5 ms: 1.10x faster                                                       |
| float                      | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                       |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                      |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                       |
| regex_effbot               | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 62.6 ms: 1.06x faster                                                       |
| nbody                      | 85.7 ms                                                | 81.1 ms: 1.06x faster                                                       |
| telco                      | 8.45 ms                                                | 8.07 ms: 1.05x faster                                                       |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                        |
| json                       | 5.20 ms                                                | 4.99 ms: 1.04x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                        |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.85 us                                                | 2.76 us: 1.03x faster                                                       |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 725 ms: 1.03x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| pyflate                    | 460 ms                                                 | 452 ms: 1.02x faster                                                        |
| logging_format             | 6.25 us                                                | 6.20 us: 1.01x faster                                                       |
| thrift                     | 796 us                                                 | 791 us: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                        |
| regex_v8                   | 25.3 ms                                                | 25.2 ms: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| pickle                     | 11.6 us                                                | 11.5 us: 1.00x faster                                                       |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.71 sec: 1.00x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.00x slower                                                        |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                        |
| chaos                      | 58.4 ms                                                | 58.9 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                       |
| pycparser                  | 1.19 sec                                               | 1.21 sec: 1.02x slower                                                      |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.02x slower                                                        |
| pickle_list                | 5.01 us                                                | 5.09 us: 1.02x slower                                                       |
| async_tree_none            | 354 ms                                                 | 360 ms: 1.02x slower                                                        |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                       |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                        |
| deltablue                  | 3.15 ms                                                | 3.21 ms: 1.02x slower                                                       |
| coverage                   | 83.7 ms                                                | 85.9 ms: 1.03x slower                                                       |
| bench_thread_pool          | 815 us                                                 | 837 us: 1.03x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| html5lib                   | 64.5 ms                                                | 66.5 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                        |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 111 ms: 1.04x slower                                                        |
| tornado_http               | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                       |
| django_template            | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                       |
| regex_compile              | 131 ms                                                 | 138 ms: 1.05x slower                                                        |
| nqueens                    | 80.6 ms                                                | 84.6 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 605 ms: 1.05x slower                                                        |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                        |
| pickle_dict                | 33.2 us                                                | 35.1 us: 1.06x slower                                                       |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 57.1 ms: 1.06x slower                                                       |
| gc_traversal               | 3.81 ms                                                | 4.04 ms: 1.06x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                       |
| 2to3                       | 265 ms                                                 | 282 ms: 1.07x slower                                                        |
| dulwich_log                | 63.0 ms                                                | 67.6 ms: 1.07x slower                                                       |
| sympy_str                  | 274 ms                                                 | 296 ms: 1.08x slower                                                        |
| sympy_expand               | 462 ms                                                 | 503 ms: 1.09x slower                                                        |
| unpickle_list              | 4.96 us                                                | 5.41 us: 1.09x slower                                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.73 ms: 1.10x slower                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 513 ms: 1.10x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.83 ms: 1.12x slower                                                       |
| async_tree_io              | 843 ms                                                 | 941 ms: 1.12x slower                                                        |
| generators                 | 28.8 ms                                                | 32.6 ms: 1.13x slower                                                       |
| genshi_text                | 22.9 ms                                                | 26.0 ms: 1.13x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.15x slower                                                        |
| genshi_xml                 | 50.3 ms                                                | 58.8 ms: 1.17x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 666 ms: 1.23x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 1.02 sec: 1.23x slower                                                      |
| docutils                   | 2.58 sec                                               | 3.20 sec: 1.24x slower                                                      |
| async_tree_none_tg         | 320 ms                                                 | 401 ms: 1.25x slower                                                        |
| unpack_sequence            | 42.4 ns                                                | 107 ns: 2.52x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (8): fannkuch, logging_simple, unpickle, bench_mp_pool, json_loads, asyncio_websockets, pylint, async_tree_memoization
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 88.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x