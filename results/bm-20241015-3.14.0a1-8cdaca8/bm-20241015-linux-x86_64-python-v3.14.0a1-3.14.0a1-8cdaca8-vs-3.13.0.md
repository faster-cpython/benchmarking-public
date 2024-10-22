# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.01x slower
- HPT reliability: 84.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                       |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                     |
| html5lib       | 64.5 ms                                                | 61.9 ms: 1.04x faster                                      |
| tornado_http   | 91.5 ms                                                | 89.9 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                       |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.08x faster                                       |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                       |
| asyncio_tcp                | 488 ms                                                 | 486 ms: 1.00x faster                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                     |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                      |
| async_generators           | 433 ms                                                 | 447 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 562 ms: 1.03x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 968 ms: 1.17x slower                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| float          | 78.5 ms                                                | 79.2 ms: 1.01x slower                                      |
| nbody          | 85.7 ms                                                | 88.8 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.60 ms: 1.08x faster                                      |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                       |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                       |
| regex_v8       | 25.3 ms                                                | 25.5 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.09 sec: 1.01x faster                                     |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| json_loads           | 27.0 us                                                | 26.9 us: 1.00x faster                                      |
| pickle_dict          | 33.2 us                                                | 33.3 us: 1.00x slower                                      |
| xml_etree_generate   | 87.0 ms                                                | 87.5 ms: 1.01x slower                                      |
| unpickle             | 14.9 us                                                | 15.0 us: 1.01x slower                                      |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                       |
| pickle_list          | 5.01 us                                                | 5.10 us: 1.02x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                       |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                       |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.49 us: 1.11x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.02 ms: 1.00x slower                                      |
| python_startup         | 10.6 ms                                                | 11.8 ms: 1.12x slower                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.0 ms: 1.01x faster                                      |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| genshi_text     | 22.9 ms                                                | 23.4 ms: 1.02x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.1 ms: 1.03x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 264 us: 1.34x faster                                       |
| deepcopy_memo              | 38.0 us                                                | 30.4 us: 1.25x faster                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                       |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                      |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.08x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.60 ms: 1.08x faster                                      |
| generators                 | 28.8 ms                                                | 27.0 ms: 1.07x faster                                      |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                       |
| pycparser                  | 1.19 sec                                               | 1.12 sec: 1.06x faster                                     |
| telco                      | 8.45 ms                                                | 7.97 ms: 1.06x faster                                      |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.79 ms: 1.05x faster                                      |
| richards                   | 48.1 ms                                                | 46.0 ms: 1.05x faster                                      |
| 2to3                       | 265 ms                                                 | 254 ms: 1.04x faster                                       |
| html5lib                   | 64.5 ms                                                | 61.9 ms: 1.04x faster                                      |
| json                       | 5.20 ms                                                | 5.03 ms: 1.03x faster                                      |
| richards_super             | 54.4 ms                                                | 52.8 ms: 1.03x faster                                      |
| thrift                     | 796 us                                                 | 773 us: 1.03x faster                                       |
| mdp                        | 2.74 sec                                               | 2.67 sec: 1.03x faster                                     |
| sympy_str                  | 274 ms                                                 | 266 ms: 1.03x faster                                       |
| logging_simple             | 5.66 us                                                | 5.52 us: 1.03x faster                                      |
| sympy_expand               | 462 ms                                                 | 450 ms: 1.03x faster                                       |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                       |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                       |
| scimark_fft                | 369 ms                                                 | 360 ms: 1.02x faster                                       |
| logging_format             | 6.25 us                                                | 6.13 us: 1.02x faster                                      |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                       |
| tornado_http               | 91.5 ms                                                | 89.9 ms: 1.02x faster                                      |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                       |
| pprint_safe_repr           | 744 ms                                                 | 734 ms: 1.01x faster                                       |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                      |
| django_template            | 34.4 ms                                                | 34.0 ms: 1.01x faster                                      |
| crypto_pyaes               | 73.0 ms                                                | 72.1 ms: 1.01x faster                                      |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| tomli_loads                | 2.11 sec                                               | 2.09 sec: 1.01x faster                                     |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                       |
| nqueens                    | 80.6 ms                                                | 79.9 ms: 1.01x faster                                      |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| asyncio_tcp                | 488 ms                                                 | 486 ms: 1.00x faster                                       |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                       |
| json_loads                 | 27.0 us                                                | 26.9 us: 1.00x faster                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                     |
| pickle_dict                | 33.2 us                                                | 33.3 us: 1.00x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.02 ms: 1.00x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 87.5 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| unpickle                   | 14.9 us                                                | 15.0 us: 1.01x slower                                      |
| dulwich_log                | 63.0 ms                                                | 63.5 ms: 1.01x slower                                      |
| float                      | 78.5 ms                                                | 79.2 ms: 1.01x slower                                      |
| regex_v8                   | 25.3 ms                                                | 25.5 ms: 1.01x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                      |
| hexiom                     | 6.13 ms                                                | 6.19 ms: 1.01x slower                                      |
| typing_runtime_protocols   | 159 us                                                 | 161 us: 1.01x slower                                       |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                       |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 67.4 ms: 1.02x slower                                      |
| pickle_list                | 5.01 us                                                | 5.10 us: 1.02x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.80 sec: 1.02x slower                                     |
| pyflate                    | 460 ms                                                 | 471 ms: 1.02x slower                                       |
| genshi_text                | 22.9 ms                                                | 23.4 ms: 1.02x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.02x slower                                      |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                       |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                     |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                      |
| bench_thread_pool          | 815 us                                                 | 837 us: 1.03x slower                                       |
| chaos                      | 58.4 ms                                                | 60.1 ms: 1.03x slower                                      |
| async_generators           | 433 ms                                                 | 447 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 562 ms: 1.03x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 52.1 ms: 1.03x slower                                      |
| nbody                      | 85.7 ms                                                | 88.8 ms: 1.04x slower                                      |
| pickle_pure_python         | 300 us                                                 | 313 us: 1.04x slower                                       |
| fannkuch                   | 381 ms                                                 | 404 ms: 1.06x slower                                       |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                      |
| unpickle_list              | 4.96 us                                                | 5.49 us: 1.11x slower                                      |
| python_startup             | 10.6 ms                                                | 11.8 ms: 1.12x slower                                      |
| unpack_sequence            | 42.4 ns                                                | 48.5 ns: 1.14x slower                                      |
| async_tree_io_tg           | 825 ms                                                 | 968 ms: 1.17x slower                                       |
| gc_traversal               | 3.81 ms                                                | 4.54 ms: 1.19x slower                                      |
| create_gc_cycles           | 1.61 ms                                                | 2.67 ms: 1.66x slower                                      |
| bench_mp_pool              | 24.0 ms                                                | 77.9 ms: 3.25x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (12): sympy_integrate, asyncio_websockets, coverage, pprint_pformat, sqlite_synth, raytrace, async_tree_cpu_io_mixed, xml_etree_process, async_tree_none_tg, xml_etree_parse, async_tree_io, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 84.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x